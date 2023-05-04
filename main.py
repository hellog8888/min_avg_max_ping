from math import ceil
import glob

file = glob.glob('*.txt')

with open(file[0], 'r', encoding='UTF-8') as read_file:

    count_line = 0
    lst = []

    for line in read_file.readlines():
        if count_line > 1:
            lst.append(int(''.join(line.strip().split()[5:-1]).split('=')[-1].strip('мс')))
        count_line += 1

    sort_lst = sorted(lst)
    print(sort_lst[0], ceil(sum(sort_lst) / len(sort_lst)), sort_lst[-1])