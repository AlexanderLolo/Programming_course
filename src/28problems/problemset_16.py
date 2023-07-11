def MaximumDiscount(N: int, price: list) -> int:

    price.sort(reverse=True)
    return sum(price[2::3])
