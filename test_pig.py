import pytest
import random
from pig import ComputerPerson, PersonPerson, Game

regis_comp = ComputerPerson('Regis', current_score=0)
matilde_person = PersonPerson('Matilde', current_score=0)
Game(regis_comp, matilde_person, None)

def test_player_name():
    assert regis_comp.name == 'Regis'
    assert matilde_person.name == 'Matilde'

def test_comp_choose():
    assert regis_comp.choose == 'HOLD' or 'ROLL'

def test_roll_die():
    assert regis_comp.roll_die() in range(1, 6)
    assert matilde_person.roll_die() in range (1, 6)