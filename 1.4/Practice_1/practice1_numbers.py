with open("number_list.txt", "w") as file:
    numbers = [str(num) + "\n" for num in range(50, 101)]
    file.writelines(numbers)

print("Numbers from 50 to 100 written to number_list.txt")
