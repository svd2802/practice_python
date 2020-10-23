from __future__ import annotations
import sys
sys.path.append('C:/Users/narut/practice_python/war')
from exceptions import NotRealizedMethodError


class Weapon:
    def __init__(self, name='Stick', damage=1):
        self._name = name
        self._damage = damage

    @property
    def name(self):
        return self._name

    @property
    def damage(self):
        raise NotRealizedMethodError()

    @damage.setter
    def damage(self, value):
        raise NotRealizedMethodError()

    def attack(self, target):
        raise NotRealizedMethodError()

    def __le__(self, other: Weapon):
        if self.damage >= other.damage:
            return self
        else:
            return other

    def __str__(self):
        return "Название: " + str(self.name) + "; Урон: " + str(self.damage)
