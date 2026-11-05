"""Guard of the sealed test (PreToolUse hook, every agent and the main session).

The test period of a strategy is opened in one place only: lab/run_test.py, which Claude Code runs only after the
user approves it (rule "ask" in .claude/settings.json). This hook closes the other doors:
1. Bash: no command may pass open_test=True (python -c, a script, a heredoc), touch a TEST_DONE lock, or call
   run_test other than as `poetry run python lab/run_test.py ...` or `python3 lab/run_test.py ...`.
2. Write and Edit: no file may be written with open_test=True in it, no TEST_DONE lock, and nobody edits
   lab/run_test.py, this hook or .claude/settings.json.

It stops mistakes and shortcuts, not a determined attacker: the real protection is the lock, the code hash and git.
Exit code 0 lets the call through; exit code 2 blocks it and shows the message to the agent.
"""
from __future__ import annotations

import json
import re
import sys

OPEN_TEST = re.compile(r"""open_test["']?\s*[:=]\s*(True|1|not\s+False)\b""")
LOCK = re.compile(r"TEST_DONE")
RUN_TEST = re.compile(r"run_test")
ALLOWED_RUN = re.compile(r"^\s*(cd\s+[^;&|]+&&\s*)?(poetry run python|python3?)\s+lab/run_test\.py(\s|$)")
PROTECTED = ("lab/run_test.py", ".claude/hooks/test_guard.py", ".claude/settings.json")
READS_TEST_AFTER_LOCK = ("lab/strategy_report.py", "lab/book_report.py")     # reports: read the test only once it is opened
READ_ONLY_CMDS = re.compile(r"^\s*(cat|ls|head|tail|grep|wc|find|git (status|log|diff|show))\b")


def block(msg: str) -> None:
    print(msg, file=sys.stderr)
    sys.exit(2)


def check_bash(cmd: str) -> None:
    if ALLOWED_RUN.match(cmd) and not re.search(r"[;|&`<>]|\$\(", cmd.split("run_test.py", 1)[1]):
        return                                                         # the one door; Claude Code asks the user first
    if READ_ONLY_CMDS.match(cmd) and not re.search(r"[>;&`]|\$\(|\|\s*(sh|bash|python|xargs)|-delete|-exec", cmd):
        return                                                         # reading a lock or a file is fine
    if OPEN_TEST.search(cmd):
        block("Blocked: only lab/run_test.py opens a test, after the user approves it. Ask for the test in the "
              "desk's batch (`poetry run python lab/run_test.py --batch FILE:VARIANT ...`) instead.")
    if LOCK.search(cmd):
        block("Blocked: TEST_DONE locks are written by lab/run_test.py only, and never removed or edited.")
    if RUN_TEST.search(cmd):
        block("Blocked: run the test only as `poetry run python lab/run_test.py ...`, alone on its line, so the user is asked.")


def check_write(path: str, text: str) -> None:
    p = path.replace("\\", "/")
    if any(p.endswith(x) for x in PROTECTED):
        block(f"Blocked: {path} guards the sealed test and is changed by the user only.")
    if p.endswith("TEST_DONE"):
        block("Blocked: TEST_DONE locks are written by lab/run_test.py only.")
    if OPEN_TEST.search(text or "") and not any(p.endswith(x) for x in READS_TEST_AFTER_LOCK):
        block("Blocked: no file may pass open_test=True; strategy files pass open_test through from run(), "
              "and only lab/run_test.py sets it.")


def main() -> None:
    payload = json.load(sys.stdin)
    tool = payload.get("tool_name", "")
    ti = payload.get("tool_input", {}) or {}
    if tool == "Bash":
        check_bash(ti.get("command", ""))
    elif tool == "Write":
        check_write(ti.get("file_path", ""), ti.get("content", ""))
    elif tool == "Edit":
        check_write(ti.get("file_path", ""), ti.get("new_string", ""))
    elif tool == "MultiEdit":
        for e in ti.get("edits", []) or []:
            check_write(ti.get("file_path", ""), e.get("new_string", ""))
    elif tool == "NotebookEdit":
        check_write(ti.get("notebook_path", ""), ti.get("new_source", ""))
    sys.exit(0)


if __name__ == "__main__":
    main()
