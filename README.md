
# 🚀 LLM Fine-tuning Dataset Hub

<p align="center">
	<img src="docs/logos.png" alt="Supported Model Logos" width="400"/>
</p>

<div align="center">
	<a href="#features"><img src="https://img.shields.io/badge/Features-Complete-brightgreen"/></a>
	<a href="#license"><img src="https://img.shields.io/badge/License-Apache%202.0-blue"/></a>
	<a href="#contributing"><img src="https://img.shields.io/badge/Contributions-Welcome-orange"/></a>
	<a href="#supported-models"><img src="https://img.shields.io/badge/Models-Mistral%2C%20Pi%2C%20Gemini%2C%20Distilled-purple"/></a>
	<a href="#dialogue-support"><img src="https://img.shields.io/badge/Dialogue-Supported-success"/></a>
</div>

A professional, extensible dataset collection and preprocessing pipeline for fine-tuning Large Language Models (LLMs) using efficient techniques like QLoRA (Quantized Low-Rank Adaptation), Axolotl, model distillation, and advanced validation. Now with comprehensive dialogue model support!

## 🎯 Supported Models

<ul>
	<li><strong>Mistral</strong> <img src="https://img.shields.io/badge/-7B%20v0.1-blue"/></li>
	<li><strong>Pi</strong> <img src="https://img.shields.io/badge/-Conversational-green"/></li>
	<li><strong>Gemini</strong> <img src="https://img.shields.io/badge/-Multimodal-yellow"/></li>
	<li><strong>Custom Distilled Models</strong> <img src="https://img.shields.io/badge/-Student%20Models-lightgrey"/></li>
</ul>

## 📁 Repository Structure

```text
datasets-base/
├── data/                # Dataset storage
│   ├── raw/            # Original, unprocessed datasets
│   └── processed/      # Cleaned and formatted datasets
├── scripts/            # Processing utilities
│   ├── preprocessing/  # Data processing scripts
│   ├── training/       # Training utilities
│   └── validation/     # Data validation tools
├── notebooks/          # Interactive examples and training workflows
│   ├── 1_dataset_preparation.ipynb        # Dataset preprocessing
│   ├── 2_qlora_training.ipynb            # Basic QLoRA training
│   ├── 3_qlora_dialogue_training.ipynb   # Dialogue-specific QLoRA
│   └── 4_axolotl_dialogue_training.ipynb # Axolotl implementation
├── docs/              # Detailed documentation and guidelines
└── config/            # Model and training configurations
    └── model_configs/ # Model-specific settings
```

## 🛠️ Key Features

- <strong>Advanced Dialogue Support</strong>
  - Multi-turn conversation handling
  - Context window management
  - Proper dialogue formatting
  - Chat template support

- <strong>Dual Training Approaches</strong>
  - QLoRA Implementation
    - 4-bit quantization
    - Memory-efficient training
    - Parameter-efficient fine-tuning
  - Axolotl Integration
    - Simplified dialogue handling
    - Flash Attention 2 support
    - Automatic optimization

- <strong>Data Processing</strong>
  - Efficient preprocessing pipeline
  - Model-specific transformations
  - Advanced validation & quality checks
  - Dialogue-aware formatting

- <strong>Training Features</strong>
  - Cross-platform compatibility (Colab/Kaggle/Local)
  - Memory optimization techniques
  - Automated checkpointing
  - Progress tracking

## 🚀 Getting Started

1. <strong>Clone the repository</strong>
	```bash
	git clone https://github.com/bentex2006/datasets-base.git
	cd datasets-base
	```

2. <strong>Install dependencies</strong>
	```bash
	pip install -r requirements.txt
	```

3. <strong>Choose your training approach</strong>
   - For manual QLoRA: Use `notebooks/3_qlora_dialogue_training.ipynb`
   - For Axolotl: Use `notebooks/4_axolotl_dialogue_training.ipynb`

4. <strong>Follow setup instructions</strong>
	See `docs/setup.md` for environment-specific details.

## 📚 Documentation

- <strong>[Data Format Specifications](docs/data_format.md)</strong>
- <strong>[Preprocessing Guidelines](docs/preprocessing.md)</strong>
- <strong>[Model-specific Instructions](docs/models.md)</strong>
- <strong>[Contributing Guidelines](docs/CONTRIBUTING.md)</strong>

## 🎯 Training Approaches

### QLoRA Implementation
- 4-bit quantization for memory efficiency
- Low-rank adaptation for parameter efficiency
- Custom dialogue dataset handling
- Proper context management

### Axolotl Integration
- Simplified dialogue fine-tuning
- Built-in optimization techniques
- Flash Attention 2 support
- Efficient training configurations

## 📊 Dataset Statistics

<em>Coming soon: Automated dataset statistics and visualizations.</em>

## 📜 License

<img src="https://img.shields.io/badge/License-Apache%202.0-blue"/> This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

<img src="https://img.shields.io/badge/Contributions-Welcome-orange"/> Contributions are welcome! Please read our [Contributing Guidelines](docs/CONTRIBUTING.md) for details.

## 📫 Contact & Support

- <strong>Repository Owner:</strong> <a href="https://github.com/bentex2006">@bentex2006</a>
- <strong>Project Link:</strong> <a href="https://github.com/bentex2006/datasets-base">GitHub: datasets-base</a>
- <strong>Issues & Discussions:</strong> Use the GitHub Issues tab for bugs, feature requests, and questions.
