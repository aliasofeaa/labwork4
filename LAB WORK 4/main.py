"""
 Program purpose: Review from customers about flowers
 Programmer: NOORALIA EVIEANNA SOFEA
 Date: 8 March 2024
"""

# lists of flower names, units sold, and customer reviews
flower_names = ["Daisy", "Rose", "Sunflower", "Marigold", "Jasmine", "Lavender", "Hibiscus", "Orchid", "Lily", "Tulip", "Jasmine",
                "Lotus", "Dahlia", "Dandelion", "Baby breath", "Cornflower", "Kale", "Lilac", "Bougainvillea", "Coatbuttons"]
units_sold = [300, 285, 174, 80, 196, 120, 240, 240, 245, 70, 245, 210, 230, 120, 90, 289, 85, 190, 300, 296]
customer_reviews = [5.0, 4.5, 3.9, 2.5, 4.0, 4.0, 5.0, 4.7, 3.6, 2.9, 3.2, 4.3, 5.0, 3.5, 2.5, 5.0, 2.7, 3.6, 4.2, 4.8]

# calculate the total number of units sold for all flowers based on the given flower sales data.
total_units_sold = sum(units_sold)
print("Total units sold for all flowers:", total_units_sold)

# Determine the flower with the highest sales among the provided flower sales data.
max_sales_index = units_sold.index(max(units_sold))
highest_sales = flower_names[max_sales_index]
print("Flowers with the highest sales:", highest_sales)

# Identify flowers with average customer reviews above 3 from the given flower sales data.
above_3_reviews = [flower_names[i] for i in range(len(customer_reviews)) if customer_reviews[i] > 3]
print("Flowers with average customer reviews above 3:", above_3_reviews)

# Calculate the average customer review score for all flowers based on the provided flower sales data.
average_review = sum(customer_reviews)/20
print("The average customer review score for all flowers:", average_review)

# Calculate the average sales for below-average sales
average_solds = total_units_sold / len(units_sold)

# Identify flowers names with below-average sales from the given flower sales
below_names = [flower_names[i] for i in range(len(units_sold)) if units_sold[i] < average_solds]
print("Flower with below-average sales from the average units sold:", below_names)
# Identify the below-average sales from the average units sold
below_average = [units_sold[i] for i in range(len(units_sold)) if units_sold[i] < average_solds]
print("Below-average sales from the average units sold:", below_average)
# Identify the below-average for customer review
below_review = [customer_reviews[i] for i in range(len(customer_reviews)) if customer_reviews[i] < average_review]
print("Below-average sales from the average customer review:",below_review)