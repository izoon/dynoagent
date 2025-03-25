"""Test configuration and shared fixtures."""

import asyncio
import sys

import pytest

from dynoagent import DynoAgent, Team


@pytest.fixture(scope="session")
def event_loop_policy():
    """Configure the event loop policy for the test session."""
    if sys.platform.startswith("win") and sys.version_info[:2] >= (3, 8):
        # Windows Python >= 3.8 defaults to ProactorEventLoop, which doesn't support some features
        # we need. Force the use of SelectorEventLoop instead.
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    return asyncio.get_event_loop_policy()


@pytest.fixture
def dyno_agent():
    """Create a basic DynoAgent instance for testing."""
    return DynoAgent(
        name="TestAgent",
        role="Tester",
        skills=["Testing"],
        goal="Test functionality",
    )


@pytest.fixture
def team():
    """Create a basic Team instance for testing."""
    agent = DynoAgent(
        name="TestAgent",
        role="Tester",
        skills=["Testing"],
        goal="Test functionality",
    )
    return Team("TestTeam", [agent])


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
            name="agent1",
            role="processor",
            skills=["processing"],
            goal="process_data",
        ),
        DynoAgent(
            name="agent2",
            role="analyzer",
            skills=["analysis"],
            goal="analyze_data",
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
