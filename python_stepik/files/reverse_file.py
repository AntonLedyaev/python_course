

with open('dataset_24465_4.txt') as file:
    file_lines = file.read().splitlines()

with open('reversed.txt', 'w') as revers:
    for line in file_lines[::-1]:
        revers.write('%s\n' % line)
