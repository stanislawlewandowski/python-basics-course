hitsTitles = ['BROTHERS IN ARMS', 'BOHEMIAN RHAPSODY', 'STAIRWAY TO HEAVEN', 'RIDERS ON THE STORM',
              'WISH YOU WERE HERE']
hitsTitles.append('CHILD IN TIME')
hitsTitles.append('AGAIN')
hitsTitles.insert(2, 'HOTEL CALIFORNIA')
hitsTitles.insert(0, 'THE SOUND OF SILENCE')
print(hitsTitles)
print(hitsTitles.index('HOTEL CALIFORNIA'))
hitsTitles.remove('HOTEL CALIFORNIA')
hitsTitles[0] = 'ENJOY THE SILENCE'
hitsToRead = hitsTitles.copy()
hitsToRead.reverse()
hitsToRead.sort()
print(hitsToRead)
print(hitsTitles)
print(hitsToRead.pop(0))
print(hitsToRead)
additionalSongs = ['NOTHING COMPARES 2 U', 'WISH YOU WERE HERE']
hitsToRead.extend(additionalSongs)
print(hitsToRead)
print(hitsToRead.count('WISH YOU WERE HERE'))
hitsToRead.clear()
print(hitsToRead)