"""
Tests for DynoAgent examples.
These tests verify that the example files work as expected and demonstrate proper usage.
"""

import pytest
import asyncio
from dynoagent import DynoAgent, Team
from dynoagent.task_complexity import TaskComplexityAnalyzer

def test_sequential_example():
    """Test the sequential execution example."""
    # Create agents with specific roles and skills
    data_collector = DynoAgent(
        name="DataCollector",
        role="Collector",
        skills=["Web Scraping", "API Integration"],
        goal="Collect raw data from various sources"
    )

    data_processor = DynoAgent(
        name="DataProcessor",
        role="Processor",
        skills=["Data Cleaning", "Feature Engineering"],
        goal="Process and clean raw data"
    )

    data_analyzer = DynoAgent(
        name="DataAnalyzer",
        role="Analyzer",
        skills=["Statistical Analysis", "Pattern Recognition"],
        goal="Analyze processed data and generate insights"
    )

    report_generator = DynoAgent(
        name="ReportGenerator",
        role="Reporter",
        skills=["Report Writing", "Data Visualization"],
        goal="Generate comprehensive reports from analysis"
    )

    # Create a team with sequential dependencies
    analytics_team = Team("AnalyticsTeam", [data_collector])

    # Add agents with explicit dependencies
    analytics_team.add_agent(data_processor, dependencies=["DataCollector"])
    analytics_team.add_agent(data_analyzer, dependencies=["DataProcessor"])
    analytics_team.add_agent(report_generator, dependencies=["DataAnalyzer"])

    # Verify execution plan is correct
    assert len(analytics_team.execution_plan) == 4  # 4 levels
    assert analytics_team.execution_plan[0] == ["DataCollector"]
    assert analytics_team.execution_plan[1] == ["DataProcessor"]
    assert analytics_team.execution_plan[2] == ["DataAnalyzer"]
    assert analytics_team.execution_plan[3] == ["ReportGenerator"]

    # Execute and verify results
    results = analytics_team.execute_sequential()
    assert len(results) == 4  # All agents should have results
    assert all(agent_name in results for agent_name in [
        "DataCollector", "DataProcessor", "DataAnalyzer", "ReportGenerator"
    ])

@pytest.mark.asyncio
async def test_parallel_example():
    """Test the parallel execution example."""
    # Create agents for independent data processing tasks
    image_processor = DynoAgent(
        name="ImageProcessor",
        role="Processor",
        skills=["Image Recognition", "Feature Extraction"],
        goal="Process and analyze image data"
    )

    text_processor = DynoAgent(
        name="TextProcessor",
        role="Processor",
        skills=["NLP", "Text Analysis"],
        goal="Process and analyze text data"
    )

    audio_processor = DynoAgent(
        name="AudioProcessor",
        role="Processor",
        skills=["Audio Analysis", "Speech Recognition"],
        goal="Process and analyze audio data"
    )

    data_aggregator = DynoAgent(
        name="DataAggregator",
        role="Aggregator",
        skills=["Data Integration", "Multi-modal Fusion"],
        goal="Aggregate results from all processors"
    )

    # Create a team with parallel processing capabilities
    processing_team = Team("MultiModalProcessingTeam", [
        image_processor,
        text_processor,
        audio_processor
    ])

    # Add aggregator that depends on all processors
    processing_team.add_agent(
        data_aggregator,
        dependencies=["ImageProcessor", "TextProcessor", "AudioProcessor"]
    )

    # Verify execution plan is correct
    assert len(processing_team.execution_plan) == 2  # 2 levels
    assert set(processing_team.execution_plan[0]) == {
        "ImageProcessor", "TextProcessor", "AudioProcessor"
    }
    assert processing_team.execution_plan[1] == ["DataAggregator"]

    # Execute and verify results
    results = await processing_team.execute_parallel()
    assert len(results) == 4  # All agents should have results
    assert all(agent_name in results for agent_name in [
        "ImageProcessor", "TextProcessor", "AudioProcessor", "DataAggregator"
    ])

