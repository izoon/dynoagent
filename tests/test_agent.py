"""Tests for the DynoAgent class."""

import pytest

from dynoagent import DynoAgent


def test_agent_initialization(basic_agent):
    """Test that an agent is initialized with correct attributes."""
    assert basic_agent.name == "test_agent"
    assert basic_agent.role == "tester"
    assert "testing" in basic_agent.skills
    assert basic_agent.goal == "run_tests"


def test_agent_perform_task(basic_agent):
    """Test that an agent can perform a basic task."""
    task = "Run a simple test"
    result = basic_agent.perform_task(task)
    assert result is not None


def test_agent_invalid_initialization():
    """Test that agent initialization fails with invalid parameters."""
    with pytest.raises(ValueError):
        DynoAgent(
            name="",  # Empty name should raise error
            role="tester",
            skills=["testing"],
            goal="test",
        )


def test_agent_add_skill(basic_agent):
    """Test adding a new skill to an agent."""
    new_skill = "new_test_skill"
    basic_agent.add_skill(new_skill)
    assert new_skill in basic_agent.skills


def test_agent_update_goal(basic_agent):
    """Test updating an agent's goal."""
    new_goal = "new_test_goal"
    basic_agent.update_goal(new_goal)
    assert basic_agent.goal == new_goal
