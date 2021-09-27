class EventHandler:

    def __init__(self, return_func):
        self.return_func = return_func

    def on_event(self, data: dict, topic: str):
        self.return_func(data)
