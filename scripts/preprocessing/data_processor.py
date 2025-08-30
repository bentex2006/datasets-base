"""
Core data preprocessing utilities for LLM fine-tuning datasets.
"""
import json
import pandas as pd
from typing import Dict, List, Union
from pathlib import Path

class DataProcessor:
    def __init__(self, config_path: str = None):
        self.config = self._load_config(config_path) if config_path else {}
        
    def _load_config(self, config_path: str) -> Dict:
        """Load preprocessing configuration."""
        with open(config_path, 'r') as f:
            return json.load(f)
    
    def clean_text(self, text: str) -> str:
        """Clean and normalize text data."""
        if not text:
            return ""
        # Basic cleaning
        text = text.strip()
        # Normalize whitespace
        text = " ".join(text.split())
        return text
    
    def format_for_mistral(self, 
                          data: List[Dict[str, str]], 
                          output_path: str) -> None:
        """Format data for Mistral model fine-tuning."""
        formatted = [{
            "instruction": item.get("instruction", ""),
            "input": item.get("input", ""),
            "output": item.get("output", "")
        } for item in data]
        
        self._save_jsonl(formatted, output_path)
    
    def format_for_pi(self, 
                     data: List[Dict[str, str]], 
                     output_path: str) -> None:
        """Format data for Pi model fine-tuning."""
        formatted = [{
            "conversations": [
                {"role": "human", "content": item.get("input", "")},
                {"role": "assistant", "content": item.get("output", "")}
            ]
        } for item in data]
        
        self._save_jsonl(formatted, output_path)
    
    def format_for_gemini(self, 
                         data: List[Dict[str, str]], 
                         output_path: str) -> None:
        """Format data for Gemini model fine-tuning."""
        formatted = [{
            "prompt": item.get("input", ""),
            "completion": item.get("output", ""),
            "context": item.get("context", "")
        } for item in data]
        
        self._save_jsonl(formatted, output_path)
    
    def validate_entry(self, entry: Dict) -> bool:
        """Validate a single data entry."""
        if not entry.get("input") or not entry.get("output"):
            return False
            
        # Check minimum lengths
        min_input_length = self.config.get("min_input_length", 10)
        min_output_length = self.config.get("min_output_length", 10)
        
        if (len(entry["input"]) < min_input_length or 
            len(entry["output"]) < min_output_length):
            return False
            
        return True
    
    def _save_jsonl(self, data: List[Dict], output_path: str) -> None:
        """Save data in JSONL format."""
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            for item in data:
                f.write(json.dumps(item) + '\n')
