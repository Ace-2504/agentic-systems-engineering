# MCP.md: `explain_hold` on MCP

## 2.1 Serving it

```
python serve_explain_hold.py                                   # stdio, one JSON-RPC message per line
python serve_explain_hold.py --user ECLARKE --log logs/calls.jsonl
python serve_explain_hold.py --transport http --port 8765      # streamable HTTP at http://127.0.0.1:8765/mcp
```

`serve_explain_hold.py` is the course's own server, `ledgerline.toolbox.mcp.build_toolbox_server`, with three changes the stock command line cannot make:
- a Ledgerline running the `fin_payables` module with my capstone's records (`capstone_seed.py`)
- only my tool, acting for one person (Priya Shah, `PSHAH`, by default)
- `_meta` carrying only the keys my `tool.json` sets. The course's server always adds every key, filling the ones a tool does not set with `null`. Publishing empty fields tells a host nothing, so my server leaves them out.

`python -m ledgerline.toolbox.mcp --tool-dir tools --tools explain_hold` does load the folder. But it starts the purchasing Ledgerline, which has no `ap_*` services, so every call would fail.

## 2.2 The raw wire

`part2_wire.py` starts the server the way Claude Code does, as a child process on stdio, and writes each message itself. Every line that crossed the pipe is below, unedited (also in `logs/mcp_wire.jsonl`).

**1 · initialize, and the reply**

```json
-> {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2025-06-18", "capabilities": {}, "clientInfo": {"name": "a4-part2", "version": "1.0"}}}
```

```json
<- {"jsonrpc": "2.0", "id": 1, "result": {"protocolVersion": "2025-06-18", "capabilities": {"logging": {}, "prompts": {"listChanged": true}, "resources": {"subscribe": false, "listChanged": true}, "tools": {"listChanged": true}}, "serverInfo": {"name": "northbridge-ap", "version": "4.1.8"}, "instructions": "Northbridge Cycles' Ledgerline ERP, as PSHAH. One tool per business activity."}}
```

**2 · notifications/initialized** (a notification: no `id`, no reply)

```json
-> {"jsonrpc": "2.0", "method": "notifications/initialized"}
```

**3 · tools/list, and the reply**

```json
-> {"jsonrpc": "2.0", "id": 2, "method": "tools/list"}
```

