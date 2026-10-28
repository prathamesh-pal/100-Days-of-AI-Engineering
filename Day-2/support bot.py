
# Token usage per request
input_tokens = 3000
output_tokens = 400

# Prices per million tokens (dollars)
input_price = 1
output_price = 5

# Response timing
time_to_first_token = 1.0  # seconds
generation_speed = 50      # tokens per second

# Monthly volume
monthly_requests = 20_000

# 1. Cost of one request
input_cost = (input_tokens / 1_000_000) * input_price
output_cost = (output_tokens / 1_000_000) * output_price
cost_per_request = input_cost + output_cost

# 2. Monthly cost
monthly_cost = cost_per_request * monthly_requests

# 3. Total response time
generation_time = output_tokens / generation_speed
total_time = time_to_first_token + generation_time

# Print results
print("COST")
print(f"Input cost per request: ${input_cost:.6f}")
print(f"Output cost per request: ${output_cost:.6f}")
print(f"Total cost per request: ${cost_per_request:.6f}")
print(f"Monthly cost: ${monthly_cost:.2f}")

print("\nRESPONSE TIME")
print(f"Generation time: {generation_time:.2f} seconds")
print(f"Total response time: {total_time:.2f} seconds")
