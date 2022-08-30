# running_total = 0

# int = [1, 2, 3, 4, 5]
# for i in int:
#     if i % 2 == 0:
#         running_total += 1
#     # elif int[i] == 8:
#     #     running_total += 5
#     else:
#         running_total += 3
#     print(running_total)

# name = "Charles"
# city = "Festac"

# print("my name is {} and I stay in {} ".format(name, city))

def num(evn_num, odd_num, prime_num):
    print("{} is an even number, {} is a odd number, and {} is a prime number".format(
        evn_num, odd_num, prime_num))


num(prime_num=3, odd_num=9, evn_num=5)


def employee(fname, lname, email, company, *args, **kwargs):
    print("{} {} works at {}, her email is {}.".format(
        fname, lname, company, email))


employee("Jess", "Ingrass", "jessIn@mail.com",
         "TeachCode.org", "$75000", hire_date="September 2010")
