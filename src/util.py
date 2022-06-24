from os import system, name
from time import sleep
def clear():
   # for windows
   if name == 'nt':
      _ = system('cls')

   # for mac and linux
   else:
      _ = system('clear')


class Action:
    def __init__(self,text: str,encounter) -> None:
        self.text=text
        self.encounter=encounter
    def Choose(self):
        if self.encounter==None:
            print('End')
        else:
            clear()
            self.encounter.Render()

class Encounter:
    def __init__(self,description: str,actions: list[Action]) -> None:
        self.description=description
        self.actions=actions
    
    def Render(self):
        print(self.description)
        print("\n\n")
        for a in self.actions:
            print(str(self.actions.index(a)+1)+':'+a.text)
        choice=input('>')
        choice=int(choice)
        self.actions[choice-1].Choose()

def encounter_from_dict(dict : dict):
    if dict==None:
        return None
    actions=dict["actions"]
    actions=[Action(a["str"],encounter_from_dict(a["encounter"])) for a in actions]
    return Encounter(description=dict["description"],actions=actions)



