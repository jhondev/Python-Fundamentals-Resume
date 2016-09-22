file = open('wastland.txt', mode='rt')
print(file.readline())

file2 = open('wastland.txt', mode='rt')
file_lines = file2.readlines()

print('printing lines...')
for line in file_lines:
    print(line)

file.close()
file2.close()

print('done')