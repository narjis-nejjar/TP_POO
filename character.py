import logging
import random 

log = logging.getLogger(__name__)


class CharacterError(Exception):
    """Base class for Character error"""
    pass


class Character:
    
    def __init__(self, name: str):
        self._name = name
        self._life = 100.0
        self._attack = 20.0
        self._defense = 0.10

    
    @property
    def name(self):
        return self._name

    @property
    def is_dead(self):
        return self._life <= 0
    
    def attack(self, target: "Character"):
        if self.is_dead:
            return     # Un personnage mort n'attaque pas
        damage = self._attack
        target.take_damages(damage)

    def take_damages(self, damage_value: float):
        effective_damage = damage_value * (1 - self._defense)
        self._life -= effective_damage
        if self._life < 0:
            self._life = 0

    def __str__(self):
        return f"{self._name} <{self._life:.3f}>"
    

    

class Weapon:

    def __init__(self, name: str, attack_value: float):
        self._name = name
        self._attack_value = attack_value

    @property
    def attack_value(self) -> float:
        return self._attack_value

    def __str__(self):
        return f"{self._name} (+{self._attack_value} ATK)"

    @classmethod
    def default(cls):
        return cls("Wood stick", 1.0)



class Warrior:

    def __init__(self, name: str, weapon: Weapon = None):
        super().__init__(name)
        self._life = 150.0  # 1.5 * 100
        self._defense = 0.12  # 1.2 * 0.10
        self._base_life = self._life
        self.weapon = weapon if weapon else Weapon.default()
    
    @property

    def is_raging(self):
        return self._life < 0.2 * self._base_life

    def attack(self, target: 'Character'):
        total_attack = self._attack + self.weapon.attack
        if self.is_raging:
            total_attack *= 1.2
        if not self.is_dead:
            target.take_damages(total_attack)



class Magician:

    def __init__(self, name: str):
        super().__init__(name)
        self._life = 80.0  # 0.8 * 100
        self._attack = 40.0  # 2 * 20
