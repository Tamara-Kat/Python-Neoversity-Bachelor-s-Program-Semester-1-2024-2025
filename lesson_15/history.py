"""
>>> d = HistoryDict({"foo": 42})
>>> d.set_value("bar", 43)
>>> d.get_history()
["bar"]
>>> d.set_value("foo", 44)
>>> d.get_history()
["bar", "foo"]
"""


class HistoryDict:
    def __init__(self, initial_data=None, max_length=5):
        self.data = {}
        self.history = []
        self.max_history = max_length
        if initial_data:
            self.data = initial_data

    def get_history(self):
        return self.history
    
    def get_value(self, key):
        return self.data.get(key)

    def set_value(self, key, value):
        self.data[key] = value
        if len(self.history) >= self.max_history:
            self.history.pop(0)
        self.history.append(key)

d = HistoryDict({"foo": 42})
d.set_value("bar", 43)
print(d.get_history())
d.set_value("foo", 44)
print(d.get_history())
d.set_value("foo", 45)
print(d.get_history())