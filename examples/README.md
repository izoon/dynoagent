# DynoAgent Execution Strategy Examples

This directory contains examples of different execution strategies for agent workflows using the DynoAgent framework.

## Examples

### Sequential Execution (`sequential.py`)

The sequential execution strategy runs each agent one after another in a predefined order. This is the simplest approach and is suitable for workflows where each step depends on the output of the previous step.

```python
# Example of sequential execution
extracted_text = ingest_agent.perform_task("Extract receipt text", receipt_text)
indexed_text = indexing_agent.perform_task("Index extracted text", extracted_text)
summary = analysis_agent.perform_task("Analyze receipt data", indexed_text)
```

### Parallel Execution (`parallel.py`)

The parallel execution strategy runs independent agents concurrently using asyncio. This approach is more efficient for workflows where some steps can be executed in parallel.

```python
# Example of parallel execution
extracted_text = await asyncio.to_thread(ingest_agent.perform_task, "Extract receipt text", receipt_text)
indexing_task = asyncio.to_thread(indexing_agent.perform_task, "Index extracted text", extracted_text)
analysis_task = asyncio.to_thread(analysis_agent.perform_task, "Analyze receipt data", extracted_text)
indexed_text, summary = await asyncio.gather(indexing_task, analysis_task)
```

### Dynamic Execution (`dynamic.py`)

The dynamic execution strategy uses a reinforcement learning decision agent to determine the best next step based on the current state of the workflow. This approach is more flexible and can adapt to changing conditions.

```python
# Example of dynamic execution with RL decision agent
next_agent = rl_decision_agent.decide_next_agent(current_state, available_agents)
result = await asyncio.to_thread(next_agent.perform_task, f"Process {next_agent.name} task", current_data)
```

## Usage

To run these examples, you need to have the DynoAgent package installed:

```bash
pip install dynoagent
```

Then, you can run the examples directly:

```bash
python sequential.py
python parallel.py
python dynamic.py
```

Note that these examples are simplified for demonstration purposes. In a real application, you would likely need to customize them to fit your specific use case. 