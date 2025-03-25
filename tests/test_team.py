"""Tests for the Team class."""
import pytest
from dynoagent import Team, DynoAgent

def test_team_initialization(basic_team, team_agents):
    """Test that a team is initialized with correct attributes."""
    assert basic_team.name == "test_team"
    assert len(basic_team.agents) == len(team_agents)
    assert "agent2" in basic_team.explicit_dependencies

def test_team_add_agent(basic_team):
    """Test adding a new agent to the team."""
    new_agent = DynoAgent(
        name="agent3",
        role="validator",
        skills=["validation"],
        goal="validate_data"
    )
    basic_team.add_agent(new_agent, dependencies=["agent2"])
    assert len(basic_team.agents) == 3
    assert "agent3" in basic_team.agent_map

def test_team_execute_sequential(basic_team):
    """Test sequential execution of team tasks."""
    context = {"test_data": "sample"}
    results = basic_team.execute_sequential(context)
    assert results is not None
    assert len(results) == len(basic_team.agents)

def test_team_dependency_validation(team_agents):
    """Test that invalid dependencies raise appropriate errors."""
    with pytest.raises(ValueError):
        Team(
            name="invalid_team",
            agents=team_agents,
            explicit_dependencies={
                "non_existent_agent": ["agent1"]  # Invalid dependency
            }
        )

def test_team_circular_dependency_detection(team_agents):
    """Test that circular dependencies are detected."""
    with pytest.raises(ValueError):
        Team(
            name="circular_team",
            agents=team_agents,
            explicit_dependencies={
                "agent1": ["agent2"],
                "agent2": ["agent1"]  # Creates a cycle
            }
        ) 