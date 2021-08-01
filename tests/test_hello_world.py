import pytest
from project_name.main import hello_world


@pytest.mark.parametrize("x", ['Niko', 'Yang Weining'])
def test_hello_world(x):
    assert isinstance(hello_world(x), str)
