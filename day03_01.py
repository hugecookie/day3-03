# chap 5 text

# 여러줄의 문자열의 경우 '''가 유용하게 사용된다. ''를 더 붙여도 기능은 하지만, 뒤 ''기호와 연결되는 문장이 발생하므로 '''만 쓰도록 하자
poem = '''There was a Young Lady of Norway,
Who casually sat in a doorway;
When the door squeezed her flat,
She exclaimed, "What of that?"
This courageous Young Lady of Norway.'''
# print(poem)

army = "어등산 깊은 곳 \t 적막한 산하 \n 드리운 이 앞에 우리는 간다." # \n 줄바꿈 \t 탭 \' = ', \" = " 단, 원시 문자열은 줄바꿈 불가능
# print(army)
# 대화식 인터 프리터의 경우 중요한
start = "Na " * 4 + '\n'
middle = "Hey " * 3 + '\n'
end = "Goodbye"
# print(start+start+middle+end)
name = 'henny'
# name[0] = 'P' - error ****불변성****
name = 'Henny'
name.replace('H', 'P')

# print('P' + name[1:])

univ = 'inha university'
# print(univ[5:-6])
# print(univ[5:])
# print(univ[5:15])
# print(univ[-10:])
# print(univ[::2])
# 2칸에 하나씩 출력
# print(univ.split(' '))

pokemon_list = ['피카츄', '꼬부기']
pokemon_string = ','.join(pokemon_list)
# print(pokemon_string) #.join 앞의 str 타입의 문자열을 적어 두면 원소 사이에 붙어서 출력된다.

setup = "a duck goes into a bar..."
# print(setup.replace('duck ', 'marmoset'))
# print(setup.replace('duck ', 'marmoset')) # 횟수 제한을 둘 수도 있다.

world = ' earth '
# print(world.lstrip())
# print(world.rstrip())
subjects = '  python, data structure, database    '
# print(subjects.strip())
# print(subjects.strip('$'))

poem = '''All that doth flow we cannot liquid name or else would fire and water ne the same;
          But that is liquid which is moist and wet 
          Fire that property can never get.
          Then 'tis not cold that doth the fire put out But 'tis that wet that makes it die, no doubt.'''
# print(len(poem))
# print(poem.startswith('All')) # 첫 시작 글자가 All인가?

# print(univ.rfind('ha')) # find나 index나 같은 값을 반환
# print(subjects.isalnum())
# print(poem.count('that'))

# print(univ.capitalize())
# print(univ.upper())
# print(univ.lower())
# print(univ.title())
# print(univ.swapcase())

# print(univ.center(20))
# print(univ.rjust(20))
# print(univ.ljust(20))

# %s, %d, %%, %x, %o, %f, %e, %g
# print('%d %%' % 100)
thing = 'woodchuck'
# print('%+12s' % thing)
# print('%-12s' % thing)
# print('%12.3s' % thing)
thing = '98.6'
# print('%f' % thing)
# print('%+12f' % thing)
# print('%-12f' % thing)
# print('%12.3f' % thing)

thing = 'woodchuck'
place = 'lake'
# print('{}'.format(thing))
# print('The {} is in the {}.'.format(thing, place))
# print('The {1} is in the {0}.'.format(thing, place))
# print('The {thing} is in the {place}.'.format(thing = 'duck', place = 'bathtub'))
d = {'thing':'duck', 'place':'bathtub'}
# print('The {0[thing]} is in the {0[place]}'.format(d))
# print(f'The {thing} is in the {place}')



# while True:
#     dan = int(input('Dan:'))
#
#     if 1 < dan < 10:
#         i = 1
#         while i<10:
#             print(f'{dan}*{i} = {dan*i}')
#             i = i+1


numbers = [1,3,5]
position = 0





# prime number

# number = int(input("정수 입력 : "))
counts = 0

# k = 1
# while k <= 10:
#     if number % k == 0:
#         counts = counts + 1
# if counts == 2:
#     print(f'{number} is prime number!')
# else:
#     print(f'{number} is not prime number')
# count = 1
# for num in range(2, number):
#     if number % count == 0:
#         print(f'{number}는 {count}의 배수입니다.')
#     count = count+1


# num = input("숫자 2개를 입력 해주세요. 띄어 쓰기로 구분 ex) 3 14 ").split()
# big = small = int
# if num[0] > num[1]:
#     big = num[0] # 두 수의 위치 바꾸기
#     small = num[1]
# else:
#     big = num[1]
#     small = num[0]
# print(num[0], num[1])

# for i in range(small, big + 1):
#     count = 0
#     for k in range(2, i):
#         if i % k == 0:
#             count = count + 1
#     if count < 1:
#         print(f'{i}는 소수 입니다 .')
