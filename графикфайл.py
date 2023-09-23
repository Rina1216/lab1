file = open('sequence.txt', 'r')
list = []
for i in file:
    list.append(float(i))
file.close()
positive = 0
negative = 0
counter = len(list)
for i in list:
    if i > 0:
        positive += 1
    else:
        negative += 1
procentp = positive/counter * 100
procentn = negative/counter * 100
step = round(abs(procentp - procentn),2)
p = int(100/step)
for i in range(p, -1, -1):
    line = str(round(step*i,2))
    if round(step*i,2) == 100:
        line += ' '
    elif round(step*i,2) >= 10:
        line += '  '
    elif round(step*i,2) == 0:
        line += '   '
    else:
        line += '   '
    if procentp >= round(step*i,2):
        line += '!!'
    else:
        line += '--'
    line += '--'
    if procentn >= round(step*i,2):
        line += '!!'
    else:
        line += '--'
    print(line)
print('      >0  <0')
