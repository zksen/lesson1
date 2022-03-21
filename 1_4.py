num = abs(int(input("Enter your number -> ")))
num_ans = num
num_max = num % 10
while num >= 1:
    num = num // 10
    if num % 10 > num_max:
        num_max = num % 10
    elif num > 9:
        continue
    else:
        print(f"Maximum digit in number {num_ans} is {num_max}")
        break
