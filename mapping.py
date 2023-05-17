import numpy as np
from copy import deepcopy


# getNewAction changes the current switching state and returns the corresponing action number of the gem environment to apply the new action.
def getNewAction(self,act_,halfbridge):
    act = deepcopy(self.subactions[act_])
    if act[halfbridge] == -1:
        act[halfbridge] = 1
    elif act[halfbridge] == 1:
        act[halfbridge] = -1
    else:
        raise NotImplementedError
    
    for idx in np.arange(0, len(self.subactions), 1):
        if np.array_equal(self.subactions[idx],act):
            return idx


# function to map the action of the DQ-DTC-RCS to the corresponing volteage vector of the inverter
def mapAction(self, action):
    if action == 0:
        return self.old_action
    elif action == 1:
        return getNewAction(self,self.old_action,0)
    elif action == 2:
        return getNewAction(self,self.old_action,1)
    elif action == 3:
        return getNewAction(self,self.old_action,2)
    else:
        raise NotImplementedError

    