def test_dynamic_example():
    """Test the dynamic execution example."""
    # Create agents for a complex data pipeline
    data_ingestion = DynoAgent(
        name="DataIngestion",
        role="Ingester",
        skills=["Data Loading", "Schema Validation"],
        goal="Ingest and validate raw data"
    )

    feature_extraction = DynoAgent(
        name="FeatureExtraction",
        role="Extractor",
        skills=["Feature Engineering", "Dimensionality Reduction"],
        goal="Extract relevant features from data"
    )

    model_training = DynoAgent(
        name="ModelTraining",
        role="Trainer",
        skills=["Model Selection", "Hyperparameter Tuning"],
        goal="Train and optimize ML models"
    )

    model_evaluation = DynoAgent(
        name="ModelEvaluation",
        role="Evaluator",
        skills=["Performance Metrics", "Cross Validation"],
        goal="Evaluate model performance"
    )

    error_analysis = DynoAgent(
        name="ErrorAnalysis",
        role="Analyzer",
        skills=["Error Detection", "Bias Analysis"],
        goal="Analyze model errors and biases"
    )

    model_deployment = DynoAgent(
        name="ModelDeployment",
        role="Deployer",
        skills=["Model Serving", "API Integration"],
        goal="Deploy models to production"
    )

    monitoring = DynoAgent(
        name="Monitoring",
        role="Monitor",
        skills=["Performance Monitoring", "Drift Detection"],
        goal="Monitor model performance and data drift"
    )

    # Create a team with complex dependencies
    ml_team = Team("MLOpsTeam", [data_ingestion])

    # Add agents with complex dependencies
    ml_team.add_agent(feature_extraction, dependencies=["DataIngestion"])
    ml_team.add_agent(model_training, dependencies=["FeatureExtraction"])
    ml_team.add_agent(model_evaluation, dependencies=["ModelTraining"])
    ml_team.add_agent(error_analysis, dependencies=["ModelEvaluation"])
    ml_team.add_agent(model_deployment, dependencies=["ModelEvaluation", "ErrorAnalysis"])
    ml_team.add_agent(monitoring, dependencies=["ModelDeployment"])

    # Verify execution plan is correct
    assert len(ml_team.execution_plan) == 7  # 7 levels
    assert ml_team.execution_plan[0] == ["DataIngestion"]
    assert ml_team.execution_plan[1] == ["FeatureExtraction"]
    assert ml_team.execution_plan[2] == ["ModelTraining"]
    assert ml_team.execution_plan[3] == ["ModelEvaluation"]
    assert ml_team.execution_plan[4] == ["ErrorAnalysis"]
    assert ml_team.execution_plan[5] == ["ModelDeployment"]
    assert ml_team.execution_plan[6] == ["Monitoring"]

    # Execute and verify results
    results = ml_team.execute_optimal()
    assert len(results) == 7  # All agents should have results
    assert all(agent_name in results for agent_name in [
        "DataIngestion", "FeatureExtraction", "ModelTraining", "ModelEvaluation",
        "ErrorAnalysis", "ModelDeployment", "Monitoring"
    ])

def test_example_error_handling():
    """Test error handling in examples."""
    # Test circular dependency
    agent1 = DynoAgent("Agent1", "Role1", ["Skill1"], "Goal1")
    agent2 = DynoAgent("Agent2", "Role2", ["Skill2"], "Goal2")
    
    team = Team("TestTeam", [agent1, agent2])
    
    # Try to create circular dependency
    with pytest.raises(ValueError):
        team.explicit_dependencies = {
            "Agent1": ["Agent2"],
            "Agent2": ["Agent1"]
        }
        team._add_explicit_dependencies()
        team._create_execution_plan()

    # Test non-existent dependency
    team = Team("TestTeam", [agent1])
    with pytest.raises(ValueError):
        team.add_agent(agent2, dependencies=["NonExistentAgent"])

    # Test empty team
    team = Team("EmptyTeam")
    results = team.execute_sequential()
    assert results == {}

def test_agent_core_functionality():
    """Test core DynoAgent functionality."""
    agent = DynoAgent(
        name="TestAgent",
        role="Tester",
        skills=["Testing", "Debugging"],
        goal="Test core functionality",
        enable_learning=True
    )

    # Test skill management
    agent.add_skill("New Skill")
    assert "New Skill" in agent.skills
    
    # Test goal updates
    agent.update_goal("Updated goal")
    assert agent.goal == "Updated goal"
    
    # Test tool registration
    def dummy_tool(x): return x
    agent.register_tool("dummy", dummy_tool)
    assert "dummy" in agent.tools_dataloaders
    
    # Test tool unregistration
    agent.unregister_tool("dummy")
    assert "dummy" not in agent.tools_dataloaders
    
    # Test tool usage
    agent.register_tool("dummy", dummy_tool)
    result = agent.use_tool("dummy", "test")
    assert result == "test"
    
    # Test learning and optimization
    agent.perform_task("Test task", {"input": "test input"})
    agent.optimize_workflow()  # Should not raise error
    
    # Test metrics
    error_margin = agent.calculate_error_margin()
    assert isinstance(error_margin, (float, type(None)))
    
    quality = agent.average_input_quality()
    assert isinstance(quality, (float, type(None)))

