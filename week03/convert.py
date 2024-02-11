# convert the float - dollar number with the minus
# to return absolute amount in cent
# author: Katarina Siklodyova

amount = float(input("Enter the amount value: "))
result = amount * 100
cent = abs(result)
rounded_cent = round(cent)

print("The absolute amount of entered value: {} is: {} cents." . format (amount,rounded_cent))
      