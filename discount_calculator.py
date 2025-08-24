def calculate_discount(price, discount_percent):

    if not (0 <= discount_percent <= 100):
        raise ValueError("Discount percent must be between 0 and 100.")
    
    discount_amount = (discount_percent / 100) * price
    discounted_price = price - discount_amount
    return (discounted_price)



original_price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))


discounted_price = calculate_discount(original_price, discount_percent)
if discount_percent >= 20:
    print(f"The discounted price is: {discounted_price}")
else:
    print("No discount applied.")
