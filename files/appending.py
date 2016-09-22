file = open('wastland.txt', mode='at')

file.writelines(['appending just one line'])

file.close()

print('done')