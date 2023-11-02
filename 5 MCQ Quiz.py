import random
A = ['Delhi', 'Kolkata', 'Mumbai', 'Chennai']
random.shuffle(A)
print('Which is the capital City of India:')
print('A.{}\nB.{}\nC.{}\nD.{}'.format(A[0], A[1],A[2], A[3] ))
choice = input().lower()

if choice == 'delhi':
    print('Correct!')

else:
    print("Wrong!")