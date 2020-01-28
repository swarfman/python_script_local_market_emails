import fileinput

#REMOVE END OF LINE BREAKS
with fileinput.FileInput('MarketEmail.txt', inplace=True) as file:
    for line in file:
        print(line.replace('</b>',' '), end='')

#REMOVE BACK TO BACK BREAKS
with fileinput.FileInput('MarketEmail.txt', inplace=True) as file:
    for line in file:
        print(line.replace('<br><br>',' '), end='')

#REMOVE ORPHAN BREAKS    
with fileinput.FileInput('MarketEmail.txt', inplace=True) as file:
    for line in file:
        print(line.replace('<br>',' '), end='')

#REMOVE NEW LINE BREAKS AND SAVE BACK-UP FILE
with fileinput.FileInput('MarketEmail.txt', inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace('/n',' '), end='')