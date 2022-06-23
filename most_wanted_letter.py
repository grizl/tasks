def most_wanted_letter(string):
    letters = [i for i in string.lower() if i.isalpha()]
    if len(letters) != 0:
        counted = dict((x,letters.count(x)) for x in set(letters))
        maxL = max(counted, key=counted.get)
        return f'The most popular letter is {maxL}'
    else:
        return f'There are no letters in the string.'

print(most_wanted_letter('......HeLlo......'))
print(most_wanted_letter('String ssss ttAAds TTTTTTT'))
print(most_wanted_letter('!@#$%^&*(*&^%$#@@#$%^&*DFGBQQQQQQQQqqqrrrrrrrr'))
print(most_wanted_letter('!@#$%^&*543234%^&*%$#@345677^%$#@#$%^&'))
print(most_wanted_letter('....пррррривет...'))
print(most_wanted_letter('....Tschüüüüüüüss!...'))
