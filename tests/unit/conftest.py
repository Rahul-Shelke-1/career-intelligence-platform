import os

import pytest
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture
def get_env():
    return os.getenv("MY_VAR")
