import pytest
from dotenv import load_dotenv
import os

load_dotenv()

@pytest.fixture
def get_env():
    return os.getenv("MY_VAR")
