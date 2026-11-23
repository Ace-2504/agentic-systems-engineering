"""A4 Part 3, Claude's harness: turn Claude Code's headless stream-json output into a readable transcript.

    claude -p "<question>" --mcp-config claude_mcp.json --strict-mcp-config ^
        --allowedTools mcp__northbridge-ap__explain_hold --output-format stream-json --verbose > logs/claude_turn1.jsonl
    claude -c -p "<answer>" ... > logs/claude_turn2.jsonl              (only if Claude asked which invoice)
    python part3_claude_summary.py logs/claude_turn1.jsonl [logs/claude_turn2.jsonl]
"""
import json
import sys

summary = {"turns": []}
for path in sys.argv[1:]:
    events = [json.loads(line) for line in open(path, encoding="utf-8-sig") if line.strip().startswith("{")]
    turn = {"file": path, "steps": []}
    for e in events:
        if e.get("type") == "system" and e.get("subtype") == "init":
            turn["model"] = e.get("model")
            turn["mcp_servers"] = e.get("mcp_servers")
            turn["tools_offered"] = len(e.get("tools") or [])
            turn["mcp_tools"] = [t for t in e.get("tools") or [] if t.startswith("mcp__")]
        elif e.get("type") == "assistant":
            for c in e["message"].get("content", []):
                if c.get("type") == "text" and c["text"].strip():
                    turn["steps"].append({"kind": "text", "text": c["text"]})
                elif c.get("type") == "tool_use":
                    turn["steps"].append({"kind": "call", "tool": c["name"], "args": c.get("input")})
        elif e.get("type") == "user":
            content = e.get("message", {}).get("content", [])
            for c in content if isinstance(content, list) else []:
                if c.get("type") == "tool_result":
                    body = c.get("content")
                    if isinstance(body, list):
                        body = " ".join(b.get("text", "") for b in body if isinstance(b, dict))
                    turn["steps"].append({"kind": "result", "is_error": c.get("is_error", False), "text": body})
        elif e.get("type") == "result":
            turn.update({k: e.get(k) for k in ("num_turns", "duration_ms", "total_cost_usd", "usage", "modelUsage",
                                               "result", "is_error", "session_id")})
    summary["turns"].append(turn)
    print(f"=== {path} · model {turn.get('model')} · MCP {turn.get('mcp_servers')} · tools offered {turn.get('tools_offered')}")
    for s in turn["steps"]:
        if s["kind"] == "call":
            print("  CALL  ", s["tool"], json.dumps(s["args"]))
        elif s["kind"] == "result":
            print("  RESULT", "(isError)" if s["is_error"] else "", (s["text"] or "")[:400])
        else:
            print("  TEXT  ", s["text"])
    u = turn.get("usage") or {}
    print(f"  turns {turn.get('num_turns')} · {turn.get('duration_ms')} ms · cost reported ${turn.get('total_cost_usd')}"
          f" · input {u.get('input_tokens')} · cache read {u.get('cache_read_input_tokens')}"
          f" · cache write {u.get('cache_creation_input_tokens')} · output {u.get('output_tokens')}")
with open("logs/part3_claude.json", "w", encoding="utf-8") as f:
    json.dump(summary, f, indent=1)
print("written logs/part3_claude.json")
