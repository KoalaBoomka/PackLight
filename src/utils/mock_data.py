import random
import csv
import json

# Simple lists of clothing properties
TOPS = ['T-Shirt', 'Long Sleeve Shirt', 'Tank']
BOTTOMS = ['Jeans', 'Shorts', 'Sweatpants', 'Chinos']
LAYERS = ['Sweater', 'Hoodie', 'Cardigan']
JACKETS = ['Light Jacket', 'Bomber', 'Rain Jacket']
SHOES = ['Low Sneakers', 'Boots', 'High Sneakers']

COLORS = ['Black', 'White', 'Navy', 'Gray', 'Beige', 'Blue', 'Purple']

def create_item(item_type, name):
    """Create one clothing item"""
    return {
        'type': item_type,
        'name': name,
        'color': random.choice(COLORS),
        'min_temp': random.randint(-5, 15),
        'max_temp': random.randint(20, 35)
    }

# Create wardrobe
wardrobe = []

# Add 5 tops
for top in random.sample(TOPS, 3):
    wardrobe.append(create_item('top', top))

# Add 4 bottoms
for bottom in random.sample(BOTTOMS, 3):
    wardrobe.append(create_item('bottom', bottom))

# Add 3 layers
for layer in random.sample(LAYERS, 3):
    wardrobe.append(create_item('layer', layer))

# Add 3 jackets
for jacket in random.sample(JACKETS, 3):
    wardrobe.append(create_item('jacket', jacket))

# Add 2 shoes
for shoe in random.sample(SHOES, 2):
    wardrobe.append(create_item('shoe', shoe))

print(f"Generated {len(wardrobe)} items")

# Save to CSV
with open('wardrobe_inventory.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['type', 'name', 'color', 'min_temp', 'max_temp'])
    writer.writeheader()
    writer.writerows(wardrobe)

print("Saved wardrobe_inventory.csv")

# Save to JSON
with open('wardrobe_inventory.json', 'w') as f:
    json.dump(wardrobe, f, indent=2)

print("Saved wardrobe_inventory.json")

# Show first 3 items
print("\nFirst 3 items:")
for item in wardrobe[:3]:
    print(f"  {item['color']} {item['name']} - Good for {item['min_temp']}°C to {item['max_temp']}°C")