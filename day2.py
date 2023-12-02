num_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

# Day 1
total_sum: int = 0

def foo(input: str):
    global total_sum
    nums = []
    
    for key in list(num_map.keys()):
        if key in input:
            pass
    
    for c in input:
        if c.isnumeric():
            nums.append(c)
    
    if len(nums) == 1:
        nums.append(nums[0])
    first_num = int(nums[0])
    last_num = int(nums[len(nums) - 1])
    
    total_sum += first_num * 10 + last_num


def getInput():
    inputs = []
    with open("input.txt", "r") as f:
        return f.readlines()


for i in getInput():
    foo(i)
    
# print(total_sum)
# foo(getInput())
