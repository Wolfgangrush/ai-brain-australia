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
    print("  ailawfirm-australia · run `ailawfirm-australia --help` for commands")


def main():
    parser = argparse.ArgumentParser(
        description="AI Brain for Australia Lawyers",
    )
    sub = parser.add_subparsers(dest="command")

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

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return

    dispatch = {
        "init": cmd_init,
        "status": cmd_status,
        "update": cmd_update,
    }
    dispatch[args.command](args)


if __name__ == "__main__":
    sys.exit(main() or 0)
