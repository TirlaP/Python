def howSum(targetSum, numbers):
    if targetSum == 0:
        print(targetSum)
    if targetSum < 0:
        return None

    for num in numbers:
        remainder = targetSum - num
        remainderResult = howSum(remainder, numbers)
        print(remainderResult)

    return None

print(howSum(7, [2, 3, 4, 7]))