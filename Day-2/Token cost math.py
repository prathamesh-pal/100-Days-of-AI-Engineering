
import tiktoken

enc = tiktoken.get_encoding("cl100k_base")

samples = {
    "english": "The weather is very nice today, so we decided to go for a walk in the park.",
    "hindi": "आज मौसम बहुत अच्छा है, इसलिए हमने पार्क में टहलने जाने का फैसला किया।",
    "python_code": "for i in range(5):\n    print(i)",
    "numbers": "3141592, 2718281, 1618033, 1414213",
}

# Example price only: $1 per million input tokens.


PRICE_PER_MILLION = 1
REQUESTS = 10_000

results = {}

for name, text in samples.items():
    tokens = enc.encode(text)
    characters = len(text)
    words = len(text.split())
    token_count = len(tokens)

    tokens_per_character = token_count / characters
    cost = token_count * REQUESTS * PRICE_PER_MILLION / 1_000_000

    results[name] = token_count

    print(f"\n{name}")
    print("Characters:", characters)
    print("Words:", words)
    print("Tokens:", token_count)
    print(f"Tokens per character: {tokens_per_character:.4f}")
    print(f"Cost for 10,000 requests: ${cost:.6f}")

english_tokens = results["english"]
hindi_tokens = results["hindi"]

print("\nHindi vs English")
print("Token ratio:", hindi_tokens / english_tokens)
print(
    "Hindi is",
    f"{(hindi_tokens / english_tokens - 1) * 100:.2f}% more expensive"
    if hindi_tokens > english_tokens
    else f"{(1 - hindi_tokens / english_tokens) * 100:.2f}% cheaper"
    if hindi_tokens < english_tokens
    else "the same cost"
)
