


print("THis is a puzzle favored by Eintein. You will be asked to enter a three digit number where the hundred's "
      "digit differs from the one digit by at least two. The procedure will always yield 1089.")


number = int(input('Give a number : '))

if (number < 1000 and number > 99):
    print("For the number", number ,"the reverse number is :", str(number)[::-1])

else:
    print("Inavlid input give a 3 digit number")

reverse_num = int(input('Enter the reversed number to find the difference:'))
difference = number-reverse_num

if number > reverse_num:
    print('The difference between', number, 'and', reverse_num, 'is :', difference)

print('Reverse the difference : ', str(difference)[::-1])
rev_dif = int(input('Enter the reversed number to sum : '))

print("The sum of : ", difference,"and revDiff is :", rev_dif+difference)



