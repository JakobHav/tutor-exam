# Ex4: Datenklassen (15P)

from dataclasses import dataclass, field
from enum import IntEnum


if __name__ == "__main__":
    charmander = FirePokemon("Charmander", 90, 52)
    bulbasaur = Pokemon("Bulbasaur", 100, 49, PokemonType.Erde)
    charmander.fire_attack(bulbasaur)
    assert bulbasaur.hp == 22  # 100 - int(52 * 1.5) = 100 - 78 = 22
    charmander.fire_attack(bulbasaur)
    assert not bulbasaur.is_alive()
