# import pytest
from dogdoor import DogDoor


def test_dogdoor_is_closed_when_created():
    door = DogDoor()
    assert door.is_open() == False


def test_dogdoor_is_open_after_opening_it():
    door = DogDoor()
    door.open()
    assert door.is_open()


def test_dogdoor_is_closed_after_closing_it():
    door = DogDoor()
    door.open()
    assert door.is_open()
    door.close()
    assert door.is_open() == False
