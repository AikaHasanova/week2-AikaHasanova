

air_temp1 = 10.0
air_speed1 = 15
wct_index1 = 35.74 + 0.6215 * air_temp1 - 35.75 * air_speed1 ** 0.16 + 0.4275 * air_temp1 * air_speed1**0.16
print("Wind index 1:", int(wct_index1))
air_temp2 = 0.0
air_speed2 = 25
wct_index2 = 35.74 + 0.6215 * air_temp2 - 35.75 * air_speed2 ** 0.16 + 0.4275 * air_temp2 * air_speed2**0.16
print("Wind index 2:", int(wct_index2))
air_temp3 = -10.0
air_speed3 = 35
wct_index3 = 35.74 + 0.6215 * air_temp3 - 35.75 * air_speed3 ** 0.16 + 0.4275 * air_temp3 * air_speed3**0.16
print("Wind index 3:", int(wct_index3))

air_temp = int(input("Enter the air temperature"))
air_speed = int(input("Enter the air speed"))
wct_index = 35.74 + 0.6215 * air_temp - 35.75 * air_speed**0.16 + 0.4275 * air_temp * air_speed**0.16
print("Wind temperature index is : ", wct_index)

answer = str(input('Do you want to continue? (yes/no): '))
if answer == 'no':
   print ('Goodbye')
if answer=='yes':
   print("start again")



