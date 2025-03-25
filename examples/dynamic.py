"""
Example of dynamic team execution in DynoAgent.
This example demonstrates how to:
1. Create agents with different roles
2. Form a team with complex dependencies
3. Execute tasks dynamically based on the dependency graph
"""

from dynoagent import DynoAgent, Team

def main():
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
    # Feature extraction depends on data ingestion
    ml_team.add_agent(feature_extraction, dependencies=["DataIngestion"])

    # Model training depends on feature extraction
    ml_team.add_agent(model_training, dependencies=["FeatureExtraction"])

    # Model evaluation depends on model training
    ml_team.add_agent(model_evaluation, dependencies=["ModelTraining"])

    # Error analysis can start after model evaluation
    ml_team.add_agent(error_analysis, dependencies=["ModelEvaluation"])

    # Model deployment depends on both evaluation and error analysis
    ml_team.add_agent(model_deployment, dependencies=["ModelEvaluation", "ErrorAnalysis"])

    # Monitoring depends on deployment
    ml_team.add_agent(monitoring, dependencies=["ModelDeployment"])

    # Execute the workflow dynamically
    # The team will automatically determine the optimal execution order
    # based on the dependency graph and agent availability
    results = ml_team.execute_optimal()

    # Print execution results
    print("\nDynamic Execution Results:")
    for agent_name, result in results.items():
        print(f"{agent_name}: {result}")

    # Print execution plan
    print("\nExecution Plan:")
    for i, level in enumerate(ml_team.execution_plan):
        print(f"Level {i}: {', '.join(level)}")

if __name__ == "__main__":
    main()
