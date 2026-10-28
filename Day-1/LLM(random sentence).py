import random

# A tiny "model": for each word, the possible next words and their probabilities
model = {
    "the":  {"cat": 0.5, "dog": 0.3, "idea": 0.2},
    "cat":  {"sat": 0.6, "ran": 0.4},
    "dog":  {"sat": 0.3, "ran": 0.7},
    "idea": {"ran": 1.0},
    "sat":  {"down": 1.0},
    "ran":  {"away": 1.0},
}

def generate(start, steps=3):
    text = [start]
    for _ in range(steps):
        options = model.get(text[-1])
        if not options:
            break
        words = list(options.keys())
        probs = list(options.values())
        next_word = random.choices(words, weights=probs)[0]  # sample one
        text.append(next_word)
    return " ".join(text)

for _ in range(5):
    print(generate("the"))