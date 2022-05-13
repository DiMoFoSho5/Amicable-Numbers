# function for creating a list of proper divisors 
def get_dvsr_sum_lst(a):
    divisors = []
    sums_list = dict()

    if a % 2 != 0:
        for o in range(1, int(a / 2) + 2, 2):
            if a % o == 0:
                divisors += [o]
    else:
        for o in range(2, int(a / 2) + 1):
            if a % o == 0:
                divisors += [o]

    if sum(divisors) > 1:
        sums_list.update({str(a): sum(divisors) + 1})

    return sums_list


# function for determining if two numbers are amicable, based on their sums of divisors
def get_amicable_numbers(a):
    num_sum = dict()

    for i in range(1, a + 1):
        num_sum.update(get_dvsr_sum_lst(i))

    num_list = []

    for i in range(1, a + 1):
        if num_sum.get(str(num_sum.get(str(i)))) == i:
            if num_sum.get(str(i)) != i:
                num_list += [i]

    return num_list


# CHANGE n HERE, where n = the largest number to be checked for amicability
print(get_amicable_numbers(n))
