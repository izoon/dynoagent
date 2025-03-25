# DynoAgent 🤖

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Tests](https://github.com/izoon/dynoagent/actions/workflows/tests.yml/badge.svg)](https://github.com/izoon/dynoagent/actions/workflows/tests.yml)
[![Coverage](https://img.shields.io/badge/coverage-78%25-green.svg)](https://github.com/izoon/dynoagent/actions/workflows/tests.yml)

A Python package for managing and orchestrating AI agents in a team environment.

## Features

- Dynamic role-based agent framework
- Team-based task execution
- Flexible agent communication patterns
- Built-in task validation and error handling
- Support for async operations

## Installation

### From PyPI

```bash
pip install dynoagent
```

### From GitHub

```bash
# Basic installation
pip install git+https://github.com/izoon/dynoagent.git

# With development dependencies
pip install git+https://github.com/izoon/dynoagent.git#egg=dynoagent[dev]
```

## Quick Start

```python
from dynoagent import Agent, Team, Task

# Create agents
researcher = Agent("researcher", "Research and analyze data")
writer = Agent("writer", "Write reports and documentation")

# Create a team
team = Team([researcher, writer])

# Define tasks
research_task = Task("Research market trends", researcher)
writing_task = Task("Write report", writer)

# Execute tasks
team.execute_tasks([research_task, writing_task])
```

## Documentation

For detailed documentation, please visit our [GitHub repository](https://github.com/izoon/dynoagent#readme).

## Contributing

We welcome contributions! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- NetworkX team for the graph processing capabilities
- All our contributors and users

## 📬 Contact

- GitHub Issues: [https://github.com/izoon/dynoagent/issues](https://github.com/izoon/dynoagent/issues)
- Author: Vahid Salami (vahid.salami@izoon.com)

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