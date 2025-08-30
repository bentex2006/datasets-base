"""
QLoRA training utilities for different model architectures.
"""
import json
import torch
from typing import Dict
from pathlib import Path
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    TrainingArguments
)
from peft import (
    LoraConfig,
    prepare_model_for_kbit_training,
    get_peft_model
)

class QLoraTrainer:
    def __init__(self, config_path: str):
        self.config = self._load_config(config_path)
        self.model = None
        self.tokenizer = None
        
    def _load_config(self, config_path: str) -> Dict:
        """Load training configuration."""
        with open(config_path, 'r') as f:
            return json.load(f)
    
    def setup_model(self):
        """Initialize model with QLoRA configuration."""
        # Quantization config
        quant_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_compute_dtype=torch.float16,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_use_double_quant=True
        )
        
        # Load base model
        self.model = AutoModelForCausalLM.from_pretrained(
            self.config["model_name_or_path"],
            quantization_config=quant_config,
            device_map="auto"
        )
        
        # Load tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(
            self.config["model_name_or_path"],
            padding_side="right",
            use_fast=False
        )
        
        # Prepare model for k-bit training
        self.model = prepare_model_for_kbit_training(self.model)
        
        # LoRA configuration
        lora_config = LoraConfig(
            r=self.config.get("lora_r", 64),
            lora_alpha=self.config.get("lora_alpha", 16),
            lora_dropout=self.config.get("lora_dropout", 0.1),
            bias="none",
            task_type="CAUSAL_LM"
        )
        
        # Get PEFT model
        self.model = get_peft_model(self.model, lora_config)
        
    def get_training_args(self) -> TrainingArguments:
        """Get training arguments from config."""
        return TrainingArguments(
            output_dir=self.config["output_dir"],
            num_train_epochs=self.config.get("num_train_epochs", 3),
            per_device_train_batch_size=self.config.get("per_device_train_batch_size", 4),
            gradient_accumulation_steps=self.config.get("gradient_accumulation_steps", 4),
            learning_rate=self.config.get("learning_rate", 2e-4),
            max_grad_norm=self.config.get("max_grad_norm", 0.3),
            warmup_ratio=self.config.get("warmup_ratio", 0.03),
            lr_scheduler_type=self.config.get("lr_scheduler_type", "constant"),
            save_strategy="steps",
            save_steps=50,
            logging_steps=10,
            evaluation_strategy="steps",
            eval_steps=50,
            load_best_model_at_end=True,
        )
        
    def save_model(self, output_path: str):
        """Save the trained model."""
        self.model.save_pretrained(output_path)
        self.tokenizer.save_pretrained(output_path)
