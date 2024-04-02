import pytest

from client_soap import check_text

@pytest.fixture()
def good_word():
   return 'Королевство'

@pytest.fixture()
def bad_word():
   return 'Королество'
