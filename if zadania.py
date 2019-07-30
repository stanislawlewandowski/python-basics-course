musclePain = False
fever = False
weakness = True
isMan = False
if musclePain and fever and weakness:
    print('suspiction of influenza')
else:
    print('The flu is unlikely')
if weakness and not(fever and musclePain):
    print('Just take a rest!')
else:
    print('you may be cold')
if musclePain and fever and weakness:
    print("suspicion of influenza")
elif weakness and not (musclePain and fever):
    print("Just take a rest!")
else:
    print("you may be cold")

if musclePain and fever and weakness or isMan and (musclePain or fever or weakness):
    print("suspicion of influenza")
elif weakness and not (musclePain and fever):
    print("Just take a rest!")
else:
    print("you may be cold")

