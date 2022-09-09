from gbuilder import GBuilder
from gtype import GType
from guitarspec import GuitarSpec
from gwood import GWood
import pytest

from gwood import GWood


def test_gspec_is_equal_good_match():
    gspec = GuitarSpec(GBuilder.FENDER, 'stratocaster', GType.ELECTRIC, 6, GWood.ALDER, GWood.ALDER)
    other = GuitarSpec(GBuilder.FENDER, 'stratocaster', GType.ELECTRIC, 6, GWood.ALDER, GWood.ALDER)
    assert gspec.is_equal(other) == True

def test_gspec_is_equal_fails_diff_builder():
    gspec = GuitarSpec(GBuilder.FENDER, 'stratocaster', GType.ELECTRIC, 6, GWood.ALDER, GWood.ALDER)
    nomatch = GuitarSpec(GBuilder.GIBSON, 'stratocaster', GType.ELECTRIC, 6, GWood.ALDER, GWood.ALDER)
    assert gspec.is_equal(nomatch) == False

def test_gspec_is_equal_fails_diff_model():
    gspec = GuitarSpec(GBuilder.FENDER, 'stratocaster', GType.ELECTRIC, 6, GWood.ALDER, GWood.ALDER)
    nomatch = GuitarSpec(GBuilder.FENDER, 'Les Paul', GType.ELECTRIC, 6, GWood.ALDER, GWood.ALDER)
    assert gspec.is_equal(nomatch) == False

def test_gspec_is_equal_fails_diff_type():
    gspec = GuitarSpec(GBuilder.FENDER, 'stratocaster', GType.ELECTRIC, 6, GWood.ALDER, GWood.ALDER)
    nomatch = GuitarSpec(GBuilder.FENDER, 'stratocaster', GType.ACOUSTIC, 6, GWood.ALDER, GWood.ALDER)
    assert gspec.is_equal(nomatch) == False

def test_gspec_is_equal_fails_diff_top_wood():
    gspec = GuitarSpec(GBuilder.FENDER, 'stratocaster', GType.ELECTRIC, 6, GWood.ALDER, GWood.ALDER)
    nomatch = GuitarSpec(GBuilder.FENDER, 'stratocaster', GType.ELECTRIC, 6, GWood.ADIRONDACK, GWood.ALDER)
    assert gspec.is_equal(nomatch) == False

def test_gspec_is_equal_fails_diff_back_wood():
    gspec = GuitarSpec(GBuilder.FENDER, 'stratocaster', GType.ELECTRIC, 6, GWood.ALDER, GWood.ALDER)
    nomatch = GuitarSpec(GBuilder.FENDER, 'stratocaster', GType.ELECTRIC, 6, GWood.ALDER, GWood.MAHOGONEY)
    assert gspec.is_equal(nomatch) == False