```json
{
 "jsonrpc": "2.0",
 "id": 2,
 "result": {
  "tools": [
   {
    "_meta": {
     "ledgerline/category": "Look up",
     "ledgerline/writes": false,
     "ledgerline/services": [
      "ap_inv_list",
      "ap_inv_get",
      "usr_get"
     ],
     "ledgerline/policy": {
      "ledgerline_reply_timeout_s": 30,
      "on_busy_or_lost_reply": "retry the read, at most 2 more times",
      "after_retries": "ok=false, ledgerline_code ERR-SYS-0503 or TIMEOUT, with next_step"
     },
     "fastmcp": {
      "tags": []
     }
    },
    "annotations": {
     "destructiveHint": false,
     "idempotentHint": true,
     "openWorldHint": false,
     "readOnlyHint": true,
     "title": "Explain hold"
    },
    "description": "Why a supplier invoice is on hold: each open hold and what is wrong, who may release it, and the last Friday run that still pays it by the due date. Give the number printed on the invoice (e.g. 4471) or Ledgerline's AP number; if two suppliers match, ask which.",
    "inputSchema": {
     "properties": {
      "invoice_no": {
       "type": "string",
       "description": "the number on the supplier's invoice, e.g. 4471, or Ledgerline's own number, e.g. AP/2026/03390"
      },
      "supplier": {
       "type": "string",
       "description": "part of the supplier's name, e.g. Voltway Cells; needed when two suppliers used the same number"
      }
     },
     "required": [
      "invoice_no"
     ],
     "type": "object"
    },
    "name": "explain_hold",
    "outputSchema": {
     "properties": {
      "ok": {
       "type": "boolean",
       "description": "true when it worked; false comes with error and next_step"
      },
      "supplier": {
       "type": "string",
       "description": "the supplier's name as Ledgerline has it, e.g. Voltway Cells Pvt. Ltd."
      },
      "ap_no": {
       "type": "string",
       "description": "Ledgerline's own number for the invoice, e.g. AP/2026/03390; use it in any later call"
      },
      "status": {
       "type": "string",
       "enum": [
        "on hold",
        "waiting for approval",
        "clear to pay",
        "paid",
        "rejected",
        "cancelled"
       ],
       "description": "the invoice's status in Ledgerline"
      },
      "invoice_no": {
       "type": "string",
       "description": "the number printed on the supplier's invoice, e.g. 4471"
      },
      "amount": {
       "type": "number",
       "description": "rupees including GST"
      },
      "due_date": {
       "type": "string",
       "format": "date",
       "description": "YYYY-MM-DD; Ledgerline works it out from the invoice date and the supplier's payment terms"
      },
      "payment": {
       "type": [
        "object",
        "null"
       ],
       "description": "when the invoice can be paid; null when it is already paid, rejected or cancelled",
       "properties": {
        "last_run": {
         "type": "string",
         "format": "date",
         "description": "the last Friday run on or before the due date (YYYY-MM-DD)"
        },
        "cutoff": {
         "type": "string",
         "format": "date",
         "description": "the Thursday before last_run; every hold must be released and the payment approved by then"
        },
        "this_friday": {
         "type": "string",
         "format": "date",
         "description": "the next Friday run (YYYY-MM-DD)"
        },
        "payable_this_friday": {
         "type": "boolean"
        },
        "why_not": {
         "type": [
          "string",
          "null"
         ],
         "description": "the reason when payable_this_friday is false, e.g. on hold, or early and needs the financial controller"
        }
       },
       "required": [
        "last_run",
        "cutoff",
        "this_friday",
        "payable_this_friday"
       ]
      },
      "holds": {
       "type": "array",
       "description": "every open hold on the invoice, oldest first; empty when the invoice is not on hold",
       "items": {
        "type": "object",
        "properties": {
         "code": {
          "type": "string",
          "enum": [
           "H-PRC",
           "H-QTY",
           "H-GRN",
           "H-DUP"
          ],
          "description": "H-PRC price, H-QTY quantity, H-GRN no goods receipt, H-DUP looks like a duplicate"
         },
         "what_is_wrong": {
          "type": "string",
          "description": "the gap in words, e.g. 18,000 billed, 17,700 accepted"
         },
         "on_hold_since": {
          "type": "string",
          "format": "date",
          "description": "YYYY-MM-DD"
         },
         "may_release": {
          "type": "array",
          "description": "the people allowed to release this hold, from AP policy 4.1",
          "items": {
           "type": "object",
           "properties": {
            "name": {
             "type": "string"
            },
            "role": {
             "type": "string",
             "description": "e.g. stores, financial controller"
            }
           },
           "required": [
            "name",
            "role"
           ]
          }
         }
        },
        "required": [
         "code",
         "what_is_wrong",
         "on_hold_since",
         "may_release"
        ]
       }
      },
      "matches": {
       "type": "array",
       "description": "only when the number matches invoices from more than one supplier; then holds and payment are left out",
       "items": {
        "type": "object",
        "properties": {
         "ap_no": {
          "type": "string"
         },
         "supplier": {
          "type": "string"
         },
         "invoice_date": {
          "type": "string",
          "format": "date",
          "description": "YYYY-MM-DD"
         },
         "amount": {
          "type": "number",
          "description": "rupees including GST"
         },
         "status": {
          "type": "string",
          "enum": [
           "on hold",
           "waiting for approval",
           "clear to pay",
           "paid",
           "rejected",
           "cancelled"
          ]
         }
        },
        "required": [
         "ap_no",
         "supplier",
         "invoice_date",
         "amount",
         "status"
        ]
       }
      },
      "error": {
       "type": "string",
       "description": "what went wrong, only when ok is false"
      },
      "next_step": {
       "type": "string",
       "description": "what to do next: ask which supplier (with matches), or how to recover (with error)"
      },
      "ledgerline_code": {
       "type": [
        "string",
        "null"
       ],
       "description": "Ledgerline's own error code, e.g. ERR-AP-0001 or ERR-SYS-0503; empty when the tool itself refused"
      }
     },
     "required": [
      "ok"
     ],
     "type": "object"
    },
    "title": "Explain hold"
   }
  ]
 }
}
```

