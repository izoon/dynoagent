"""
Example of parallel team execution in DynoAgent.
This example demonstrates how to:
1. Create agents with different roles
2. Form a team with independent tasks that can run in parallel
3. Execute tasks in parallel where possible
"""

from dynoagent import DynoAgent, Team


def main():
    # Create agents for independent data processing tasks
    image_processor = DynoAgent(
        name="ImageProcessor",
        role="Processor",
        skills=["Image Recognition", "Feature Extraction"],
        goal="Process and analyze image data",
    )

    text_processor = DynoAgent(
        name="TextProcessor",
        role="Processor",
        skills=["NLP", "Text Analysis"],
        goal="Process and analyze text data",
    )

    audio_processor = DynoAgent(
        name="AudioProcessor",
        role="Processor",
        skills=["Audio Analysis", "Speech Recognition"],
        goal="Process and analyze audio data",
    )

    data_aggregator = DynoAgent(
        name="DataAggregator",
        role="Aggregator",
        skills=["Data Integration", "Multi-modal Fusion"],
        goal="Aggregate results from all processors",
    )

    # Create a team with parallel processing capabilities
    processing_team = Team(
        "MultiModalProcessingTeam", [image_processor, text_processor, audio_processor]
    )

    # Add aggregator that depends on all processors
    # This creates a parallel workflow where all processors run independently
    # and the aggregator waits for all of them to complete
    processing_team.add_agent(
        data_aggregator,
        dependencies=["ImageProcessor", "TextProcessor", "AudioProcessor"],
    )

    # Execute the workflow in parallel
    # Processors will run concurrently, then aggregator will run
    results = processing_team.execute_parallel()

    # Print execution results
    print("\nParallel Execution Results:")
    for agent_name, result in results.items():
        print(f"{agent_name}: {result}")


if __name__ == "__main__":
    main()
