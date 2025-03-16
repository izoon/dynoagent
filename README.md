# DynoAgent

A flexible framework for building and orchestrating intelligent agents. DynoAgent provides core components for creating, managing, and coordinating AI agents to solve complex tasks individually or as a team.

## Features

- **DynoAgent**: Core agent class with customizable roles, skills, and goals
- **Team**: Coordinate multiple agents with dependency-based execution ordering
- **DynoAgentWithTools**: Extended agent with tool integration capabilities
- **Task Complexity Analyzer**: Dynamic analysis of task complexity to optimize agent performance

## Installation

### Option 1: Install from PyPI (Coming Soon)

```bash
pip install dynoagent
```

### Option 2: Install from GitHub

```bash
pip install git+https://github.com/izoon/dynoagent.git
```

### Option 3: Install from source

```bash
# Clone the repository
git clone https://github.com/izoon/dynoagent.git

# Change to the project directory
cd dynoagent

# Install the package
pip install .
```

### Development Installation

For development, install in editable mode:

```bash
# Clone the repository
git clone https://github.com/izoon/dynoagent.git

# Change to the project directory
cd dynoagent

# Install in development mode
pip install -e .
```

## Basic Usage

### Creating a Simple Agent

```python
from dynoagent import DynoAgent

# Create a simple agent
agent = DynoAgent(
    name="ResearchAgent",
    role="Researcher",
    skills=["Web Search", "Data Analysis", "Report Writing"],
    goal="Find and analyze information on a specific topic"
)

# Perform a task
result = agent.perform_task("Research the impact of AI on healthcare")
print(result)
```

### Using the Task Complexity Analyzer

```python
from dynoagent import TaskComplexityAnalyzer

# Initialize the analyzer
analyzer = TaskComplexityAnalyzer()

# Analyze a task
task = "Create a comprehensive report on climate change"
complexity = analyzer.analyze_complexity(task)
print(f"Task complexity: {complexity}")

# Get recommended parameters based on complexity
params = analyzer.get_parameters_for_complexity(complexity)
print(f"Recommended parameters: {params}")
```

### Creating a Team of Agents

```python
from dynoagent import DynoAgent, Team

# Create multiple agents
research_agent = DynoAgent(
    name="ResearchAgent",
    role="Researcher",
    skills=["Data Collection", "Analysis"],
    goal="Gather and analyze data"
)

writing_agent = DynoAgent(
    name="WritingAgent",
    role="Writer",
    skills=["Content Creation", "Editing"],
    goal="Create well-written content"
)

review_agent = DynoAgent(
    name="ReviewAgent",
    role="Reviewer",
    skills=["Quality Control", "Feedback"],
    goal="Ensure quality of final output"
)

# Create a team with explicit dependencies
team = Team(
    name="ContentCreationTeam",
    agents=[research_agent, writing_agent, review_agent],
    explicit_dependencies={
        "WritingAgent": ["ResearchAgent"],
        "ReviewAgent": ["WritingAgent"]
    }
)

# Execute the team
context = {"topic": "Renewable Energy"}
results = team.execute_sequential(context)
```

## Advanced Usage

### Using DynoAgentWithTools

```python
from dynoagent import DynoAgentWithTools

# Create an agent with tools
agent_with_tools = DynoAgentWithTools(
    name="DataAgent",
    role="Data Processor",
    skills=["Data Loading", "Information Retrieval"],
    goal="Process and retrieve information from various data sources"
)

# Perform a task with tools
result = agent_with_tools.perform_task("Load and summarize data from the annual report")
print(result)
```

## Requirements

- Python 3.8+
- numpy
- networkx

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 