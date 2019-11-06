#from .context import testbed
import testbed
from testbed import simple_func

def test_instantiate():
    t = testbed.TestBed()
    assert t

def test_state():
    t = testbed.TestBed()
    state = t.state
    assert state
    assert type(state) == str
    assert state == 'init'

def test_func():
    result = simple_func()
    assert result == 'Ni!'
