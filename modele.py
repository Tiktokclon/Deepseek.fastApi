from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_name = "deepseek-ai/deepseek-llm-7b-instruct"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name, torch_dtype=torch.float16, device_map="auto"
)

def generate_response(prompt: str) -> str:
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    output = model.generate(**inputs, max_new_tokens=150, do_sample=True, temperature=0.7)
    return tokenizer.decode(output[0], skip_special_tokens=True)
