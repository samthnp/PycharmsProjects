def suggest(product_idea):
    if len(product_idea) < 3:
        raise ValueError
    else:
        return product_idea + "inator"

