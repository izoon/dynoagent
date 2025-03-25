"""
Command-line interface for DynoAgent.
"""
import argparse
import sys
from typing import List, Optional

from . import __version__
from .core import DynoAgent


def create_parser() -> argparse.ArgumentParser:
    """Create the command-line argument parser."""
    parser = argparse.ArgumentParser(
        description="DynoAgent - A dynamic role-based agent framework"
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"DynoAgent {__version__}",
        help="Show version number and exit",
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    
    # Create agent command
    create_parser = subparsers.add_parser("create", help="Create a new agent")
    create_parser.add_argument("name", help="Name of the agent")
    create_parser.add_argument("role", help="Role of the agent")
    create_parser.add_argument("--skills", nargs="+", help="Skills for the agent")
    create_parser.add_argument("--goal", help="Goal for the agent")
    
    # Execute task command
    execute_parser = subparsers.add_parser("execute", help="Execute a task")
    execute_parser.add_argument("agent_name", help="Name of the agent to use")
    execute_parser.add_argument("task", help="Task to execute")
    
    return parser


def main(args: Optional[List[str]] = None) -> int:
    """Main entry point for the CLI."""
    if args is None:
        args = sys.argv[1:]
    
    parser = create_parser()
    parsed_args = parser.parse_args(args)
    
    if not parsed_args.command:
        parser.print_help()
        return 1
    
    if parsed_args.command == "create":
        agent = DynoAgent(
            name=parsed_args.name,
            role=parsed_args.role,
            skills=parsed_args.skills or [],
            goal=parsed_args.goal or "default_goal"
        )
        print(f"Created agent: {agent.name}")
        return 0
    
    elif parsed_args.command == "execute":
        # This is a simplified example - in a real implementation,
        # you would need to handle agent persistence and loading
        agent = DynoAgent(
            name=parsed_args.agent_name,
            role="executor",
            skills=[],
            goal="execute_task"
        )
        result = agent.perform_task(parsed_args.task)
        print(f"Task result: {result}")
        return 0
    
    return 1


if __name__ == "__main__":
    sys.exit(main()) 