# DynoAgent 🤖

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Tests](https://github.com/izoon/dynoagent/actions/workflows/tests.yml/badge.svg)](https://github.com/izoon/dynoagent/actions/workflows/tests.yml)
[![Coverage](https://img.shields.io/badge/coverage-78%25-green.svg)](https://github.com/izoon/dynoagent/actions/workflows/tests.yml)

DynoAgent is a powerful Python framework for building and orchestrating intelligent agents. It provides a flexible architecture for creating, managing, and coordinating AI agents that can work individually or as a team to solve complex tasks.

## 🌟 Key Features

- **Dynamic Role-Based Agents**: Create agents with specific roles, skills, and goals
- **Team Orchestration**: Coordinate multiple agents with automatic dependency management
- **Parallel & Sequential Execution**: Smart execution strategies based on task dependencies
- **Built-in Task Analysis**: Automatic complexity assessment and resource optimization
- **Extensible Tools System**: Easy integration of custom tools and data loaders
- **Dependency Graph Visualization**: Visual representation of agent relationships
- **Comprehensive Test Coverage**: 78% overall coverage with 100% coverage for core components
- **CLI Interface**: Command-line tools for agent creation and task execution

## 📦 Installation

### Basic Installation
```bash
pip install dynoagent
```

### Development Installation
```bash
# Clone the repository
git clone https://github.com/izoon/dynoagent.git
cd dynoagent

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install with development dependencies
pip install -e ".[dev]"
```

## 🚀 Quick Start

### Creating a Simple Agent

```python
from dynoagent import DynoAgent

# Create a basic agent
agent = DynoAgent(
    name="research_agent",
    role="researcher",
    skills=["web_search", "data_analysis"],
    goal="research_topic"
)

# Execute a task
result = agent.perform_task("Research AI trends in 2024")
```

### Building a Team of Agents

```python
from dynoagent import DynoAgent, Team

# Create specialized agents
data_agent = DynoAgent(
    name="DataAgent",
    role="data_processor",
    skills=["data_cleaning", "feature_extraction"],
    goal="prepare_data"
)

analysis_agent = DynoAgent(
    name="AnalysisAgent",
    role="analyzer",
    skills=["statistical_analysis", "visualization"],
    goal="analyze_data"
)

# Create a team with dependencies
team = Team(
    name="DataAnalysisTeam",
    agents=[data_agent, analysis_agent],
    explicit_dependencies={
        "AnalysisAgent": ["DataAgent"]
    }
)

# Execute the team
results = team.execute_optimal({"data_source": "example.csv"})
```

### Using Agents with Tools

```python
from dynoagent import DynoAgentWithTools

# Create an agent with custom tools
agent = DynoAgentWithTools(
    name="document_processor",
    role="processor",
    skills=["text_extraction", "indexing"],
    goal="process_documents",
    llm_provider="openai",  # Optional LLM provider
    temperature=0.7,        # Optional temperature setting
    max_tokens=1500        # Optional max tokens setting
)

# Process documents
results = agent.load_data("pdf", "document.pdf")
agent.index_documents(results)
```

## 🛠️ Advanced Features

### Task Complexity Analysis

```python
from dynoagent import TaskComplexityAnalyzer

analyzer = TaskComplexityAnalyzer()
complexity = analyzer.analyze_complexity(
    "Create a comprehensive market analysis report",
    role="analyst"
)
print(f"Task Complexity: {complexity}")
```

### Dependency Graph Visualization

```python
# Visualize team dependencies
team.visualize_dependencies("team_graph.png")
```

### Parallel Execution

```python
import asyncio

# Execute team tasks in parallel
async def main():
    results = await team.execute_parallel(context={})

asyncio.run(main())
```

## 📚 Documentation

For detailed documentation, visit our [documentation site](https://dynoagent.readthedocs.io/).

## 🧪 Testing

```bash
# Run tests
pytest

# Run tests with coverage
pytest --cov=dynoagent
```

Current test coverage:
- Overall: 78%
- Core components: 100%
- CLI: 92%
- Team management: 72%
- Task complexity: 77%

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- NetworkX team for the graph processing capabilities
- All our contributors and users

## 📬 Contact

- GitHub Issues: [https://github.com/izoon/dynoagent/issues](https://github.com/izoon/dynoagent/issues)
- Email: example@example.com 