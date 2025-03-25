# DynoAgent Examples

This directory contains examples demonstrating different ways to use the DynoAgent framework for coordinating multiple agents in a team. Each example showcases a different execution strategy and team configuration.

## Examples Overview

### 1. Sequential Execution (`sequential.py`)
Demonstrates how to:
- Create a data analytics pipeline with sequential dependencies
- Set up a linear workflow where each agent depends on the previous one
- Execute tasks in sequential order using `Team.execute_sequential()`

Example workflow:
```
DataCollector -> DataProcessor -> DataAnalyzer -> ReportGenerator
```

### 2. Parallel Execution (`parallel.py`)
Demonstrates how to:
- Create a multi-modal processing pipeline with independent tasks
- Configure agents that can run concurrently
- Execute tasks in parallel using `Team.execute_parallel()`

Example workflow:
```
ImageProcessor ─┐
TextProcessor  ─┼─> DataAggregator
AudioProcessor ─┘
```

### 3. Dynamic Execution (`dynamic.py`)
Demonstrates how to:
- Create a complex MLOps pipeline with multiple dependencies
- Configure agents with branching and merging workflows
- Execute tasks optimally using `Team.execute_optimal()`

Example workflow:
```
                           ┌─> ErrorAnalysis ─┐
DataIngestion -> FeatureExtraction -> ModelTraining -> ModelEvaluation ─┤                 ┌─> Monitoring
                                                                        └─> ModelDeployment┘
```

## Usage

1. Install the DynoAgent package:
```bash
pip install dynoagent
```

2. Run any example:
```bash
python examples/sequential.py
python examples/parallel.py
python examples/dynamic.py
```

## Key Concepts

1. **Team Creation**: Each example shows how to create a `Team` instance and add agents with appropriate dependencies.

2. **Dependency Management**: The examples demonstrate different ways to structure agent dependencies:
   - Sequential: Linear dependencies
   - Parallel: Independent tasks
   - Dynamic: Complex dependency graphs

3. **Execution Strategies**: Each example uses a different execution strategy:
   - `execute_sequential()`: Run tasks one after another
   - `execute_parallel()`: Run independent tasks concurrently
   - `execute_optimal()`: Automatically determine the best execution order

4. **Error Handling**: The examples include proper error handling and dependency validation.

## Best Practices

1. **Clear Dependencies**: Always explicitly define agent dependencies when adding them to a team.
2. **Meaningful Names**: Use descriptive names for agents and teams.
3. **Proper Skills**: Define relevant skills for each agent based on their role.
4. **Goal Setting**: Set clear, specific goals for each agent.
5. **Execution Strategy**: Choose the appropriate execution strategy based on your workflow requirements. 