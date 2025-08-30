"""
Dataset validation utilities for ensuring data quality.
"""
import json
from typing import Dict, List, Tuple
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split

class DataValidator:
    def __init__(self, config_path: str = None):
        self.config = self._load_config(config_path) if config_path else {}
        
    def _load_config(self, config_path: str) -> Dict:
        """Load validation configuration."""
        with open(config_path, 'r') as f:
            return json.load(f)
    
    def validate_dataset(self, 
                        data_path: str, 
                        model_type: str = None) -> Tuple[bool, List[str]]:
        """
        Validate an entire dataset file.
        Returns (is_valid, error_messages)
        """
        errors = []
        try:
            data = self._load_data(data_path)
        except Exception as e:
            return False, [f"Failed to load dataset: {str(e)}"]
            
        # Basic validation
        if not data or len(data) == 0:
            return False, ["Dataset is empty"]
            
        # Model-specific validation
        if model_type:
            valid, model_errors = self._validate_model_format(data, model_type)
            if not valid:
                errors.extend(model_errors)
                
        # Content validation
        content_errors = self._validate_content(data)
        if content_errors:
            errors.extend(content_errors)
            
        return len(errors) == 0, errors
    
    def _validate_model_format(self, 
                             data: List[Dict], 
                             model_type: str) -> Tuple[bool, List[str]]:
        """Validate data format for specific models."""
        errors = []
        required_fields = {
            "mistral": ["instruction", "input", "output"],
            "pi": ["input", "output"],
            "gemini": ["prompt", "completion"]
        }
        
        if model_type not in required_fields:
            return False, [f"Unknown model type: {model_type}"]
            
        fields = required_fields[model_type]
        for idx, entry in enumerate(data):
            missing = [f for f in fields if f not in entry]
            if missing:
                errors.append(f"Entry {idx}: Missing fields {missing}")
                
        return len(errors) == 0, errors
    
    def _validate_content(self, data: List[Dict]) -> List[str]:
        """Validate content quality."""
        errors = []
        
        min_length = self.config.get("min_length", 10)
        max_length = self.config.get("max_length", 2048)
        
        for idx, entry in enumerate(data):
            # Length checks
            for field in ["input", "output", "instruction", "prompt", "completion"]:
                if field in entry:
                    length = len(entry[field])
                    if length < min_length:
                        errors.append(f"Entry {idx}: {field} too short ({length} chars)")
                    elif length > max_length:
                        errors.append(f"Entry {idx}: {field} too long ({length} chars)")
        
        return errors
    
    def create_train_val_split(self, 
                             data_path: str, 
                             output_dir: str, 
                             val_size: float = 0.1) -> None:
        """Split dataset into training and validation sets."""
        data = self._load_data(data_path)
        train_data, val_data = train_test_split(data, test_size=val_size)
        
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Save splits
        self._save_jsonl(train_data, output_dir / "train.jsonl")
        self._save_jsonl(val_data, output_dir / "val.jsonl")
    
    def _load_data(self, path: str) -> List[Dict]:
        """Load dataset from file."""
        data = []
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                data.append(json.loads(line.strip()))
        return data
    
    def _save_jsonl(self, data: List[Dict], output_path: Path) -> None:
        """Save data in JSONL format."""
        with open(output_path, 'w', encoding='utf-8') as f:
            for item in data:
                f.write(json.dumps(item) + '\n')
