import time

import pytest
from dogdoor import DogDoor
from remote import Remote


@pytest.mark.skip
def test_if_door_is_closed_when_button_pressed_then_door_should_open():
    door = DogDoor()
    remote = Remote(door)
    assert door.is_open() == False
    remote.press_button()
    assert door.is_open()


def test_if_door_is_open_when_button_pressed_then_door_should_close():
    door = DogDoor()
    remote = Remote(door)
    door.open()
    assert door.is_open()
    remote.press_button()
    assert door.is_open() == False


def test_when_door_is_opened_it_automatically_closes_after_2_seconds():
    door = DogDoor()
    remote = Remote(door)
    assert door.is_open() == False
    remote.press_button()
    # assert door.is_open()
    time.sleep(3)
    assert door.is_open() == False
