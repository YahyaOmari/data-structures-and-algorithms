from challenges.hashtable.hashtable import *
import pytest

@pytest.fixture
def hashtable():
    test_hash = Hashtable()
    test_hash.add('yahya', '23')
    test_hash.add('there', 95)
    test_hash.add('there', 127)
    return test_hash

def test_hash(hashtable):
    assert hashtable._buckets[hashtable.hash('yahya')].head.value == '23'
    assert hashtable.hash('united') == 389


def test_add(hashtable):
    hashtable.add('go','play football')
    assert hashtable._buckets[hashtable.hash('go')].head.value == 'play football'

def test_contains(hashtable):
    assert hashtable.contains('yahya') == True
    assert hashtable.contains('anything') == False

def test_get(hashtable):
    assert hashtable.get('yahya') == '23'

def test_collision(hashtable):
    assert hashtable._buckets[hashtable.hash('there')].head.value == 127
    assert hashtable._buckets[hashtable.hash('there')].head.next.value == 95
    assert hashtable.get('there') == 127
