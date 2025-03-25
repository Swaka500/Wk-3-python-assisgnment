def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    If the discount percentage is 20% or higher, apply the discount.
    Otherwise, return the original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    return price

# Prompt user for input
try:
    price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))
    
    # Calculate and display final price
    final_price = calculate_discount(price, discount_percent)
    print(f"Final price after discount (if applicable): ${final_price:.2f}")
except ValueError:
    print("Please enter valid numerical values.")

    #THE END
