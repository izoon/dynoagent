"""
Tests for DynoAgentWithTools class.
"""

import pytest
from dynoagent.dyno_agent_with_tools import DynoAgentWithTools

def test_initialization():
    """Test DynoAgentWithTools initialization."""
    # Test basic initialization
    agent = DynoAgentWithTools(
        name="TestAgent",
        role="Tester",
        skills=["Testing"],
        goal="Test initialization"
    )
    assert agent.name == "TestAgent"
    assert agent.role == "Tester"
    assert agent.skills == ["Testing"]
    assert agent.goal == "Test initialization"
    assert agent.llm_provider is None
    assert agent.temperature == 0.7
    assert agent.max_tokens == 1500

    # Test initialization with custom parameters
    agent = DynoAgentWithTools(
        name="CustomAgent",
        role="CustomRole",
        skills=["CustomSkill"],
        goal="Custom goal",
        llm_provider="test_provider",
        temperature=0.5,
        max_tokens=2000
    )
    assert agent.llm_provider == "test_provider"
    assert agent.temperature == 0.5
    assert agent.max_tokens == 2000

def test_perform_task():
    """Test task performance with context."""
    agent = DynoAgentWithTools(
        name="TaskAgent",
        role="TaskExecutor",
        skills=["TaskExecution"],
        goal="Execute tasks"
    )
    
    # Test task execution with context
    result = agent.perform_task("Test task", {"context": "test"})
    assert isinstance(result, dict)
    assert "task" in result
    assert "context" in result
    assert "result" in result
    assert "metrics" in result

def test_data_operations():
    """Test data loading and indexing operations."""
    agent = DynoAgentWithTools(
        name="DataAgent",
        role="DataHandler",
        skills=["DataProcessing"],
        goal="Handle data"
    )

    # Test load_data
    result = agent.load_data("test_type", "test_data")
    assert isinstance(result, list)
    assert len(result) == 0

    # Test index_documents
    agent.index_documents([])  # Should not raise error

    # Test save_index
    agent.save_index()  # Should not raise error

    # Test load_index
    agent.load_index()  # Should not raise error

    # Test query_index
    result = agent.query_index("test query")
    assert isinstance(result, str)
    assert "Query result for: test query" in result

    # Test get_document_summaries
    summaries = agent.get_document_summaries()
    assert isinstance(summaries, list)
    assert len(summaries) == 0

def test_register_data_tools():
    """Test data tool registration."""
    agent = DynoAgentWithTools(
        name="ToolAgent",
        role="ToolHandler",
        skills=["ToolManagement"],
        goal="Manage tools"
    )

    # Test _register_data_tools
    agent._register_data_tools()  # Should not raise error

def test_inheritance():
    """Test that DynoAgentWithTools properly inherits from DynoAgent."""
    agent = DynoAgentWithTools(
        name="InheritAgent",
        role="InheritRole",
        skills=["InheritSkill"],
        goal="Test inheritance"
    )

    # Test inherited methods
    agent.add_skill("NewSkill")
    assert "NewSkill" in agent.skills

    agent.update_goal("New goal")
    assert agent.goal == "New goal"

    # Test tool registration (inherited)
    def dummy_tool(x): return x
    agent.register_tool("dummy", dummy_tool)
    assert "dummy" in agent.tools_dataloaders

def test_edge_cases():
    """Test edge cases and error handling."""
    # Test initialization with invalid parameters
    with pytest.raises(ValueError):
        DynoAgentWithTools("", "role", ["skill"], "goal")  # Empty name

    with pytest.raises(ValueError):
        DynoAgentWithTools("name", "", ["skill"], "goal")  # Empty role

    with pytest.raises(ValueError):
        DynoAgentWithTools("name", "role", "not_a_list", "goal")  # Invalid skills type

    with pytest.raises(ValueError):
        DynoAgentWithTools("name", "role", ["skill"], "")  # Empty goal

    # Test invalid temperature
    with pytest.raises(ValueError):
        DynoAgentWithTools(
            name="name",
            role="role",
            skills=["skill"],
            goal="goal",
            temperature=-1  # Invalid temperature
        )

    # Test invalid max_tokens
    with pytest.raises(ValueError):
        DynoAgentWithTools(
            name="name",
            role="role",
            skills=["skill"],
            goal="goal",
            max_tokens=-1  # Invalid max_tokens
        ) 