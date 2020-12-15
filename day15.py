starting_nums = [1, 17, 0, 10, 18, 11, 6]


def play_game(starting_nums, limit):
    turn = len(starting_nums) - 2
    nums_last_said = {n: i for i, n in enumerate(starting_nums[:-1])}
    last_num = starting_nums[-1]
    while turn < limit - 2:
        turn += 1
        if last_num in nums_last_said.keys():
            age = turn - nums_last_said[last_num]
            nums_last_said[last_num] = turn
            last_num = age
        else:
            nums_last_said[last_num] = turn
            last_num = 0
    return last_num


print(play_game(starting_nums, 2020))

print(play_game(starting_nums, 30000000))
