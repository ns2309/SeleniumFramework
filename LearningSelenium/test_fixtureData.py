import pytest

from pytestDemo.conftest import dataLoad


@pytest.mark.usefixtures("dataLoad")
class TestExample2:

    def test_editprofile(self, dataLoad):
        print(dataLoad)