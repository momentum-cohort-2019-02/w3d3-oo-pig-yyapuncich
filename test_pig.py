import pytest
import random
from pig import ComputerPerson, PersonPerson

comp_player = ComputerPerson('Regis', current_score=0)
other_player = PersonPerson('Matilde', current_score=0)

def test_player_name():
    assert comp_player.name == 'Regis'
    assert other_player.name == 'Matilde'

def test_comp_choose():
    comp_player.choose == 'HOLD' or 'ROLL'