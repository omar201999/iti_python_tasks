bill_amount = 47.28
tip_percentage = 15
num_friends = 2

tip_amount = bill_amount * (tip_percentage / 100)

total_amount = bill_amount + tip_amount

each_share = total_amount / num_friends

print("Tip amount: ${:.2f}".format(tip_amount))
print("Total amount to pay: ${:.2f}".format(total_amount))
print("Each person needs to pay: ${:.2f}".format(each_share))
