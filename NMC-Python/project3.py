# Statically typed recipe cost calculator pork
from typing import Final

# Unit prices and quantities
BREAD_COST: Final[float] = 5.30  # per loaf (12 slices)
LUNCHMEAT_COST: Final[float] = 16.96  # per 20 slices
CHEESE_COST: Final[float] = 12.72  # per 30 slices
MAYO_COST: Final[float] = 15.90  # per quarter-gallon (128 tbsp)
TOOTHPICK_COST: Final[float] = 1.06  # per 100 toothpicks

# Package sizes (units per package)
BREAD_PACK_SIZE: Final[int] = 12
LUNCHMEAT_PACK_SIZE: Final[int] = 20
CHEESE_PACK_SIZE: Final[int] = 30
MAYO_PACK_SIZE: Final[int] = 16
TOOTHPICK_PACK_SIZE: Final[int] = 100

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

    return (
        bread_per_sandwich
        + meat_per_sandwich
        + cheese_per_sandwich
        + mayo_per_sandwich
        + toothpicks_per_sandwich
    )


# Main calculations
sandwich_cost = round(calculate_sandwich_cost(),2)
three_batches_cost = round(3 * 6 * sandwich_cost,2)
discounted_batch_cost = round(6 * sandwich_cost * 0.85,2)


# Calculate leftovers after each batch
def calculate_leftovers(batches: int) -> dict:
    # Calculate total usage
    total_sandwiches = batches * 6
    bread_used = total_sandwiches * BREAD_SLICES
    meat_used = total_sandwiches * MEAT_SLICES
    cheese_used = total_sandwiches * CHEESE_SLICES
    mayo_used = total_sandwiches * MAYO_TBSP
    toothpicks_used = total_sandwiches * TOOTHPICS

    # Use // (floor division) and % (modulo) to find packages needed.
    # Floor division gives full packages; modulo checks for a partial package.
    bread_packs = (bread_used // BREAD_PACK_SIZE) + (
        1 if bread_used % BREAD_PACK_SIZE else 0
    )
    meat_packs = (meat_used // LUNCHMEAT_PACK_SIZE) + (
        1 if meat_used % LUNCHMEAT_PACK_SIZE else 0
    )
    cheese_packs = (cheese_used // CHEESE_PACK_SIZE) + (
        1 if cheese_used % CHEESE_PACK_SIZE else 0
    )
    mayo_packs = (mayo_used // MAYO_PACK_SIZE) + (
        1 if mayo_used % MAYO_PACK_SIZE else 0
    )
    toothpick_packs = (toothpicks_used // TOOTHPICK_PACK_SIZE) + (
        1 if toothpicks_used % TOOTHPICK_PACK_SIZE else 0
    )

    # Calculate leftover units after batch using total purchased minus used.
    # Note: (pack_size - (used % pack_size)) % pack_size also directly
    # calculates the remainder left in the opened package using modulo (%).
    bread_left = (bread_packs * BREAD_PACK_SIZE) - bread_used
    meat_left = (meat_packs * LUNCHMEAT_PACK_SIZE) - meat_used
    cheese_left = (cheese_packs * CHEESE_PACK_SIZE) - cheese_used
    mayo_left = (mayo_packs * MAYO_PACK_SIZE) - mayo_used
    toothpicks_left = (toothpick_packs * TOOTHPICK_PACK_SIZE) - toothpicks_used

    return {
        "bread": bread_left,
        "lunchmeat": meat_left,
        "cheese": cheese_left,
        "mayo": mayo_left,
        "toothpicks": toothpicks_left
    }


# Function to check if initial quantities are sufficient for the batch
def check_sufficient_ingredients(batches: int) -> None:
    # Calculate required amount for the batch
    total_sandwiches = batches * 6
    required_bread = total_sandwiches * BREAD_SLICES
    required_meat = total_sandwiches * MEAT_SLICES
    required_cheese = total_sandwiches * CHEESE_SLICES
    required_mayo = total_sandwiches * MAYO_TBSP
    required_toothpicks = total_sandwiches * TOOTHPICS

    # Check each ingredient
    if INITIAL_BREAD < required_bread:
        print(
            f"NOTICE: Bread initial quantity ({INITIAL_BREAD}) is not "
            f"enough for {batches} batches. Multiple packages needed."
        )
    if INITIAL_LUNCHMEAT < required_meat:
        print(
            f"NOTICE: Lunchmeat initial quantity ({INITIAL_LUNCHMEAT}) is not "
            f"enough for {batches} batches. Multiple packages needed."
        )
    if INITIAL_CHEESE < required_cheese:
        print(
            f"NOTICE: Cheese initial quantity ({INITIAL_CHEESE}) is not "
            f"enough for {batches} batches. Multiple packages needed."
        )
    if INITIAL_MAYO < required_mayo:
        print(
            f"NOTICE: Mayo initial quantity ({INITIAL_MAYO}) is not "
            f"enough for {batches} batches. Multiple packages needed."
        )
    if INITIAL_TOOTHPICKS < required_toothpicks:
        print(
            f"NOTICE: Toothpicks initial quantity ({INITIAL_TOOTHPICKS}) is "
            f"not enough for {batches} batches. Multiple packages needed."
        )

# Print the recipe
print("=" * 20)
print("Recipe: Sandwich")


# Print ingredient costs
print("=" * 20)
print("Recipe Ingredient Costs:")
print(f"Bread: ${BREAD_COST: .2f} per loaf (12 slices)")
print(f"Lunchmeat: ${LUNCHMEAT_COST: .2f} per 20 slices")
print(f"Cheese: ${CHEESE_COST: .2f} per 30 slices")
print(f"Mayo: ${MAYO_COST: .2f} per half-gallon (16 tbsp)")
print(f"Toothpicks: ${TOOTHPICK_COST: .2f} per 100 toothpicks")
print("=" * 20, end='')

# Print cost per sandwich
print("\nCost per Sandwich: ", f"${sandwich_cost: .2f}")
print("3 batches (18 sandwiches): ", f"${three_batches_cost: .2f}")
print(
    "1 batch (6 sandwiches) at 15% discount: ",
    f"${discounted_batch_cost: .2f}"
)

# Print divider
print("=" * 20)

check_sufficient_ingredients(1)

# Print leftovers after 1 batch
print("\nLeftover Ingredients after 1 Batch:")
leftovers = calculate_leftovers(1)
for item, quantity in leftovers.items():
    print(f"{item}: {quantity} units left")

# Print separator line
print("=" * 20)
