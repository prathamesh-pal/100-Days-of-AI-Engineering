import tiktoken

enc = tiktoken.get_encoding("cl100k_base")

samples = {
    "english": "The weather is very nice today, so we decided to go for a walk in the park.",
    "hindi":   "आज मौसम बहुत अच्छा है, इसलिए हमने पार्क में टहलने जाने का फैसला किया।",
}

for name, text in samples.items():
    tokens = enc.encode(text)
    print(name, "| characters:", len(text), "| words:", len(text.split()), "| tokens:", len(tokens))