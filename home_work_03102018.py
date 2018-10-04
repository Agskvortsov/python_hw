import collections
import pytest

items = [1, 2, [3, 4, [5, 6], 7], 8]

def flatten(l):
    for el in l:
        if isinstance(el, collections.Iterable):
            for sub in flatten(el):
                yield sub
        else:
            yield el



def test_flatten():
    assert list(flatten([1, 2, [3, 4, [5, 6], 7], 8])) == [1, 2, 3, 4, 5, 6, 7, 8]

def test_flatten_is_list():
    assert list(flatten([1, 2, [3, 4, [5, 6], 7], 8]))

def test_flatten_elem_is_int():
    for elem in flatten([1, 2, [3, 4, [5, 6], 7], 8]):
        assert type(elem) == int


@pytest.mark.parametrize("items, expected",
                         [([1, 2, [3, 4, [5, 6], 7], 8], [1, 2, 3, 4, 5, 6, 7, 8]),
                          ([1, 2, [3, 4, [5,[2,7], 6], 7], 8], [1, 2, 3, 4, 5, 2, 7,  6, 7, 8])])

def test_flatten_parametrize(items, expected):
    assert list(flatten(items)) == expected


