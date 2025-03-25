def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    If the discount is 20% or higher, apply the discount; otherwise, return the original price.
    """
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    return price

# Get user input
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))
    
    # Calculate the final price
    final_price = calculate_discount(price, discount_percent)
    
    # Display result
    print(f"Final price after discount: ${final_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numerical values for price and discount.")