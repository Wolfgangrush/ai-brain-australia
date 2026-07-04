"""AI Brain — Australia · CLI entry point."""

import argparse
import sys
from pathlib import Path

from .update import cmd_update, copy_claude_md_template


def cmd_init(args):
    print(f"\n  Initialising firm in: {args.dir}")
    Path(args.dir).expanduser().resolve().mkdir(parents=True, exist_ok=True)
    copy_claude_md_template(args.dir)
    print("  ✔ Firm initialised. Edit CLAUDE.md with your firm details.")


def cmd_status(args):
    print("  ailawfirm-australia · run `python -m ailawfirm_australia --help` for commands")


# ---------------------------------------------------------------------------
# Terminal-brain front door
# ---------------------------------------------------------------------------
# These four commands turn the brain into a real terminal app — they are the
# `reception · ask · chat · recap` surface that the AI-backed host relies on.


def cmd_ask(args):
    """One-shot: classify → route → render a single query and print it."""
    from ailawfirm_australia.brain.repl import run_ask

    query = " ".join(args.query) if isinstance(args.query, list) else str(args.query or "")
    return run_ask(query.strip())


def cmd_chat(args):
    """Interactive REPL — talk to the brain; each line routes to a specialist."""
    from ailawfirm_australia.brain.repl import run_chat

    return run_chat()


def cmd_reception(args):
    """Boot the brain — greet, verify all 7 specialists, memory, recap."""
    from ailawfirm_australia.brain.reception import run_reception

    return run_reception()


def cmd_recap(args):
    """Show the retrospective-memory recap of recent sessions."""
    from ailawfirm_australia.brain.memory import recap

    print(recap(getattr(args, "n", 5)))
    return 0


def main():
    parser = argparse.ArgumentParser(
        description="AI Brain for Australia Lawyers",
    )
    sub = parser.add_subparsers(dest="command")

    # --- existing surface ----------------------------------------------------
    p_init = sub.add_parser("init", help="Initialise a firm directory")
    p_init.add_argument("dir", help="Directory to initialise as the firm")

    sub.add_parser("status", help="Show firm status")

    p_update = sub.add_parser(
        "update",
        help="Pull the latest firm code, skills, and prompts from upstream (matter data is NEVER touched)",
    )
    p_update.add_argument(
        "--quiet", "-q", action="store_true", help="suppress pip output (errors still print)"
    )

    # --- terminal-brain front door -----------------------------------------
    p_ask = sub.add_parser(
        "ask",
        help="Ask the brain one question — it classifies + routes to the right specialist",
    )
    p_ask.add_argument(
        "query",
        nargs="+",
        help='Your question, e.g. "limitation for a NSW debt matter"',
    )

    sub.add_parser(
        "chat",
        help="Talk to the brain in the terminal — each line routes to a specialist",
    )

    sub.add_parser(
        "reception",
        help="Boot the brain: greet, verify all 7 specialists, turn on memory, show recap",
    )

    p_recap = sub.add_parser(
        "recap",
        help="Show recent-session retrospective memory",
    )
    p_recap.add_argument(
        "-n",
        type=int,
        default=5,
        help="How many recent interactions to show (default: 5)",
    )

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return

    dispatch = {
        "init": cmd_init,
        "status": cmd_status,
        "update": cmd_update,
        "ask": cmd_ask,
        "chat": cmd_chat,
        "reception": cmd_reception,
        "recap": cmd_recap,
    }
    dispatch[args.command](args)


if __name__ == "__main__":
    sys.exit(main() or 0)
