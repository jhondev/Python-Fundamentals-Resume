#w=write, t=text
f = open('wastland.txt', mode='wt')

f.write('testing')
f.write('a test in another line')

f.close()

print('done')