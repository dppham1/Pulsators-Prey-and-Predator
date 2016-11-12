import controller, sys
import model   #strange, but we need a reference to this module to pass this module to update

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from special   import Special


oset = set()
isrunning = False
ckind = None
cycle_count = 0


def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())


def reset ():
    global oset, isrunning, cycle_count
    oset, isrunning, cycle_count = set(), False, 0


def start ():
    global isrunning
    isrunning = True


def stop ():
    global isrunning
    isrunning = False


def step ():
    global isrunning, cycle_count
    isrunning = False
    cycle_count += 1
    for i in set(oset):
        i.update(model)

 
def select_object(kind):
    global ckind
    ckind = kind


def mouse_click(x,y):
    if ckind == 'Remove':
        for sims in set(oset):
            if sims.contains((x,y)):
                remove(sims)
    elif ckind is None:
        pass
    else:
        add(eval('{}({},{})'.format(ckind,x,y)))
        

def add(s):
    global oset
    oset.add(s)
    
   
def remove(s):
    global oset
    oset.remove(s)
    
   
def find(p):
    rset = set()
    for sims in oset:
        if p(sims):
            rset.add(sims)
    return rset


def update_all():
    global cycle_count
    if isrunning:
        cycle_count += 1
        for sims in set(oset):
            sims.update(model)


def display_all():
    for sims in controller.the_canvas.find_all():
        controller.the_canvas.delete(sims)
        
    for sims in oset:
        sims.display(controller.the_canvas)

    controller.the_progress.config(text=str(len(oset))+" objects/"+str(cycle_count)+" cycles")



