from email.policy import default
from os import system, name
import re
from collections import namedtuple
c = namedtuple('colors', ['FAIL', 'ENDC'], defaults=[
    '\033[91m', '\033[0m'])

colors = c()


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux
    else:
        _ = system('clear')


class Story:
    def __init__(self, encounterdict, debug) -> None:
        self.inventory = []
        self.value = {}
        self.debug = debug
        self.encounter = encounter_from_dict(encounterdict, self)

    def render_inventory(self):
        print("Inventory")
        print("-------------------------------------------")
        for i in self.inventory:
            print(i)
        print("-------------------------------------------")
        if self.debug == True:
            print("Values")
        print("-------------------------------------------")

        print(self.value)
        print("-------------------------------------------")

    def start(self):
        self.encounter.Render()


class Action:
    def __init__(self, text: str, encounter, story: Story, items, ritems, vchanges, iconditions) -> None:
        self.text = text
        self.encounter = encounter
        self.items = items
        self.story = story
        self.ritems = ritems
        self.vchanges = vchanges
        self.iconditions = iconditions

    def Choose(self):
        if not self.encounter:
            print('End')
        else:
            if not self.story.debug:
                clear()
            for it in self.items:
                self.story.inventory.append(it)

            for rit in self.ritems:
                if rit in self.story.inventory:

                    self.story.inventory.remove(rit)
                else:
                    if self.story.debug:
                        print(colors.FAIL+"couldn't remove item " +
                              rit+" item inexistent")
                        print("there maybe a typo"+colors.ENDC)
            for c in self.vchanges:
                name = c["name"]
                sign = c["operation"]
                value = int(c["value"])
                if name not in self.story.value.keys():
                    self.story.value[name] = 0
                if sign == "=":
                    self.story.value[name] = value
                elif sign == "+":
                    self.story.value[name] += value
                elif sign == "*":
                    self.story.value[name] *= value
                elif sign == "-":
                    self.story.value[name] -= value
                elif sign == "/":
                    self.story.value[name] /= value

            self.encounter.Render()


class Encounter:
    def __init__(self, description: str, actions, story: Story) -> None:
        self.description = description
        self.actions = actions
        self.story = story

    def Render(self):
        self.story.render_inventory()
        print(self.description)
        print("\n\n")
        pactions = []
        for a in self.actions:
            if a.iconditions == "":
                pactions.append(a)
                continue

            condition = a.iconditions

            for r in list(self.story.value.keys()):

                condition = condition.replace('$'+r, str(self.story.value[r]))

            if eval(condition.replace("__", ""), {"__builtins__": None}, {"inventory": self.story.inventory}):
                pactions.append(a)

        if not pactions:
            print("END")
        else:
            for pa in pactions:
                print(str(pactions.index(pa)+1)+':'+pa.text)

            choice = input('>')
            choice = int(choice)
            pactions[choice-1].Choose()


def encounter_from_dict(dict: dict, story: Story):
    if not dict:
        return None
    actions = dict["actions"]
    actions = [Action(a["description"], encounter_from_dict(a["encounter"], story), story,
                      a["additems"], a["removeitems"], a["valuechanges"], a["conditions"]) for a in actions]
    return Encounter(description=dict["description"], actions=actions, story=story)
