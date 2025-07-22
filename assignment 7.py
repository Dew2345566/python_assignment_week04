children = [ [ {"name": "Alice", "age": 2, "height": 95}, {"name": "Bob", "age": 4, "height": 105}, {"name": "Charlie", "age": 3, "height": 110}, {"name": "David", "age": 5, "height": 102}, {"name": "Eve", "age": 6, "height": 99} ]]

eligible_children = [child for child in children[0] if child["age"] >= 3 and child["height"] >= 100]

print("Eligible children for the ride:", eligible_children)