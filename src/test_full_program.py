
import json
import util


def startgame():
    try:
        with open("test.json", "r") as f:
            dict = json.load(f)
        story = util.Story(dict, False)
        story.start()
        return story
    except FileNotFoundError:
        print("file not found error please enter in an existing file")


class TestClass:
    def test_end_to_end(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "1")
        try:
            startgame()
        except:
            pass

    def test_values(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "1")
        story = startgame()
        assert story.value == {'=': 10, '+': 10, '-': -10, '*': 0, '/': 0.0}
