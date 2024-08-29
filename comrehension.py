letters = []

for letter in 'human':
    letters.append(letter)
    print(letters)

# using comphersion
letters = [letter for letter in 'human']
print(letters)

# list comphesion vs lambda function
letters = list(map(lambda x:x, 'human'))
print(letters)

# if list with comphersion
list = [ x for x in range (20)  if x%2 == 0]
print(list)

