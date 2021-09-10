
#Part 3 Assignment 2
file = open('demo.txt', 'w')
file.write('This is Assignment 2 text file')
file.close()

file = open('demo.txt', 'r')
content = file.read()
print(content)
file.close()

file = open('demo.txt', 'a')
file.write('\n This is the appended text.')
file.close()