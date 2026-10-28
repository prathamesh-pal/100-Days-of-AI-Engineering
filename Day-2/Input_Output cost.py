
input_tokens = 2000
output_tokens = 500
requests = 10_000

input_price = 1  # Dollars per million input tokens
output_price = 5  # Dollars per million output tokens

input_cost = (input_tokens * requests / 1_000_000) * input_price
output_cost = (output_tokens * requests / 1_000_000) * output_price

total_cost = input_cost + output_cost

print(f"Input cost: ${input_cost:.2f}")
print(f"Output cost: ${output_cost:.2f}")
print(f"Total cost: ${total_cost:.2f}")

if input_cost > output_cost:
    print("Input costs more.")
elif output_cost > input_cost:
    print("Output costs more.")
else:
    print("Input and output cost the same.")
