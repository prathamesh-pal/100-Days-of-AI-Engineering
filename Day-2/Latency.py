
time_to_first_token = 0.8  # seconds
generation_speed = 50      # tokens per second

# Answer lengths
long_answer_tokens = 500
short_answer_tokens = 100

# Calculate generation time
long_generation_time = long_answer_tokens / generation_speed
short_generation_time = short_answer_tokens / generation_speed

# Calculate total response time
long_total_time = time_to_first_token + long_generation_time
short_total_time = time_to_first_token + short_generation_time

# Calculate how many times faster the short answer is
speedup = long_total_time / short_total_time

print("500-token answer:")
print(f"Generation time: {long_generation_time:.2f} seconds")
print(f"Total time: {long_total_time:.2f} seconds")

print("\n100-token answer:")
print(f"Generation time: {short_generation_time:.2f} seconds")
print(f"Total time: {short_total_time:.2f} seconds")

print(f"\nThe 100-token answer is {speedup:.2f} times faster.")
