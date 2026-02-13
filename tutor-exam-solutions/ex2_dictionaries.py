def buyable(drinks: dict[str, tuple[set[str], float]], money: float) -> set[str]:
    ret = set()
    for cocktail, (_, mon) in drinks.items():
        if mon <= money:
            ret.add(cocktail)
    return ret


def invert(drinks: dict[str, tuple[set[str], float]]) -> dict[str, set[str]]:
    ret: dict[str, set[str]] = dict()
    for cocktail, (ingredients, _) in drinks.items():
        for ingred in ingredients:
            ret.setdefault(ingred, set()).add(cocktail)
    return ret


def buyable_allergic(drinks: dict[str, tuple[set[str], float]], money: float, allergic: set[str]) -> set[str]:
    ret = buyable(drinks, money)
    inv = invert(drinks)
    for x in allergic:
        ret = set(filter(lambda s: s not in inv[x], ret))
    return ret


if __name__ == "__main__":
    drinks = {
        "Daiquiri": ({"Rum", "Limette", "Zucker"}, 7.90),
        "Mojito": ({"Rum", "Limette", "Zucker", "Minze", "Soda"}, 7.50),
        "Whiskey Sour": ({"Whiskey", "Zitrone", "Zucker"}, 8.90),
        "Tequila Sour": ({"Tequila", "Zitrone", "Zucker"}, 6.50),
        "Moscow Mule": ({"Vodka", "Limette", "Ginger ale"}, 7.00),
    }

    assert buyable(drinks, 5.00) == set()
    assert buyable(drinks, 7) == {"Tequila Sour", "Moscow Mule"}

    assert invert(drinks) == {'Zucker': {'Whiskey Sour', 'Daiquiri', 'Mojito', 'Tequila Sour'}, 'Rum': {'Daiquiri', 'Mojito'}, 'Limette': {'Daiquiri', 'Moscow Mule', 'Mojito'}, 'Soda': {
        'Mojito'}, 'Minze': {'Mojito'}, 'Zitrone': {'Whiskey Sour', 'Tequila Sour'}, 'Whiskey': {'Whiskey Sour'}, 'Tequila': {'Tequila Sour'}, 'Vodka': {'Moscow Mule'}, 'Ginger ale': {'Moscow Mule'}}

    assert buyable_allergic(drinks, 5.00, {"Limette"}) == set()
    assert buyable_allergic(drinks, 7.00, {"Limette"}) == {"Tequila Sour"}
