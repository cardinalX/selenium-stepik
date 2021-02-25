import pytest
pytestmark = pytest.mark.skipif(...)
xfail = pytest.mark.xfail

@xfail(strict=True)
def test_succeed():
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False


def test_many_assert():
    assert True
    assert True
