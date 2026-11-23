"""One place that builds the A4 sandbox: the course kit's fin_payables Ledgerline, my capstone's records, my tool.

    from a4_setup import sandbox
    erp, tb = sandbox()                 # Ledgerline as Priya Shah (PSHAH, accounts payable), explain_hold loaded

Used by the tests, the MCP server (serve_explain_hold.py) and the harness run (part3_ours.py).
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from ledgerline.erp.engine import ERP                     # noqa: E402
from ledgerline.toolbox import Toolbox                    # noqa: E402
from ledgerline.course.l4 import add_tool_folder          # noqa: E402
from capstone_seed import apply_capstone                  # noqa: E402

TOOL = "explain_hold"
USER = "PSHAH"
TOOL_DIR = HERE / "tools" / TOOL


def load_tool() -> str:
    return add_tool_folder(TOOL_DIR)


def new_erp(faults=None) -> ERP:
    erp = ERP(modules=["fin_payables"], faults=faults)
    apply_capstone(erp)
    return erp


def sandbox(user: str = USER, faults=None):
    name = load_tool()
    erp = new_erp(faults)
    return erp, Toolbox(erp, user, names=[name])
