# Ex2: Dictionaries und Sets (15P)

def buyable(drinks, money):
    ...


def invert(drinks):
    ...


def buyable_allergic(drinks, money, allergic):
    ...


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

    assert invert(drinks) == {'Zucker': {'Whiskey Sour', 'Daiquiri', 'Mojito', 'Tequila Sour'}, 'Rum': {'Daiquiri', 'Mojito'}, 'Limette': {'Daiquiri', 'Moscow Mule', 'Mojito'}, 'Soda': {'Mojito'}, 'Minze': {'Mojito'}, 'Zitrone': {'Whiskey Sour', 'Tequila Sour'}, 'Whiskey': {'Whiskey Sour'}, 'Tequila': {'Tequila Sour'}, 'Vodka': {'Moscow Mule'}, 'Ginger ale': {'Moscow Mule'}}

    assert buyable_allergic(drinks, 5.00, {"Limette"}) == set()
    assert buyable_allergic(drinks, 7.00, {"Limette"}) == {"Tequila Sour"}
