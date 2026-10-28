# Statically typed recipe cost calculator
from typing import Final

# Unit prices and quantities
BREAD_COST: Final[float] = 5.0  # per loaf (12 slices)
LUNCHMEAT_COST: Final[float] = 16.0  # per 20 slices
CHEESE_COST: Final[float] = 12.0  # per 30 slices
MAYO_COST: Final[float] = 15.0  # per quarter-gallon (128 tbsp)
TOOTHPICK_COST: Final[float] = 1.0  # per 100 toothpicks

# Recipe per sandwich
BREAD_SLICES: Final[int] = 2
MEAT_SLICES: Final[int] = 6
CHEESE_SLICES: Final[int] = 2
MAYO_TBSP: Final[int] = 2
TOOTHPICS: Final[int] = 1

# Initial pantry quantities (assumed for calculation purposes)
# These values are not provided by user but needed for leftover calculation
INITIAL_BREAD: Final[int] = 12  # 1 loaf
INITIAL_LUNCHMEAT: Final[int] = 20  # 1 pack
INITIAL_CHEESE: Final[int] = 30  # 1 pack
INITIAL_MAYO: Final[int] = 64  # 1 half-gallon
INITIAL_TOOTHPICKS: Final[int] = 100  # 1 pack

# Calculate cost per sandwich
def calculate_sandwich_cost() -> float:
    bread_per_sandwich = BREAD_SLICES * (BREAD_COST / 12)
    meat_per_sandwich = MEAT_SLICES * (LUNCHMEAT_COST / 20)
    cheese_per_sandwich = CHEESE_SLICES * (CHEESE_COST / 30)
    mayo_per_sandwich = MAYO_TBSP * (MAYO_COST / 16)
    toothpicks_per_sandwich = TOOTHPICS * (TOOTHPICK_COST / 100)
    
    return bread_per_sandwich + meat_per_sandwich + cheese_per_sandwich + mayo_per_sandwich + toothpicks_per_sandwich

# Main calculations
sandwich_cost = calculate_sandwich_cost()
three_batches_cost = 3 * 6 * sandwich_cost
discounted_batch_cost = 6 * sandwich_cost * 0.85

# Calculate leftovers after each batch
def calculate_leftovers(batches: int) -> dict:
    # Calculate total usage
    total_sandwiches = batches * 6
    bread_used = total_sandwiches * BREAD_SLICES
    meat_used = total_sandwiches * MEAT_SLICES
    cheese_used = total_sandwiches * CHEESE_SLICES
    mayo_used = total_sandwiches * MAYO_TBSP
    toothpicks_used = total_sandwiches * TOOTHPICS
    
    # Calculate leftovers
    bread_left = INITIAL_BREAD - bread_used
    meat_left = INITIAL_LUNCHMEAT - meat_used
    cheese_left = INITIAL_CHEESE - cheese_used
    mayo_left = INITIAL_MAYO - mayo_used
    toothpicks_left = INITIAL_TOOTHPICKS - toothpicks_used
    
    return {
        "bread": bread_left,
        "lunchmeat": meat_left,
        "cheese": cheese_left,
        "mayo": mayo_left,
        "toothpicks": toothpicks_left
    }

# Print ingredient costs
print("=" * 20)
print("Ingredient Costs:")
print(f"Bread: ${BREAD_COST:.2f} per loaf (12 slices)")
print(f"Lunchmeat: ${LUNCHMEAT_COST:.2f} per 20 slices")
print(f"Cheese: ${CHEESE_COST:.2f} per 30 slices")
print(f"Mayo: ${MAYO_COST:.2f} per half-gallon (16 tbsp)")
print(f"Toothpicks: ${TOOTHPICK_COST:.2f} per 100 toothpicks")
print("=" * 20,end='')

# Print cost per sandwich
print("\nCost per Sandwich:", f"${sandwich_cost:.2f}")
print("3 batches (18 sandwiches):", f"${three_batches_cost:.2f}")
print("1 batch (6 sandwiches) at 15% discount:", f"${discounted_batch_cost:.2f}")

# Print divider
print("=" * 20,end='')

# Print leftovers after 1 batch
print("\nLeftover Ingredients after 1 Batch:")
leftovers = calculate_leftovers(1)
for item, quantity in leftovers.items():
    print(f"{item}: {quantity} units left")

# Print separator line
print("=" * 20)
