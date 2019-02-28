import pytest
import random
from pig import ComputerPerson, PersonPerson

def test_player_name():
    comp_player = ComputerPerson('Regis', current_score=0)
    other_player = PersonPerson('Matilde', current_score=0)
    assert comp_player.name == 'Regis'
    assert other_player.name == 'Matilde'


