def get_leg_height(angle):
    """
    Simulates the floor height. 
    Equation: f(x) = x^3 - 2x - 5
    (This has a zero point around 2.09)
    """
    return (angle**3) - (angle * 2) - 5

def find_stable_angle(low, high, tolerance):
    # Check if the signs are the same at both ends
    f_low = get_leg_height(low)
    f_high = get_leg_height(high)
    
    if f_low * f_high > 0:
        return None # No root exists between these two points

    while (high - low) / 2 > tolerance:
        midpoint = (low + high) / 2
        if get_leg_height(midpoint) == 0:
            return midpoint
        
        # Decide which half to keep
        if get_leg_height(low) * get_leg_height(midpoint) < 0:
            high = midpoint
        else:
            low = midpoint
            
    return (low + high) / 2

# --- User Input Section ---

print("--- Wobbly Table Solver ---")
print("Find the rotation angle where all legs touch the ground.")

try:
    # We convert the input strings to floats immediately
    user_low = float(input("Enter the start of search range (e.g., 0): "))
    user_high = float(input("Enter the end of search range (e.g., 5): "))
    user_tol = float(input("Enter required precision (e.g., 0.001): "))

    # Run the solver
    result = find_stable_angle(user_low, user_high, user_tol)

    # Output the result
    if result is None:
        print("\nResult: No stable point found in that range.")
        print("Try a wider range, like -10 to 10.")
    else:
        print(f"\nSuccess! The table stabilizes at angle: {result:.4f}")

except ValueError:
    print("\nError: Please enter valid numbers, not letters or symbols.")