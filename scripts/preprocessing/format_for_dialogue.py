import json
from typing import List, Dict

def format_for_dialogue(data: List[Dict], output_path: str):
    """Format data for dialogue-based training."""
    with open(output_path, 'w', encoding='utf-8') as f:
        for item in data:
            f.write(json.dumps({"dialogue": item["dialogue"]}) + '\n')

# Example usage:
if __name__ == "__main__":
    # Load sample data
    with open("../../data/raw/sample_dialogue_dataset.jsonl", "r", encoding="utf-8") as f:
        data = [json.loads(line) for line in f]
    format_for_dialogue(data, "../../data/processed/dialogue_format.jsonl")
