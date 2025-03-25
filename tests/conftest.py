"""Test configuration and shared fixtures."""

import pytest

from dynoagent import DynoAgent, Team


@pytest.fixture
def basic_agent():
    """Create a basic agent for testing."""
    return DynoAgent(
        name="test_agent",
        role="tester",
        skills=["testing", "validation"],
        goal="run_tests",
    )


@pytest.fixture
def team_agents():
    """Create a list of agents for team testing."""
    agents = [
        DynoAgent(
            name="agent1", role="processor", skills=["processing"], goal="process_data"
        ),
        DynoAgent(
            name="agent2", role="analyzer", skills=["analysis"], goal="analyze_data"
        ),
    ]
    return agents


@pytest.fixture
def basic_team(team_agents):
    """Create a basic team for testing."""
    return Team(
        name="test_team",
        agents=team_agents,
        explicit_dependencies={"agent2": ["agent1"]},
    )
