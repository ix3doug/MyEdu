# Statically typed recipe cost calculator
from typing import Final

# Unit prices and quantities
BREAD_COST: Final[float] = 5.0  # per loaf (12 slices)
LUNCHMEAT_COST: Final[float] = 8.0  # per 20 slices
CHEESE_COST: Final[float] = 12.0  # per 30 slices
MAYO_COST: Final[float] = 15.0  # per half-gallon (16 tbsp)
TOOTHPIC_COST: Final[float] = 1.0  # per 100 toothpicks

# Recipe per sandwich
BREAD_SLICES: Final[int] = 2
MEAT_SLICES: Final[int] = 6
CHEESE_SLICES: Final[int] = 2
MAYO_TBSP: Final[int] = 2
TOOTHPICS: Final[int] = 1

# Calculate cost per sandwich
def calculate_sandwich_cost() -> float:
    bread_per_sandwich = BREAD_SLICES * (BREAD_COST / 12)
    meat_per_sandwich = MEAT_SLICES * (LUNCHMEAT_COST / 20)
    cheese_per_sandwich = CHEESE_SLICES * (CHEESE_COST / 30)
    mayo_per_sandwich = MAYO_TBSP * (MAYO_COST / 16)
    toothpicks_per_sandwich = TOOTHPICS * (TOOTHPIC_COST / 100)
    
    return bread_per_sandwich + meat_per_sandwich + cheese_per_sandwich + mayo_per_sandwich + toothpicks_per_sandwich

# Main calculations
sandwich_cost = calculate_sandwich_cost()
three_batches_cost = 3 * 6 * sandwich_cost
discounted_batch_cost = 6 * sandwich_cost * 0.85

# Output results
print(f"Cost per sandwich: ${sandwich_cost:.2f}")
print(f"3 batches (18 sandwiches): ${three_batches_cost:.2f}")
print(f"1 batch (6 sandwiches) at 15% discount: ${discounted_batch_cost:.2f}")
