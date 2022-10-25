def shopping_cart(*args):
    limit = {"Soup": 3, "Pizza": 4, "Dessert": 2}
    cart = {"Soup": [], "Pizza": [], "Dessert": []}
    output = []
    empty = False
    for i in range(len(args)):
        if args[i] == "Stop":
            for key, value in cart.items():
                value.sort()
            cart = {x: y for x, y in sorted(cart.items(), key=lambda x: (-len(x[1]), x[0]))}
            if not cart["Soup"] and not cart["Pizza"] and not cart["Dessert"]:
                return "No products in the cart!"
            for k, v in cart.items():
                output.append(f'{k}:')
                for item in v:
                    output.append(f' - {item}')
            return "\n".join(output)
        meal, ingredient = args[i][0], args[i][1]
        if len(cart[meal]) < limit[meal] and ingredient not in cart[meal]:
            cart[meal].append(ingredient)
    if not cart["Soup"] and not cart["Pizza"] and not cart["Dessert"]:
        return "No products in the cart!"
    for key, value in cart.items():
        value.sort()
    cart = {x: y for x, y in sorted(cart.items(), key=lambda x: (-len(x[1]), x[0]))}

    for k, v in cart.items():
        output.append(f'{k}:')
        for item in v:
            output.append(f' - {item}')
    return "\n".join(output)