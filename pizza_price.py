#!/usr/bin/env python3

def order_price(basic_price, quantity, is_tuesday, needs_delivery):

    if quantity == 0:
        raise ValueError("You must order at least one pizza")

    half_price_pizzas = quantity // 2 if is_tuesday else 0
    full_price_pizzas = quantity - half_price_pizzas

    total_price = (full_price_pizzas * basic_price) + (half_price_pizzas * (basic_price / 2))

    if needs_delivery:
        total_price += 2.5

    return total_price