def test_task_complexity():
    """Test TaskComplexityAnalyzer functionality."""
    analyzer = TaskComplexityAnalyzer()
    
    # Test basic task analysis
    task = "Process and analyze large dataset"
    complexity = analyzer.analyze_complexity(task)
    assert isinstance(complexity, str)
    assert complexity in ["simple", "medium", "complex", "creative"]
    
    # Test with role
    complexity_with_role = analyzer.analyze_complexity(task, role="analyst")
    assert isinstance(complexity_with_role, str)
    assert complexity_with_role in ["simple", "medium", "complex", "creative"]
    
    # Test token estimation
    tokens = analyzer.estimate_token_needs(complexity)
    assert isinstance(tokens, int)
    assert tokens > 0
    
    # Test token estimation with references
    tokens_with_refs = analyzer.estimate_token_needs(complexity, with_references=True)
    assert isinstance(tokens_with_refs, int)
    assert tokens_with_refs > tokens  # Should be more tokens with references

@pytest.mark.asyncio
async def test_team_advanced_features():
    """Test advanced Team class features."""
    # Create agents
    agent1 = DynoAgent("Agent1", "Role1", ["Skill1"], "Goal1")
    agent2 = DynoAgent("Agent2", "Role2", ["Skill2"], "Goal2")
    agent3 = DynoAgent("Agent3", "Role3", ["Skill3"], "Goal3")
    
    # Test team creation with initial agents
    team = Team("AdvancedTeam", [agent1, agent2])
    assert len(team.agents) == 2
    
    # Test agent addition with dependencies
    team.add_agent(agent3, dependencies=["Agent1"])
    assert len(team.agents) == 3
    
    # Test dependency graph creation
    assert team.dependency_graph.number_of_nodes() == 3
    assert team.dependency_graph.has_edge("Agent1", "Agent3")
    
    # Test execution plan creation
    assert len(team.execution_plan) > 0
    
    # Test parallel execution
    results = await team.execute_parallel()
    assert len(results) == 3
    
    # Test optimal execution
    results = await team.execute_optimal()
    assert len(results) == 3
    
    # Test team visualization (should not raise error)
    team.visualize_dependencies()
    
    # Test execution plan clearing
    team.execution_plan = []
    assert len(team.execution_plan) == 0

def test_error_handling_advanced():
    """Test advanced error handling scenarios."""
    agent1 = DynoAgent("Agent1", "Role1", ["Skill1"], "Goal1")
    agent2 = DynoAgent("Agent2", "Role2", ["Skill2"], "Goal2")

    # Test invalid agent initialization
    with pytest.raises(ValueError):
        DynoAgent("", "Role", ["Skill"], "Goal")  # Empty name

    with pytest.raises(ValueError):
        DynoAgent("Name", "", ["Skill"], "Goal")  # Empty role

    with pytest.raises(ValueError):
        DynoAgent("Name", "Role", "not_a_list", "Goal")  # Invalid skills type

    with pytest.raises(ValueError):
        DynoAgent("Name", "Role", ["Skill"], "")  # Empty goal

    # Test invalid team operations
    team = Team("TestTeam")
    
    with pytest.raises(AttributeError):
        team.add_agent(None)  # None agent
    
    # Test invalid tool operations
    with pytest.raises(ValueError):
        agent1.register_tool("", lambda x: x)  # Empty tool name
    
    with pytest.raises(ValueError):
        agent1.register_tool("tool", None)  # Invalid tool function
    
    # Test circular dependencies with multiple agents
    team = Team("TestTeam", [agent1, agent2])
    agent3 = DynoAgent("Agent3", "Role3", ["Skill3"], "Goal3")
    team.add_agent(agent3)
    
    with pytest.raises(ValueError):
        team.explicit_dependencies = {
            "Agent1": ["Agent2"],
            "Agent2": ["Agent3"],
            "Agent3": ["Agent1"]
        }
        team._add_explicit_dependencies()
        team._create_execution_plan() 