N = int(input('Students: '))
K = int(input('Apples: '))

if K > N:
    print('The ' + str(K - (K % N)) + ' apples have been taken')
    print('Каждый студент взял по ' + str(int((K - (K % N))/N)) + ' яблок')
    print('Осталось: ' + str(K%N) + ' яблок')
elif K == N:
    print('Каждый студент получил по 1 яблоку. Осталось 0 яблок.')
else:
    print(str(K) + ' студентов взяли по 1 яблоку. ' + str(N-K) + ' студентов остались без яблок.')