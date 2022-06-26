from os import system, name
from time import sleep
def clear():
   # for windows
   if name == 'nt':
      _ = system('cls')

   # for mac and linux
   else:
      _ = system('clear')

class Story:
    def __init__(self,encounterdict) -> None:
        self.inventory = ["Aurevoir"]
        self.value = {}
        self.encounter = encounter_from_dict(encounterdict,self)
    def render_inventory(self):
        print("Inventory")
        print("-------------------------------------------")
        for i in self.inventory:
            print(i)
        print("-------------------------------------------")
    def start(self):
        self.encounter.Render()
         
class Action:
    def __init__(self,text: str,encounter,story : Story,items,ritems) -> None:
        self.text=text
        self.encounter=encounter
        self.items=items
        self.story=story
        self.ritems=ritems
    def Choose(self):
        if self.encounter==None:
            print('End')
        else:
            clear()
            for it in self.items:
                self.story.inventory.append(it)
                        
            for rit in self.ritems:
                if rit in self.story.inventory:
                    self.story.inventory.remove(rit)
            self.encounter.Render()

class Encounter:
    def __init__(self,description: str,actions,story : Story) -> None:
        self.description=description
        self.actions=actions
        self.story = story
    def Render(self):
        self.story.render_inventory()
        print(self.description)
        print("\n\n")
        for a in self.actions:
            print(str(self.actions.index(a)+1)+':'+a.text)
        choice=input('>')
        choice=int(choice)
        self.actions[choice-1].Choose()

def encounter_from_dict(dict : dict,story : Story):
    if dict==None:
        return None
    actions=dict["actions"]
    actions=[Action(a["str"],encounter_from_dict(a["encounter"],story),story,a["items"],a["ritems"]) for a in actions]
    return Encounter(description=dict["description"],actions=actions,story=story)



