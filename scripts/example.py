"""
Example script demonstrating how to use the dataset tools.
"""
import os
from pathlib import Path
from scripts.preprocessing.data_processor import DataProcessor
from scripts.validation.data_validator import DataValidator
from scripts.training.qlora_trainer import QLoraTrainer

def main():
    # Initialize processors
    processor = DataProcessor()
    validator = DataValidator()
    
    # Example: Process and validate data for Mistral
    raw_data_path = "data/raw/your_dataset.jsonl"
    processed_path = "data/processed/mistral_format.jsonl"
    
    # Load and process data (example data structure)
    raw_data = [
        {
            "instruction": "Translate this to French",
            "input": "Hello, how are you?",
            "output": "Bonjour, comment allez-vous?"
        }
        # Add more examples...
    ]
    
    # Format for Mistral
    processor.format_for_mistral(raw_data, processed_path)
    
    # Validate the processed dataset
    is_valid, errors = validator.validate_dataset(processed_path, "mistral")
    if not is_valid:
        print("Validation errors:", errors)
        return
    
    # Create train/val split
    validator.create_train_val_split(
        processed_path,
        "data/processed/mistral_split",
        val_size=0.1
    )
    
    # Initialize QLoRA training
    trainer = QLoraTrainer("config/model_configs/mistral_qlora_config.json")
    trainer.setup_model()
    
    print("Setup complete! Ready for training.")

if __name__ == "__main__":
    main()
