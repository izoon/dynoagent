"""Tests for the TaskComplexityAnalyzer class."""

import pytest

from dynoagent import TaskComplexityAnalyzer


def test_analyze_complexity_simple():
    """Test analysis of simple tasks."""
    analyzer = TaskComplexityAnalyzer()
    complexity = analyzer.analyze_complexity("List the key points briefly")
    assert complexity == "simple"


def test_analyze_complexity_medium():
    """Test analysis of medium complexity tasks."""
    analyzer = TaskComplexityAnalyzer()
    complexity = analyzer.analyze_complexity("Explain the concept of neural networks")
    assert complexity == "medium"


def test_analyze_complexity_complex():
    """Test analysis of complex tasks."""
    analyzer = TaskComplexityAnalyzer()
    complexity = analyzer.analyze_complexity(
        "Provide a comprehensive analysis of the economic impact"
    )
    assert complexity == "complex"


def test_analyze_complexity_with_role():
    """Test complexity analysis with role consideration."""
    analyzer = TaskComplexityAnalyzer()
    complexity = analyzer.analyze_complexity("Write a summary", role="researcher")
    # Even simple task should be considered complex for researcher role
    assert complexity == "complex"


def test_estimate_token_needs():
    """Test token estimation for different complexities."""
    analyzer = TaskComplexityAnalyzer()

    simple_tokens = analyzer.estimate_token_needs("simple")
    medium_tokens = analyzer.estimate_token_needs("medium")
    complex_tokens = analyzer.estimate_token_needs("complex")

    assert simple_tokens < medium_tokens < complex_tokens

    # Test with references
    with_refs = analyzer.estimate_token_needs("medium", with_references=True)
    without_refs = analyzer.estimate_token_needs("medium", with_references=False)
    assert with_refs > without_refs
