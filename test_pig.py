import pytest
import random
from pig import PlayerOne, PlayerTwo

def test_player_name():
    comp_player = PlayerOne('Regis', current_score=0)
    other_player = PlayerTwo('Matilde', current_score=0)
    assert comp_player.name == 'Regis'
    assert other_player.name == 'Matilde'
