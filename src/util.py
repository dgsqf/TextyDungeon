from os import system, name

class bcolors:

    FAIL = '\033[91m'
    ENDC = '\033[0m'

def clear():
   # for windows
   if name == 'nt':
      _ = system('cls')

   # for mac and linux
   else:
      _ = system('clear')

class Story:
    def __init__(self,encounterdict,debug) -> None:
        self.inventory = []
        self.value = {}
        self.debug = debug
        self.encounter = encounter_from_dict(encounterdict,self)
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
    def __init__(self,text: str,encounter,story : Story,items,ritems,vchanges) -> None:
        self.text=text
        self.encounter=encounter
        self.items=items
        self.story=story
        self.ritems=ritems
        self.vchanges=vchanges
    def Choose(self):
        if self.encounter==None:
            print('End')
        else:
            if self.story.debug==False:
                clear()
            for it in self.items:
                self.story.inventory.append(it)
                        
            for rit in self.ritems:
                if rit in self.story.inventory:
                    
                    self.story.inventory.remove(rit)
                else:
                    if self.story.debug==True:
                        print(bcolors.FAIL+"couldn't remove item " +rit+" item inexistent")
                        print("there maybe a typo"+bcolors.ENDC)
            for c in self.vchanges:
                name = c["name"]
                sign = c["operation"]
                value= int(c["value"])
                if name not in self.story.value.keys():
                    self.story.value[name]=0
                if sign == "=":
                    self.story.value[name]=value
                elif sign == "+":
                    self.story.value[name]+=value
                elif sign == "*":
                    self.story.value[name]*=value
                elif sign == "-":
                    self.story.value[name]-=value
                elif sign == "/":
                    self.story.value[name]/=value

            
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
    actions=[Action(a["str"],encounter_from_dict(a["encounter"],story),story,a["items"],a["ritems"],a["vchanges"]) for a in actions]
    return Encounter(description=dict["description"],actions=actions,story=story)


