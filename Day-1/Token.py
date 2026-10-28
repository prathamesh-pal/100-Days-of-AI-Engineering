import tiktoken

enc = tiktoken.get_encoding("cl100k_base")

text = "The capital of France is Paris"
ids = enc.encode(text)

print(ids)                              # the token IDs
print([enc.decode([i]) for i in ids])   # each ID turned back into its text piece