# Model-Specific Instructions

## Mistral
- Recommended batch size: 1-4
- Learning rate: 2e-4
- LoRA rank: 64
- QLoRA configuration:
  - bits: 4
  - groupsize: 128

## Pi
- Recommended batch size: 2-8
- Learning rate: 1e-4
- LoRA rank: 32
- QLoRA configuration:
  - bits: 4
  - groupsize: 128

## Gemini
- Recommended batch size: 1-4
- Learning rate: 5e-5
- LoRA rank: 64
- QLoRA configuration:
  - bits: 4
  - groupsize: 128

## Distillation
- Teacher model: Choose from Mistral/Pi/Gemini
- Student architectures:
  - 6 layers
  - 8 attention heads
  - Hidden size: 768
- Temperature: 2.0
- Alpha: 0.5
