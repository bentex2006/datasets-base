# Data Format Specifications

## Overview
This document outlines the required data formats for fine-tuning different LLM models using our pipeline.

## General Format
Our datasets follow a standardized JSON format:

```json
{
    "text": "Input text",
    "response": "Target response",
    "metadata": {
        "source": "dataset_name",
        "category": "category_name",
        "quality_score": 0.95
    }
}
```

## Model-Specific Formats

### Mistral Format
```json
{
    "instruction": "Task description",
    "input": "Input text",
    "output": "Target response"
}
```

### Pi Format
```json
{
    "conversations": [
        {"role": "human", "content": "Input text"},
        {"role": "assistant", "content": "Target response"}
    ]
}
```

### Gemini Format
```json
{
    "prompt": "Input text",
    "completion": "Target response",
    "context": "Additional context (optional)"
}
```

## Quality Requirements

1. Text Cleaning
   - Remove HTML tags
   - Normalize whitespace
   - Handle special characters

2. Content Guidelines
   - Clear and concise instructions
   - High-quality responses
   - Proper formatting

3. Validation Criteria
   - Minimum length requirements
   - Maximum length limits
   - Content quality scores
