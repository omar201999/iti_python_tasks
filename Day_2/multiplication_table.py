def generate_table(number):
    table = []
    for i in range(1, number + 1):
        row = [i * j for j in range(1, i + 1)]
        table.append(row)
    return table


input_number = int(input("Enter a number: "))
result_table = generate_table(input_number)
print(result_table)
