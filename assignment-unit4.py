#STEP 1
# def hypotenuse(a, b):
#     # Check if arguments are received correctly
#     print("Debug: a =", a)
#     print("Debug: b =", b)
#     return 0.0

# print("Testing Step 1:")
# hypotenuse(3, 4)


# STEP 2
# def hypotenuse(a, b):
#     squared_a = a**2
#     squared_b = b**2
#     # Check intermediate math
#     print("Debug: a^2 =", squared_a)
#     print("Debug: b^2 =", squared_b)
#     return 0.0

# print("Testing Step 2:")
# hypotenuse(3, 4)


# PART 1 STEP 3 final one
# import math

# def hypotenuse(a, b):
#     sum_squares = a**2 + b**2
#     result = math.sqrt(sum_squares)
#     return result

# print("Final Output Test 1 (3, 4):", hypotenuse(3, 4))
# print("Final Output Test 2 (5, 12):", hypotenuse(5, 12))
# print("Final Output Test 3 (1, 1):", hypotenuse(1, 1))


# =========================================================




# PART II STEP 1

# def estimate_storage_cost(storage_gb, egress_gb, storage_rate, egress_rate):
#     # Verify inputs are bound to local variables correctly
#     print(f"Debug Input: Storage={storage_gb}GB, Egress={egress_gb}GB")
#     print(f"Debug Rates: Storage Rate={storage_rate}, Egress Rate={egress_rate}")
#     return 0.0

# print("--- STEP 1 Test ---")
# estimate_storage_cost(500, 100, 0.023, 0.09)


# STEP 2

# def estimate_storage_cost(storage_gb, egress_gb, storage_rate, egress_rate):
#     # Calculate individual cost components using floating-point multiplication
#     cost_storage = storage_gb * storage_rate
#     cost_egress = egress_gb * egress_rate

#     print(f"Debug: Storage Cost = {cost_storage}, Egress Cost = {cost_egress}")
#     return 0.0

# print("--- Step 2 Test ---")
# estimate_storage_cost(500, 100, 0.023, 0.09)


# FINAL STAGE
def estimate_storage_cost(storage_gb, egress_gb, storage_rate, egress_rate):
    # 1. Calculate storage cost (GB * Rate)
    cost_storage = storage_gb * storage_rate

    # 2. Calculate network egress cost (GB * Rate)
    cost_egress = egress_gb * egress_rate

    # 3. Sum total monthly cost
    total_cost = cost_storage + cost_egress
    return total_cost

# Final Output (Three distinct calls with different usage patterns)
# Case 1: Standard usage (500GB storage, 100GB egress)
print("Final Call 1:", estimate_storage_cost(500, 100, 0.023, 0.09))

# Case 2: Archival usage (High storage 2TB, Low egress 10GB, cheaper storage class)
print("Final Call 2:", estimate_storage_cost(2000, 10, 0.015, 0.09))

# Case 3: CDN Origin (Low storage 50GB, High egress 5TB)
print("Final Call 3:", estimate_storage_cost(50, 5000, 0.023, 0.08))






