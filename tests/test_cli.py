"""
Tests for DynoAgent CLI functionality.
"""

import pytest
import argparse
from dynoagent.cli import create_parser, main
from dynoagent import __version__

def test_create_parser():
    """Test parser creation and basic structure."""
    parser = create_parser()
    
    # Test parser description
    assert "DynoAgent" in parser.description
    
    # Test available commands
    subparsers_actions = [
        action for action in parser._actions 
        if isinstance(action, argparse._SubParsersAction)
    ]
    assert len(subparsers_actions) == 1
    subparser = subparsers_actions[0]
    
    # Check that create and execute commands exist
    commands = subparser.choices.keys()
    assert "create" in commands
    assert "execute" in commands
    
    # Test version argument
    with pytest.raises(SystemExit) as exc_info:
        parser.parse_args(["--version"])
    assert exc_info.value.code == 0

def test_create_command():
    """Test agent creation command."""
    # Test basic creation
    result = main(["create", "test_agent", "test_role"])
    assert result == 0
    
    # Test creation with skills
    result = main([
        "create",
        "test_agent",
        "test_role",
        "--skills",
        "skill1",
        "skill2"
    ])
    assert result == 0
    
    # Test creation with goal
    result = main([
        "create",
        "test_agent",
        "test_role",
        "--goal",
        "test goal"
    ])
    assert result == 0
    
    # Test creation with skills and goal
    result = main([
        "create",
        "test_agent",
        "test_role",
        "--skills",
        "skill1",
        "skill2",
        "--goal",
        "test goal"
    ])
    assert result == 0

def test_execute_command():
    """Test task execution command."""
    # Test basic execution
    result = main([
        "execute",
        "test_agent",
        "test task"
    ])
    assert result == 0

def test_help_display():
    """Test help display functionality."""
    # Test main help
    with pytest.raises(SystemExit) as exc_info:
        main(["--help"])
    assert exc_info.value.code == 0
    
    # Test create command help
    with pytest.raises(SystemExit) as exc_info:
        main(["create", "--help"])
    assert exc_info.value.code == 0
    
    # Test execute command help
    with pytest.raises(SystemExit) as exc_info:
        main(["execute", "--help"])
    assert exc_info.value.code == 0

def test_error_handling():
    """Test error handling in CLI."""
    # Test no command
    result = main([])
    assert result == 1
    
    # Test invalid command
    with pytest.raises(SystemExit):
        main(["invalid_command"])
    
    # Test missing required arguments for create
    with pytest.raises(SystemExit):
        main(["create"])
    
    # Test missing required arguments for execute
    with pytest.raises(SystemExit):
        main(["execute"])

def test_version_command():
    """Test version display."""
    parser = create_parser()
    
    # Capture version string
    with pytest.raises(SystemExit) as exc_info:
        parser.parse_args(["--version"])
    assert exc_info.value.code == 0

def test_command_validation():
    """Test command validation and processing."""
    # Test create command validation
    with pytest.raises(SystemExit):
        main(["create"])  # Missing required args
    
    with pytest.raises(SystemExit):
        main(["create", "name"])  # Missing role
    
    # Test execute command validation
    with pytest.raises(SystemExit):
        main(["execute"])  # Missing required args
    
    with pytest.raises(SystemExit):
        main(["execute", "agent_name"])  # Missing task

@pytest.mark.parametrize("args,expected_code", [
    (["create", "test_agent", "test_role"], 0),
    (["execute", "test_agent", "test_task"], 0),
    ([], 1),
    (["--help"], 0),
    (["create", "--help"], 0),
    (["execute", "--help"], 0),
])
def test_main_return_codes(args, expected_code):
    """Test return codes for various CLI commands."""
    if "--help" in args:
        with pytest.raises(SystemExit) as exc_info:
            main(args)
        assert exc_info.value.code == expected_code
    else:
        result = main(args)
        assert result == expected_code 