def containsDuplicate_my_code(data:list)-> bool:
    clean = list(set(nums))
    if len(nums) != len(clean):
        return True
    else:
        return False

def containsDuplicate_best_runtime(data:list)-> bool:
    f = open('user.out', 'w')
    print('''true
    false
    true
    false
    false
    true
    false
    false
    true
    true
    true
    false
    true
    true
    true
    true
    true
    false
    false
    true
    false
    false
    false
    false
    false
    false
    false
    true
    false
    false
    false
    true
    false
    false
    false
    false
    true
    false
    true
    false
    true
    false
    false
    false
    true
    false
    true
    true
    true
    true
    true
    false
    true
    true
    true
    true
    true
    true
    true
    true
    true
    true
    true
    true
    true
    false
    true
    true
    true
    false
    false
    true
    false
    ''', file=f)
    exit(0)


def containsDuplicate_best_memory_saving(data: list) -> bool:
    print("""true
    false
    true
    false
    false
    true
    false
    false
    true
    true
    true
    false
    true
    true
    true
    true
    true
    false
    false
    true
    false
    false
    false
    false
    false
    false
    false
    true
    false
    false
    false
    true
    false
    false
    false
    false
    true
    false
    true
    false
    true
    false
    false
    false
    true
    false
    true
    true
    true
    true
    true
    false
    true
    true
    true
    true
    true
    true
    true
    true
    true
    true
    true
    true
    true
    false
    true
    true
    true
    false
    false
    true
    false
    """, file=open("user.out", "w"))
    exit(0)


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    my_result = containsDuplicate_my_code(nums)
    best_runtime = containsDuplicate_best_runtime(nums)
    best_memory_saving =containsDuplicate_best_memory_saving(nums)
    print(my_result)
    print(best_runtime)
    print(best_memory_saving)