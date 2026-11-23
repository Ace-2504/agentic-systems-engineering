"""A4 Part 3, both harnesses in one go. Run from this folder on your own computer:

    python run_part3.py

1. Checks the Python packages (installs the course's Ledgerline package from GitHub if it is missing).
2. Our harness: python part3_ours.py (live Gemini, needs GEMINI_API_KEY).
3. Claude's harness: claude -p, headless, with only my MCP server and only explain_hold allowed, from an empty folder so
   Claude Code cannot read tool.py or anything else here. A second turn only if Claude asks which invoice.
4. python part3_claude_summary.py on Claude Code's stream-json.
Everything lands in logs/.
"""
import json
import os
import pathlib
import shutil
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
LOGS = HERE / "logs"
LOGS.mkdir(exist_ok=True)
TURN1 = "Why is Voltway's invoice 4471 on hold, and can we pay it Friday?"
TURN2 = "Voltway Cells, the battery packs."
PKG = "ledgerline-erp[mcp] @ git+https://github.com/RajatDandekar/agents-for-enterprises#subdirectory=ledgerline"


def step(t):
    print(f"\n===== {t} =====", flush=True)


step("1 · packages")
try:
    import fastmcp  # noqa: F401
    import jsonschema
    import ledgerline  # noqa: F401
    import openai  # noqa: F401
    assert hasattr(jsonschema, "Draft202012Validator")
    print("ledgerline, fastmcp, jsonschema, openai: present")
except (ImportError, AssertionError):
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", PKG, "jsonschema>=4.18", "openai"], check=True)
    print("installed; run this script once more")
    sys.exit(0)
if not os.environ.get("GEMINI_API_KEY") and not os.environ.get("GOOGLE_API_KEY"):
    sys.exit("GEMINI_API_KEY is not set in this terminal. Set it, open a new terminal, and run again.")


def find_claude():
    """Claude Code's CLI: --claude <path>, CLAUDE_BIN, PATH, then the usual install folders on Windows, macOS, Linux."""
    if "--claude" in sys.argv:
        return sys.argv[sys.argv.index("--claude") + 1]
    if os.environ.get("CLAUDE_BIN"):
        return os.environ["CLAUDE_BIN"]
    found = shutil.which("claude")
    if found:
        return found
    home = pathlib.Path.home()
    appdata = pathlib.Path(os.environ.get("APPDATA", home / "AppData" / "Roaming"))
    local = pathlib.Path(os.environ.get("LOCALAPPDATA", home / "AppData" / "Local"))
    candidates = [home / ".local" / "bin" / "claude.exe", home / ".local" / "bin" / "claude",
                  appdata / "npm" / "claude.cmd", appdata / "npm" / "claude",
                  home / ".claude" / "local" / "claude.exe", home / ".claude" / "local" / "claude",
                  local / "Programs" / "claude" / "claude.exe", local / "AnthropicClaude" / "claude.exe",
                  home / ".npm-global" / "bin" / "claude", pathlib.Path("/usr/local/bin/claude")]
    for c in candidates:
        if c.exists():
            return str(c)
    for root in (local, appdata):                       # last resort: a shallow search for claude.exe / claude.cmd
        for pat in ("*/claude.exe", "*/*/claude.exe", "*/claude.cmd"):
            for c in root.glob(pat):
                if "claude-desktop" not in str(c).lower() and "anthropicclaude" not in str(c).lower():
                    return str(c)
    return None


claude = find_claude()
print("Claude Code CLI:", claude or "NOT FOUND")
if "--login" in sys.argv:
    if not claude:
        sys.exit("Claude Code's CLI was not found, so there is nothing to log in to.")
    print("Opening Claude Code. Type  /login  , finish signing in, then type  /exit  to come back here.")
    subprocess.run([claude], cwd=LOGS, shell=(os.name == "nt"))
    print("Back. Now run:  python run_part3.py --skip-ours")
    sys.exit(0)

step("2 · our harness (Ask Northbridge's loop, gemini-3.8-flash)")
if "--skip-ours" in sys.argv and (LOGS / "part3_ours.json").exists():
    print("skipped: logs/part3_ours.json is already there")
else:
    r = subprocess.run([sys.executable, str(HERE / "part3_ours.py")], cwd=HERE)
    if r.returncode:
        print("our harness failed; the Claude run continues")

step("3 · Claude's harness (Claude Code, headless)")
if not claude:
    sys.exit("Claude Code's CLI was not found. Find it with:  where claude   (or  Get-Command claude  in PowerShell)\n"
             "then run:  python run_part3.py --claude \"<that path>\" --skip-ours")
v = subprocess.run([claude, "--version"], capture_output=True, text=True, shell=(os.name == "nt"))
print("version:", (v.stdout or v.stderr).strip())
cwd = LOGS / "claude_cwd"                     # empty on purpose: Claude Code sees my MCP server and nothing else
cwd.mkdir(exist_ok=True)
calls_log = LOGS / "part3_claude_calls.jsonl"
if calls_log.exists():
    calls_log.unlink()
config = {"mcpServers": {"northbridge-ap": {"command": sys.executable,
                                            "args": [str(HERE / "serve_explain_hold.py"), "--user", "ECLARKE",
                                                     "--log", str(calls_log)]}}}
cfg = LOGS / "claude_mcp_local.json"
cfg.write_text(json.dumps(config, indent=1))
common = ["--mcp-config", str(cfg), "--strict-mcp-config", "--allowedTools", "mcp__northbridge-ap__explain_hold",
          "--disallowedTools", "Bash,Read,Edit,Write,Glob,Grep,WebFetch,WebSearch,Task,NotebookEdit,TodoWrite",
          "--output-format", "stream-json", "--verbose"]


def claude_turn(prompt, out, cont=False):
    cmd = [claude] + (["-c"] if cont else []) + ["-p", prompt] + common
    with open(out, "w", encoding="utf-8") as f:
        subprocess.run(cmd, cwd=cwd, stdout=f, stderr=subprocess.STDOUT, shell=(os.name == "nt"), timeout=600)
    print("written", out.name)


t1 = LOGS / "claude_turn1.jsonl"
claude_turn(TURN1, t1)
files = [str(t1)]
text = t1.read_text(encoding="utf-8", errors="replace")
if "authentication_failed" in text or "Not logged in" in text:
    sys.exit("Claude Code is not logged in for this terminal. Run  claude  once, type  /login , finish signing in,\n"
             "type  /exit , then run:  python run_part3.py --skip-ours")
if '\\"holds\\"' not in text and '"holds"' not in text:     # it did not get Voltway Cells' holds: answer its question
    t2 = LOGS / "claude_turn2.jsonl"
    claude_turn(TURN2, t2, cont=True)
    files.append(str(t2))

step("4 · Claude Code transcript")
subprocess.run([sys.executable, str(HERE / "part3_claude_summary.py"), *files], cwd=HERE)
print("\nDone. Tell Claude in the chat that run_part3.py has finished.")
