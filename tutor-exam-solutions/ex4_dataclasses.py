from dataclasses import dataclass, field
from enum import IntEnum


class PokemonType(IntEnum):
    Feuer = 1
    Wasser = 2
    Luft = 3
    Erde = 4


@dataclass
class Pokemon:
    name: str
    hp: int
    attack: int
    pokemon_type: PokemonType

    def __post_init__(self) -> None:
        assert self.name
        assert self.hp > 0
        assert self.attack > 0
        assert self.pokemon_type

    def take_damage(self, damage: int) -> None:
        self.hp = max(0, self.hp - damage)

    def is_alive(self) -> bool:
        return self.hp > 0


@dataclass
class WaterPokemon (Pokemon):
    pokemon_type: PokemonType = field(init=False, default=PokemonType.Wasser)
    max_hp: int = field(init=False)

    def __post_init__(self) -> None:
        super().__post_init__()
        self.max_hp = self.hp

    def heal(self, damage: int) -> None:
        self.hp += damage

        self.hp = min(self.max_hp, self.hp)


@dataclass
class FirePokemon (Pokemon):
    pokemon_type: PokemonType = field(init=False, default=PokemonType.Feuer)

    def fire_attack(self, opponent: Pokemon) -> None:
        opponent.take_damage(int(self.attack * 1.5))


if __name__ == "__main__":
    charmander = FirePokemon("Charmander", 90, 52)
    bulbasaur = Pokemon("Bulbasaur", 100, 49, PokemonType.Erde)
    charmander.fire_attack(bulbasaur)
    assert bulbasaur.hp == 22  # 100 - int(52 * 1.5) = 100 - 78 = 22
    charmander.fire_attack(bulbasaur)
    assert not bulbasaur.is_alive()
