"""A4 Part 2: serve explain_hold over MCP, bound to Priya Shah's Ledgerline session.

    python serve_explain_hold.py                       # stdio: Claude Code / Claude Desktop start it as a child process
    python serve_explain_hold.py --log logs/calls.jsonl  # also log every call and the Ledgerline services it ran
    python serve_explain_hold.py --transport http --port 8765   # streamable HTTP at http://127.0.0.1:8765/mcp
    python serve_explain_hold.py --busy usr_get        # test only: Ledgerline answers "busy" to every usr_get

It is the course's own server (ledgerline.toolbox.mcp.build_toolbox_server), with three changes the stock command line
cannot make: Ledgerline runs the fin_payables module with my capstone's records (capstone_seed.py), only my tool
is listed, and _meta carries only the keys my tool.json sets (no empty fields).
"""
import argparse
import os

os.environ.setdefault("FASTMCP_SHOW_CLI_BANNER", "false")
os.environ.setdefault("FASTMCP_LOG_LEVEL", "ERROR")

from a4_setup import USER, load_tool, new_erp                 # noqa: E402
from ledgerline.toolbox import mcp as course_mcp              # noqa: E402
from ledgerline.toolbox.mcp import build_toolbox_server        # noqa: E402

_course_definition = course_mcp.mcp_definition


def definition_without_empty_meta(spec: dict) -> dict:
    """The course's tool.json -> MCP definition, minus any _meta key my tool.json does not set (no empty fields)."""
    d = _course_definition(spec)
    d["_meta"] = {k: v for k, v in d["_meta"].items() if v is not None}
    return d


course_mcp.mcp_definition = definition_without_empty_meta      # build_toolbox_server uses it for tools/list

ap = argparse.ArgumentParser()
ap.add_argument("--user", default=USER)
ap.add_argument("--transport", default="stdio", choices=["stdio", "http"])
ap.add_argument("--port", type=int, default=8765)
ap.add_argument("--log", default="")
ap.add_argument("--busy", default="", help="test only: comma-separated services that answer 'busy' for the whole run")
a = ap.parse_args()
busy = {svc.strip(): {"mode": "error_before", "times": 10**9} for svc in a.busy.split(",") if svc.strip()}

name = load_tool()
server = build_toolbox_server(new_erp(busy or None), a.user, names=[name], name="northbridge-ap", log=a.log or None)
if a.transport == "http":
    server.run(transport="http", host="127.0.0.1", port=a.port)
else:
    server.run()
