"""
Example of sequential team execution in DynoAgent.
This example demonstrates how to:
1. Create agents with different roles
2. Form a team with explicit dependencies
3. Execute tasks sequentially
"""

from dynoagent import DynoAgent, Team


def main():
    # Create agents with specific roles and skills
    data_collector = DynoAgent(
        name="DataCollector",
        role="Collector",
        skills=["Web Scraping", "API Integration"],
        goal="Collect raw data from various sources",
    )

    data_processor = DynoAgent(
        name="DataProcessor",
        role="Processor",
        skills=["Data Cleaning", "Feature Engineering"],
        goal="Process and clean raw data",
    )

    data_analyzer = DynoAgent(
        name="DataAnalyzer",
        role="Analyzer",
        skills=["Statistical Analysis", "Pattern Recognition"],
        goal="Analyze processed data and generate insights",
    )

    report_generator = DynoAgent(
        name="ReportGenerator",
        role="Reporter",
        skills=["Report Writing", "Data Visualization"],
        goal="Generate comprehensive reports from analysis",
    )

    # Create a team with sequential dependencies
    analytics_team = Team("AnalyticsTeam", [data_collector])

    # Add agents with explicit dependencies
    # This creates a linear workflow: Collector -> Processor -> Analyzer -> Reporter
    analytics_team.add_agent(data_processor, dependencies=["DataCollector"])
    analytics_team.add_agent(data_analyzer, dependencies=["DataProcessor"])
    analytics_team.add_agent(report_generator, dependencies=["DataAnalyzer"])

    # Execute the workflow sequentially
    # Each agent will wait for its dependencies to complete before starting
    results = analytics_team.execute_sequential()

    # Print execution results
    print("\nSequential Execution Results:")
    for agent_name, result in results.items():
        print(f"{agent_name}: {result}")


if __name__ == "__main__":
    main()
