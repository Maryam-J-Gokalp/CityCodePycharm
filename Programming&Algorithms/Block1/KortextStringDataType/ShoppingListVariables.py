# Prompt user for the quantity of items
flowerpot = int(input('How many flowerpots? '))
flower_seeds = int(input('How many packs of flower seeds? '))
soil = int(input('How many bags of soil? '))
# Display the quantity of flowerpots
print(f"You have ordered {flowerpot} flowerpots.")

# costs of each shopping item
flowerpot_price = 4.00
flower_seeds_price = 1.00
soil_price = 5.00

# Create Sales Tax Variable
tax_rate = 0.06

# Calculate the cost of item

cost_of_items = (flowerpot * flowerpot_price) + (flower_seeds * flower_seeds_price) + (soil *soil_price)

#Calculate the cost of items plus tax
total_cost = (cost_of_items * tax_rate) + cost_of_items
print(total_cost)
