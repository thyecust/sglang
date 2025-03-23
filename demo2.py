from transformers import AutoTokenizer
model_name = "/home/tianhaoyu/.cache/modelscope/hub/models/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B"


tokenizer = AutoTokenizer.from_pretrained(model_name)
print(len(tokenizer))
print(tokenizer.all_special_tokens)
print(tokenizer.decode([151643]))

