result = [0 for i in range(10)]
plot_list = [[0 for i in range (10)] for i in range (10)]
for i in range(10):
    result[i] = i ** 2
step = round(abs(result[0] - result[9]) / 9, 2)
for i in range(10):
    for j in range (10):
        if j == 0:
            plot_list[i][j] = step * (8-i) + step

for i in range(10):
    for j in range (10):
        if abs(plot_list[i][0] - result[9-j]) < step:
            for k in range(9):
                if 8-k == j:
                    plot_list[i][k+1] = 1

for i in range(9):
    line = ''
    for j in range(10):
        if j == 0:
            line += str(plot_list[i][j]) + '\t'
        if plot_list[i][j] == 0:
            line += '--'
        if plot_list[i][j] == 1:
            line += '!!'
    print(line)