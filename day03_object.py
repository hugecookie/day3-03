5-1
song = """when an ell grabs your arm, and it causes great harm, That's - a moray!"""
part = []
for word in song.split():
    if word.startswith('m'):
        part.append(word)
# print(str(part).upper())

5-2
qst = [
    "first quesiton",
    "second question",
    "third question"
]
ans = [
    "first answer",
    "second answer",
    "third answer",
]
# for i in range(0, 3, 1):
#     print(f'Q: {qst[i]} \nA: {ans[i]}')

5-3
# print(" My kitty cat like %s,\n My kitty cat likes %s,\n My kitty cat fell on his %s and now think he's a %s"
#       % ('roast beef', 'ham', 'head', 'claim'))

5-4


letter = '''Dear {salutation} {name}, 
         Thank you for your letter. We are sorry that our {product} {verbed} in your
         {room} please note that it should never be used in a {room}, especially near any {animals}.
         send us your receipt and {amount} for shipping and handing. We will send you another {product} that,
         in our test, is {percent}% less likely to have {verbed}
         
         Thank you for your support
         Sincerely,
         {spokesman}
         {job_title}
         '''

5-5
salutation = 'salutation'
name = 'hanson'
product = 'chair'
verbed = 'broken'
room = 'class room'
animals = 'cat'
amount = '30$'
spokesman = 'james'
job_title = 'student'
# print(letter.format(salutation='salutation', name='hanson', product='chair', verbed='broken', room='class room',
#                     animals='cat', amount='30$', spokesman='james', job_title='student', percent='70'))

5-6
# print('%sy Mc%sFace' % ('duck', 'duck'))
# print('%sy Mc%sFace' % ('gourd', 'gourd'))
# print('%sy Mc%sFace' % ('spitz', 'spitz'))

5-7
# print('{name}y Mc{name}face'.format(name = 'duck'))
# print('{name}y Mc{name}face'.format(name = 'gourd'))
# print('{name}y Mc{name}face'.format(name = 'spitz'))

5-8
name = ['duck', 'gourd', 'spitz']
# print(f'{name[0]}y Mc{name[0]}face')
# print(f'{name[1]}y Mc{name[1]}face')
# print(f'{name[2]}y Mc{name[2]}face')
#
# for i in range(0, 3):
#     print(f'{name[i]}y Mc{name[i]}face')

6-1
# for i in [3, 2, 1, 0]:
#      print(i)

6-2
guess_me = 7
number = 1
# while guess_me >= number:
#     if guess_me > number:
#         print('too low!')
#     elif guess_me == number:
#         print('found it!')
#     else:
#         print('oops!')
#     number = number + 1


6-3
guess_me = 5
# for i  in range(10):
#     if guess_me > i:
#         print('too low!')
#     elif guess_me == i:
#         print('found it!')
#     else:
#         print('oops')
#         break