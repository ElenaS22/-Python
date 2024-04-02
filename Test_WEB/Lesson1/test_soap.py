import pytest
from client_soap import check_text
import yaml

def test_soap(good_word, bad_word):
   assert good_word in check_text(bad_word), 'fail'
    #assert True

if __name__ == '__main__':
    pytest.main(['-vv'])
   # print(check_text('королество'))