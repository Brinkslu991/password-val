# Lucas Brinks
# 12/13/24
# Password checker

password = input('Type your password: ')
score = 0
uppercase = False
lowercase = False
number = False
punctuation = False
for character in password:
    if character in 'abcdefghijklmnopqrstuvwxyz':
        lowercase = True
    elif character in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        uppercase = True
    elif character in '0123456789':
        number = True
    else:
        punctuation = True

if lowercase == True:
    print('Your password contains at least one lowercase character.')
if uppercase == True:
    print('Your password contains at least in uppercase character.')
if number == True:
    print('Your password contains at least one number.')
if punctuation == True:
    print('Your password contains at least one punctuation sign.')

if lowercase==True and uppercase==True:
    score += 10
if number==True and (lowercase==True and uppercase==True):
    score += 10
if punctuation == True:
    score += 5
if len(password) >= 8:
    score += 5
    print('Your password is at least 8 characters long.')
print('Score: ' + str(score))