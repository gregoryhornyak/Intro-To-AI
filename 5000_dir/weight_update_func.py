from settingsControl import*

# new_w = old_w + learn_rate * (top-op) * ( hn or i)
def weightUpdate(old_w,top,op,input):
    learning_rate = UseSettings("Learning_Rate")
    return (old_w + learning_rate*(top-op)*input)

