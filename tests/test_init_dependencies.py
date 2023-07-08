import pytest
import logging
import os

### Initialise Configuration ###


def test_successful_imports(caplog):
    """Check the imports"""
    try:
        import requests
        import pytest
        import langchain
        import chromadb
        import openai
    except ImportError as err:
        logging.error("couldn't import a package: %s", err)

    for log in caplog.records:
        assert log.levelno < logging.ERROR


def test_environs_set(caplog):
    assert os.getenv("OPENAI_TOKEN") is not None


@pytest.mark.skip
def test_auto_skipped_test():
    """This is how you skip a test"""
    assert False
