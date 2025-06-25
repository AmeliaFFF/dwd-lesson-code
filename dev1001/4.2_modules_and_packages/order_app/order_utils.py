# order_utils.py
TAX_RATE = 0.07 # 7% sales tax

def calculate_subtotal(items_prices):
    """Calculates subtotal from a list of item prices."""
    return sum(items_prices)

def calculate_tax(subtotal_amount):
    """Calculates tax based on the subtotal."""
    return subtotal_amount * TAX_RATE

def calculate_grand_total(subtotal_amount):
    """Calculates grand total including tax."""
    subtotal_amount = apply_discount(subtotal_amount)
    tax = calculate_tax(subtotal_amount)
    return subtotal_amount + tax

def apply_discount(subtotal, discount_threshold=50.0, discount_percentage=0.10):
    """Calculate and apply discount to subtotal if eligible."""
    if subtotal > discount_threshold:
        return subtotal * (1 - discount_percentage)
    else:
        return subtotal
    # This could be written as a ternary instead:
    # return subtotal * (1 - discount_percentage if subtotal > discount_threshold else 1)
    # The above if/else is more readable though.
      