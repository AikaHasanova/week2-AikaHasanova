budget = "b"
daily = "d"
weekly = "w"
code = (input("Enter the customer code : "))
rent_period = int(input("Rental period : "))
odometer_start = int(input("Odometer reading at the start of the rental period : "))
odometer_end = int(input("Odometer reading at the end of the rental period : "))
miles_driven = odometer_end - odometer_start
print("miles_driven", miles_driven)
cost_b = (rent_period * 40) + (0.25 * miles_driven)  # budget
cost_d = rent_period * 60
ex_cost_d = ((rent_period * 60) + (miles_driven - (rent_period * 100)) * 0.25)
cost_w = (rent_period * 190)  # less than 900
ex_cost_w = (390 * rent_period) + (0.25 * miles_driven)  # more than 1500 miles

if code == "b":
    print("amount due : ", cost_b)

if code == "d":
    if miles_driven < cost_d:
        print("If you drive less than 100 miles: ", cost_d)

    else:
        print("if you drive more than 100 the amount due is: ", ex_cost_d)

if code == "w" and miles_driven < 900:
    print("If you drive less than 900 : ", cost_w)

    if miles_driven > cost_w:
        print("If you drive between 900 - 1500 miles : ", (190 + 100) * rent_period)
    else:
        print("If you driven more than 1500 miles amount due is : ", ex_cost_w)
