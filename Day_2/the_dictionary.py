def convert_to_sorted_dict(names_list):
    sorted_dict = {}
    for name in names_list:
        first_letter = name[0].lower()
        if first_letter in sorted_dict:
            sorted_dict[first_letter].append(name)
        else:
            sorted_dict[first_letter] = [name]

    for key in sorted(sorted_dict.keys()):
        sorted_dict[key] = sorted(sorted_dict[key])
    return sorted_dict


names = ["ahmed", "fatma", "Ibrahim"]
sorted_name_dict = convert_to_sorted_dict(names)

for key, value in sorted_name_dict.items():
    print(f"{key}: {value}")
