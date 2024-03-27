from mii import pipeline
pipe = pipeline("mistralai/Mistral-7B-v0.1")
output = pipe(["Hello, my name is", "DeepSpeed is"], max_new_tokens=128)

print(dir(output))
print(output.generated_texts)
print(type(output.generated_texts))