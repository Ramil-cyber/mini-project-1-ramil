from src.main import greet

def test_greet():
    assert greet("Duke") == "Hello, Duke!"
    assert greet("Gunel") == "Hello, Gunel!"