**4 · tools/call that works:** Voltway Cells' 4471

```json
-> {"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": "explain_hold", "arguments": {"invoice_no": "4471", "supplier": "Voltway Cells"}}}
```

```json
{
 "jsonrpc": "2.0",
 "id": 3,
 "result": {
  "content": [
   {
    "text": "{\"ok\": true, \"supplier\": \"Voltway Cells Pvt. Ltd.\", \"ap_no\": \"AP/2026/03390\", \"status\": \"on hold\", \"invoice_no\": \"4471\", \"amount\": 28308672.0, \"due_date\": \"2026-11-16\", \"payment\": {\"last_run\": \"2026-11-13\", \"cutoff\": \"2026-11-12\", \"this_friday\": \"2026-10-30\", \"payable_this_friday\": false, \"why_not\": \"on hold; nothing is paid while an invoice is on hold\"}, \"holds\": [{\"code\": \"H-QTY\", \"what_is_wrong\": \"18,000 billed, 17,700 accepted\", \"on_hold_since\": \"2026-10-05\", \"may_release\": [{\"name\": \"Ganesh Pawar\", \"role\": \"stores\"}, {\"name\": \"Vikram Nair\", \"role\": \"financial controller\"}]}, {\"code\": \"H-PRC\", \"what_is_wrong\": \"billed at Rs.1,332.80 each against the order's Rs.1,276.80 (+4.39%)\", \"on_hold_since\": \"2026-10-05\", \"may_release\": [{\"name\": \"Daniel Okafor\", \"role\": \"purchase manager\"}, {\"name\": \"Vikram Nair\", \"role\": \"financial controller\"}]}]}",
    "type": "text"
   }
  ],
  "isError": false,
  "structuredContent": {
   "ok": true,
   "supplier": "Voltway Cells Pvt. Ltd.",
   "ap_no": "AP/2026/03390",
   "status": "on hold",
   "invoice_no": "4471",
   "amount": 28308672.0,
   "due_date": "2026-11-16",
   "payment": {
    "last_run": "2026-11-13",
    "cutoff": "2026-11-12",
    "this_friday": "2026-10-30",
    "payable_this_friday": false,
    "why_not": "on hold; nothing is paid while an invoice is on hold"
   },
   "holds": [
    {
     "code": "H-QTY",
     "what_is_wrong": "18,000 billed, 17,700 accepted",
     "on_hold_since": "2026-10-05",
     "may_release": [
      {
       "name": "Ganesh Pawar",
       "role": "stores"
      },
      {
       "name": "Vikram Nair",
       "role": "financial controller"
      }
     ]
    },
    {
     "code": "H-PRC",
     "what_is_wrong": "billed at Rs.1,332.80 each against the order's Rs.1,276.80 (+4.39%)",
     "on_hold_since": "2026-10-05",
     "may_release": [
      {
       "name": "Daniel Okafor",
       "role": "purchase manager"
      },
      {
       "name": "Vikram Nair",
       "role": "financial controller"
      }
     ]
    }
   ]
  }
 }
}
```

**5 · tools/call with `isError: true`:** an AP number Ledgerline does not have

```json
-> {"jsonrpc": "2.0", "id": 4, "method": "tools/call", "params": {"name": "explain_hold", "arguments": {"invoice_no": "AP/2026/99999"}}}
```

```json
{
 "jsonrpc": "2.0",
 "id": 4,
 "result": {
  "content": [
   {
    "text": "{\"ok\": false, \"error\": \"No invoice AP/2026/99999 in Ledgerline.\", \"next_step\": \"Check the AP number with the user.\", \"ledgerline_code\": \"ERR-AP-0001\"}",
    "type": "text"
   }
  ],
  "isError": true,
  "structuredContent": {
   "ok": false,
   "error": "No invoice AP/2026/99999 in Ledgerline.",
   "next_step": "Check the AP number with the user.",
   "ledgerline_code": "ERR-AP-0001"
  }
 }
}
```

