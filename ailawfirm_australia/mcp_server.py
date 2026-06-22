"""AI Brain — Australia MCP Server.

Wires the 3 Australia-specific MCP tools:
  - australia_court_lookup
  - australia_citation_validator
  - australia_calendar_sync
"""

import json
import logging
import sys

from .mcp_tools.australia_calendar_sync import sync_calendar_event
from .mcp_tools.australia_citation_validator import validate_citation
from .mcp_tools.australia_court_lookup import lookup_court

logging.basicConfig(level=logging.INFO, format="%(message)s", stream=sys.stderr)
logger = logging.getLogger("ailawfirm_australia_mcp")

TOOLS = {
    "australia_court_lookup": {
        "description": (
            "Look up an Australian court by name, code, or jurisdiction filter. "
            "Returns court details: name, level, jurisdiction, e-filing portal URL, "
            "address pattern, website URL. Covers Federal courts (HCA, FCA, FCFCOA, ART) "
            "and state courts (Supreme, District/County, Local/Magistrates). "
            "ART = Administrative Review Tribunal (post-October 2024 transition from AAT)."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "court_name": {"type": "string", "description": "Full or partial court name"},
                "court_code": {"type": "string", "description": "Court code e.g. HCA, FCA, NSWSC"},
                "jurisdiction": {
                    "type": "string",
                    "description": "Filter by jurisdiction: federal, NSW, VIC, QLD, WA, SA, TAS, ACT, NT",
                },
            },
        },
        "handler": lookup_court,
    },
    "australia_citation_validator": {
        "description": (
            "Validate and parse Australian legal citations in AGLC4 format. "
            "Handles medium-neutral citations (e.g. [2024] FCAFC 100) and reported "
            "citations (e.g. (2023) 97 ALJR 100, [2023] HCA 12, (2023) 271 CLR 1). "
            "Returns parsed components: party names, year, volume, reporter, page, "
            "jurisdiction tag, validity flag, and canonical form."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "citation": {
                    "type": "string",
                    "description": "The citation string to validate in AGLC4 format",
                },
            },
            "required": ["citation"],
        },
        "handler": validate_citation,
    },
    "australia_calendar_sync": {
        "description": (
            "Create an ICS calendar event for an Australian legal matter. "
            "Supports multiple Australian timezones (Sydney, Melbourne, Brisbane, "
            "Perth, Adelaide, Hobart, Darwin, ACT). DST-aware where applicable "
            "(Python 3.10+ zoneinfo). entity-aliasing summary in event title, full detail in body. "
            "Publishes .ics file to ~/.ailawfirm-australia/calendars/ by default."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "title": {"type": "string", "description": "Event summary (alias-safe)"},
                "description": {"type": "string", "description": "Full event description"},
                "start_time": {
                    "type": "string",
                    "description": "Start time ISO 8601 (YYYY-MM-DDTHH:MM)",
                },
                "end_time": {
                    "type": "string",
                    "description": "End time ISO 8601 (YYYY-MM-DDTHH:MM)",
                },
                "timezone": {
                    "type": "string",
                    "description": "Timezone (default Australia/Sydney). Supported: Australia/Sydney, Australia/Melbourne, Australia/Brisbane, Australia/Perth, Australia/Adelaide, Australia/Hobart, Australia/Darwin, Australia/ACT",
                },
                "output_path": {
                    "type": "string",
                    "description": "Output .ics file path (optional)",
                },
            },
            "required": ["title", "start_time", "end_time"],
        },
        "handler": sync_calendar_event,
    },
}


def handle_request(request):
    method = request.get("method", "")
    params = request.get("params", {})
    req_id = request.get("id")

    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "ailawfirm-australia", "version": "0.1.0"},
            },
        }
    elif method == "notifications/initialized":
        return None
    elif method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {"name": n, "description": t["description"], "inputSchema": t["input_schema"]}
                    for n, t in TOOLS.items()
                ]
            },
        }
    elif method == "tools/call":
        tool_name = params.get("name")
        tool_args = params.get("arguments", {})
        if tool_name not in TOOLS:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {"code": -32601, "message": f"Unknown tool: {tool_name}"},
            }
        try:
            result = TOOLS[tool_name]["handler"](**tool_args)
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {"content": [{"type": "text", "text": json.dumps(result, indent=2)}]},
            }
        except Exception as e:
            logger.error(f"Tool error in {tool_name}: {e}")
            return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32000, "message": str(e)}}

    return {
        "jsonrpc": "2.0",
        "id": req_id,
        "error": {"code": -32601, "message": f"Unknown method: {method}"},
    }


def main():
    logger.info("AI Brain — Australia MCP Server starting...")
    while True:
        try:
            line = sys.stdin.readline()
            if not line:
                break
            line = line.strip()
            if not line:
                continue
            request = json.loads(line)
            response = handle_request(request)
            if response is not None:
                sys.stdout.write(json.dumps(response) + "\n")
                sys.stdout.flush()
        except KeyboardInterrupt:
            break
        except Exception as e:
            logger.error(f"Server error: {e}")


if __name__ == "__main__":
    main()
