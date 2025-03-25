import pytest
from dynoagent.core import DynoAgent
from dynoagent.team import Team

# DynoAgent Edge Cases
def test_agent_empty_initialization():
    """Test initialization with empty values."""
    with pytest.raises(ValueError):
        DynoAgent("", "role", ["skill"], "goal")  # Empty name
    with pytest.raises(ValueError):
        DynoAgent("name", "", ["skill"], "goal")  # Empty role
    with pytest.raises(ValueError):
        DynoAgent("name", "role", "not_a_list", "goal")  # Invalid skills type
    with pytest.raises(ValueError):
        DynoAgent("name", "role", ["skill"], "")  # Empty goal

def test_agent_duplicate_skills():
    """Test adding duplicate skills."""
    agent = DynoAgent("name", "role", ["skill1"], "goal")
    result1 = agent.add_skill("skill2")
    result2 = agent.add_skill("skill2")  # Duplicate
    assert "skill2" in agent.skills
    assert agent.skills.count("skill2") == 1
    assert result1 == "Added skill: skill2"
    assert result2 == "Added skill: skill2"

def test_agent_invalid_goal_update():
    """Test updating goal with invalid values."""
    agent = DynoAgent("name", "role", ["skill"], "goal")
    with pytest.raises(ValueError):
        agent.update_goal("")
    with pytest.raises(ValueError):
        agent.update_goal(None)

def test_agent_tool_edge_cases():
    """Test tool registration and usage edge cases."""
    agent = DynoAgent("name", "role", ["skill"], "goal")
    
    # Test invalid tool registration
    with pytest.raises(ValueError):
        agent.register_tool("", lambda x: x)
    
    # Test unregistering non-existent tool
    result = agent.unregister_tool("nonexistent")
    assert result == "Tool nonexistent not found"
    
    # Test using non-existent tool
    result = agent.use_tool("nonexistent")
    assert "Tool nonexistent not found" in result

def test_agent_learning_edge_cases():
    """Test learning-related edge cases."""
    agent = DynoAgent("name", "role", ["skill"], "goal", enable_learning=True)
    
    # Test learning threshold with no data
    agent.optimize_workflow()  # Should not raise error
    
    # Test empty feedback calculations
    assert agent.calculate_error_margin() is None
    assert agent.average_input_quality() is None

def test_agent_custom_metrics_edge_cases():
    """Test custom metrics edge cases."""
    agent = DynoAgent("name", "role", ["skill"], "goal")
    
    # Test invalid metric function
    with pytest.raises(TypeError):
        agent.add_custom_metric("invalid", "not_a_function")
    
    # Test evaluating metrics with no custom metrics
    result = agent.evaluate_custom_metrics()
    assert result == {}

# Team Edge Cases
def test_team_empty_initialization():
    """Test team initialization with empty values."""
    with pytest.raises(ValueError):
        Team("")
    
    # Test empty team creation
    team = Team("EmptyTeam")
    assert len(team.agents) == 0
    assert len(team.execution_plan) == 0

def test_team_invalid_dependencies():
    """Test team with invalid dependencies."""
    agent1 = DynoAgent("Agent1", "role", ["skill"], "goal")
    agent2 = DynoAgent("Agent2", "role", ["skill"], "goal")
    
    # Test adding agent with non-existent dependency
    team = Team("TestTeam", [agent1])
    with pytest.raises(ValueError):
        team.add_agent(agent2, dependencies=["NonExistentAgent"])
    
    # Test circular dependencies
    team = Team("TestTeam", [agent1, agent2])
    with pytest.raises(ValueError):
        team.explicit_dependencies = {
            "Agent1": ["Agent2"],
            "Agent2": ["Agent1"]
        }
        team._add_explicit_dependencies()
        team._create_execution_plan()

def test_team_execution_edge_cases():
    """Test team execution edge cases."""
    # Test empty team execution
    team = Team("EmptyTeam")
    assert team.execute_sequential() == {}
    
    # Test team with single agent
    agent = DynoAgent("SingleAgent", "role", ["skill"], "goal")
    team = Team("SingleAgentTeam", [agent])
    result = team.execute_sequential()
    assert len(result) == 1
    assert "SingleAgent" in result

def test_team_visualization_edge_cases():
    """Test team visualization edge cases."""
    team = Team("EmptyTeam")
    # Should not raise error for empty graph
    team.visualize_dependencies() 