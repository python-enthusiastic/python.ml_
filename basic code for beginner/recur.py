# n! = n*(n-1)*(n-2)*(n-3)....1
# n!=n*(n-1)!
def factorial_iteretive(n):
    """

    :param n: fac_iterative:
    :return:
    """
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac
def fac_recursive(n):
    if n==1:
        return 1
    else:
        return n * fac_recursive(n-1)
number = int(input("enter number for factorial :"))
print("foctorial of this number ",factorial_iteretive(number))
print("fatorial for fac_recursive :",fac_recursive(number))
# def fac_recursive(n):
#     """
#
#     :param n:
#     :return:
#     """
#     if n==1:
#         return 1
#     else:
#         return n *fac_iterative(n-1)
# number = int(input("enter number for factorial :"))
# print("factorial of fac_itrative :", fac_iterative(number))
# print("factorial for fac_recursive :" , fac_recursive(number))
