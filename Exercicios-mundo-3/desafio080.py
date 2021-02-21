#Um programa que cria uma lista ordenada com inputs do usuario

nums = []

for n in range (0,5):
    num = int(input('Digite um numero '))
    if n == 0 or num > nums[-1]:
        nums.append(num)

    else: 
        pos = 0
        while pos < len(nums):
            if num <= nums[pos]:
                nums.insert(pos, n)
                break
            pos += 1

print(nums)