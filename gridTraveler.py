def grid_traveler(m, n, memo = {}):
    key = str(m) + ',' + str(n)
    if key in memo:
        return memo[key]

    #  are the args in the memo
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    memo[key] = grid_traveler(m - 1, n, memo) + grid_traveler(m, n - 1, memo)
    return memo[key]



print(grid_traveler(1, 1))  # 1
print(grid_traveler(2, 3))  # 3
print(grid_traveler(3, 2))  # 3
print(grid_traveler(3, 3))  # 6
print(grid_traveler(18, 18))  # 233606220
