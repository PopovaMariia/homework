var_string = input()
counting_vowels = 0
for i in str.lower(var_string):
    if i in 'aoieu':
        counting_vowels += 1
print('Number of vowels: ', counting_vowels)