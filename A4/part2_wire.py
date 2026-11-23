"""A4 Part 2: start serve_explain_hold.py the way Claude Code does (a child process on stdio) and type the JSON-RPC
ourselves. Every line that crosses the pipe is saved to logs/mcp_wire.jsonl and printed in full."""
import json
import os
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
REQUESTS = [
    {"jsonrpc": "2.0", "id": 1, "method": "initialize",
     "params": {"protocolVersion": "2025-06-18", "capabilities": {}, "clientInfo": {"name": "a4-part2", "version": "1.0"}}},
    {"jsonrpc": "2.0", "method": "notifications/initialized"},
    {"jsonrpc": "2.0", "id": 2, "method": "tools/list"},
    {"jsonrpc": "2.0", "id": 3, "method": "tools/call",
     "params": {"name": "explain_hold", "arguments": {"invoice_no": "4471", "supplier": "Voltway Cells"}}},
    {"jsonrpc": "2.0", "id": 4, "method": "tools/call",
     "params": {"name": "explain_hold", "arguments": {"invoice_no": "AP/2026/99999"}}},
]

env = {**os.environ, "FASTMCP_SHOW_CLI_BANNER": "false", "FASTMCP_LOG_LEVEL": "ERROR"}
p = subprocess.Popen([sys.executable, str(HERE / "serve_explain_hold.py"), "--log", str(HERE / "logs" / "part2_calls.jsonl")],
                     stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True, env=env, bufsize=1)
wire = []
try:
    for req in REQUESTS:
        p.stdin.write(json.dumps(req) + "\n")
        p.stdin.flush()
        wire.append({"dir": "->", "msg": req})
        if "id" not in req:
            continue
        while True:
            line = p.stdout.readline()
            if not line:
                raise RuntimeError("the server closed the pipe")
            msg = json.loads(line)
            wire.append({"dir": "<-", "msg": msg})
            if msg.get("id") == req["id"]:
                break
finally:
    p.stdin.close()
    p.wait(10)

with open(HERE / "logs" / "mcp_wire.jsonl", "w") as f:
    for w in wire:
        f.write(json.dumps(w) + "\n")
for w in wire:
    print(w["dir"], json.dumps(w["msg"]))
    print()