### What to point out in these messages

- **Protocol version.** The client asked for `"protocolVersion": "2025-06-18"`, and the server's reply agreed to the same `"2025-06-18"`. The server also says who it is (`serverInfo.name: "northbridge-ap"`) and what it supports (`capabilities.tools.listChanged: true`).
  - Two small things the wire shows that I did not choose:
    - `serverInfo.version` is `4.1.8`, which is FastMCP's own number, not my tool's.
    - The server also advertises `prompts` and `resources`, which are FastMCP's defaults, though it serves neither.
  - The `version` inside `clientInfo` is required by the MCP spec: every client names itself in `initialize`.
- **`inputSchema`** (in the `tools/list` reply): exactly my `input_schema`. `invoice_no` is a required string, `supplier` an optional string, and both carry the descriptions the model chooses by.
- **`outputSchema`**: exactly my `output_schema`, including the `status` and hold-`code` enums, the `format: date` fields and the nullable `payment`.
- **`annotations`**: `readOnlyHint: true`, `destructiveHint: false`, `idempotentHint: true`, `openWorldHint: false`, plus `title: "Explain hold"`, which the server copies in for older clients.
  - These are hints for the host: Claude sorts the tool as read-only from them. They are not a guarantee. What makes the tool read-only is that `tool.py` calls only read services.
- **`_meta`**: the `tool.json` keys MCP has no field for, namespaced `ledgerline/`:
  - `category` "Look up", `writes` false
  - the three services
  - the retry `policy`
  - (`fastmcp.tags` is FastMCP's own.)
- **Result of call 4:**
  - `content` is one text block holding the result as a JSON string. That text is what most hosts give the model.
  - `structuredContent` is the same result as an object, which a client can check against `outputSchema`.
  - `isError: false`.
- **Result of call 5:** `isError: true`. The server sets it because `tool.py` returned `ok: false`.
  - It is still a normal JSON-RPC `result`, not a JSON-RPC `error`: the protocol worked, and the tool reports a business failure.
  - `structuredContent` carries the full error contract: `error`, `next_step` and Ledgerline's own `ERR-AP-0001`.

Sizes on the wire: the `tools/list` reply is 4,928 bytes, call 4's reply 1,937 bytes (the 854-byte result sent twice, once as text and once structured), and call 5's 436 bytes.

## 2.3 Field by field

| MCP field | Where it comes from in `tool.json` | Does my server send it? |
|---|---|---|
| `name` | `name` | yes: `explain_hold` |
| `title` | `title` | yes, and again as `annotations.title` |
| `description` | `description` | yes, word for word |
| `inputSchema` | `input_schema` | yes |
| `outputSchema` | `output_schema` | yes |
| `annotations.readOnlyHint` / `destructiveHint` / `idempotentHint` / `openWorldHint` | `annotations` | yes: true / false / true / false |
| `_meta["ledgerline/category"]` | `category` | yes: "Look up" |
| `_meta["ledgerline/writes"]` | `writes` | yes: false |
| `_meta["ledgerline/services"]` | `services` | yes: `ap_inv_list`, `ap_inv_get`, `usr_get` |
| `_meta["ledgerline/policy"]` | `policy` | yes |
| any other `_meta["ledgerline/…"]` key | a key my `tool.json` does not set | **no**: left out rather than sent as `null` |
| (none) | `example` | **no**: MCP has no field for an example, so the model never sees it |
| `content[0].text` | what `run()` returns, as JSON text | yes, on every call |
| `structuredContent` | what `run()` returns, as an object | yes, on every call |
| `isError` | `ok: false` in what `run()` returns | yes: false on call 4, true on call 5 |

## How to reproduce

```
python part2_wire.py        # prints every message and writes logs/mcp_wire.jsonl
```
