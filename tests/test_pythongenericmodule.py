from pythongenericmodule import __version__
from pythongenericmodule.eventhandler.EventHandler import EventHandler


def test_version():
    assert __version__ == "0.1.0"


def test_eventHandler_return_type():
    def return_func(data: dict):
        assert type(data) == dict
    eventHandler = EventHandler(return_func=return_func)
    eventHandler.on_event({})
