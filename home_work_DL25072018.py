# Write a function:
# def solution(A)
# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
# Given A = [1, 2, 3], the function should return 4.
# Given A = [−1, −3], the function should return 1.
# Assume that:
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].
# Complexity:
# expected worst-case time complexity is O(N);
# expected worst-case space complexity is O(N) (not counting the storage required for input arguments).

# a = [-4,-2, 0,1,2,3,4]

# A=[]
# import random
# for i in range(100000):
#     A.append(random.randint(-10000, 10000))
# if 0 not in A:
#     A.append(0)
#
#
# def solution(A):
#     A.append(0)
#     a_sorted = sorted(list(set(A)))
#     position_of_zero = a_sorted.index(0)
#     elem = 0
#     for i in range(position_of_zero + 1, len(a_sorted)):
#         if a_sorted[i] - elem == 1:
#             elem = a_sorted[i]
#         if a_sorted[i] - elem > 1:
#             smallest_int = elem + 1
#             break
#         else:
#             smallest_int = elem + 1
#     return smallest_int
#
# print(solution(A))

# A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.
# For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains
# two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1.
# The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.
# Write a function:
# def solution(N)
# that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.
# For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5.
# Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.
# Assume that:
# N is an integer within the range [1..2,147,483,647].
# Complexity:
# expected worst-case time complexity is O(log(N));
# expected worst-case space complexity is O(1).


# k = 2147483647
#
# def solution(N):
#     if N<=2147483647:
#         binary_number = "{0:b}".format(N)
#         i = binary_number.rfind('1')
#         return len(max(binary_number[:i].split('1')))
#     else:
#         return "Pls input valid number"
#
#
# print(solution(k))


# An array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one
# index, and the last element of the array is moved to the first place. For example, the rotation of array
# A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one index and 6 is moved to the first place).
# The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.
# Write a function:
# def solution(A, K)
# that, given an array A consisting of N integers and an integer K, returns the array A rotated K times.
# For example, given
A = [3, 8, 9, 7, 6]
# [6, 7, 9, 8, 3]


#     K = 3
# the function should return [9, 7, 6, 3, 8]. Three rotations were made:
#     [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
#     [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
#     [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
# For another example, given
#     A = [0, 0, 0]
#     K = 1
# the function should return [0, 0, 0]
# Given
#     A = [1, 2, 3, 4]
#     K = 4
# the function should return [1, 2, 3, 4]
# Assume that:
# N and K are integers within the range [0..100];
# each element of array A is an integer within the range [−1,000..1,000].
# In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.

#
# def soution(A,K):
#     if K > int(len(A)):
#         K = K%int(len(A))
#     A.reverse()
#     for i in range(0, K):
#         elem_for_trans = A.pop(0)
#         A.append(elem_for_trans)
#
#     A.reverse()
#     return A
#
# print(soution(A, 6))


# A positive integer D is a factor of a positive integer N if there exists an integer M such that N = D * M.
# For example, 6 is a factor of 24, because M = 4 satisfies the above condition (24 = 6 * 4).
# Write a function:
# def solution(N)
# that, given a positive integer N, returns the number of its factors.
# For example, given N = 24, the function should return 8, because 24 has 8 factors, namely 1, 2, 3, 4, 6, 8, 12, 24.
# There are no other factors of 24.
# Assume that:
# N is an integer within the range [1..2,147,483,647].
# Complexity:
# expected worst-case time complexity is O(sqrt(N));
# expected worst-case space complexity is O(1).

# n = 2147483647
#
#
# def find_factor_of_number(number):
#     counter = 2
#     divider = 2
#     second_divider = int(number/2)
#     factors = [1, number]
#     dividers = []
#     while divider < second_divider:
#         dividers.append(divider)
#         if number%divider == 0:
#             counter += 2
#             factors.append(divider)
#             factors.append(int(number/divider))
#             second_divider = int(number/divider)
#             divider += 1
#         else:
#             divider += 1
#             second_divider=int(number/divider)
#
#     return dividers
#
# print(len(find_factor_of_number(n)))




# You would like to set a password for a bank account. However, there are three restrictions on the format of the password:
# it has to contain only alphanumerical characters (a−z, A−Z, 0−9);
# there should be an even number of letters;
# there should be an odd number of digits.
# You are given a string S consisting of N characters. String S can be divided into words by splitting it at, and
# removing, the spaces. The goal is to choose the longest word that is a valid password. You can assume that if there
# are K spaces in string S then there are exactly K + 1 words.
# For example, given "test 5 a0A pass007 ?xy1", there are five words and three of them are valid passwords: "5", "a0A"
# and "pass007". Thus the longest password is "pass007" and its length is 7. Note that neither "test" nor "?xy1" is a
# valid password, because "?" is not an alphanumerical character and "test" contains an even number of digits (zero).
# Write a function:
# def solution(S)
# that, given a non-empty string S consisting of N characters, returns the length of the longest word from the string
# that is a valid password. If there is no such word, your function should return −1.
# For example, given S = "test 5 a0A pass007 ?xy1", your function should return 7, as explained above.
# Assume that:
# N is an integer within the range [1..200];
# string S consists only of printable ASCII characters and spaces.
# In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.

str = "test ress0003 pass0007 50 a00A rAFess01312 ?xy1"

# def sort_by_len(str):
#     return len(str)
#
# def find_valid_password(str):
#     words_lsit = str.split(' ')
#     valid_passwords_list = []
#     for word in words_lsit:
#         digit_count = 0
#         letter_count = 0
#         if word.isalnum() == True:
#             for letter in word:
#                 if letter.isdigit() == True:
#                     digit_count += 1
#                 else:
#                     letter_count += 1
#             if digit_count%2 != 0 and letter_count%2 == 0:
#                 valid_passwords_list.append(word)
#     valid_passwords_list.sort(key=sort_by_len)
#     try:
#         valid_passwords_list[-1]
#         return valid_passwords_list[-1]
#     except:
#         return -1
#
# print(find_valid_password(str))



# A string S consisting of N characters is called properly nested if:
# S is empty;
# S has the form "(U)" where U is a properly nested string;
# S has the form "VW" where V and W are properly nested strings.
# For example, string "(()(())())" is properly nested but string "())" isn't.
# Write a function:
# def solution(S)
# that, given a string S consisting of N characters, returns 1 if string S is properly nested and 0 otherwise.
# For example, given S = "(()(())())", the function should return 1 and given S = "())", the function should return 0,
# as explained above.
# Assume that:
# N is an integer within the range [0..1,000,000];
# string S consists only of the characters "(" and/or ")".
# Complexity:
# expected worst-case time complexity is O(N);
# expected worst-case space complexity is O(1) (not counting the storage required for input arguments).

# import re
#
# str = '(((a)))((as)(as))(as)'
#
# def check_of_nested(str):
#     if len(str) == 0:
#         return 1
#     for s in re.findall(r'\(\w*\)', str):
#         print(s)
#         str = str.replace(s, '')
#     try:
#         len(str) == 0
#         print(str, len(str))
#         return 1
#     except:
#         return 0
#
#
#
#
# print(check_of_nested(str))



def nesting(str):
    open_bracket_counter = 0
    for s in str:
        if s == '(' and open_bracket_counter >= 0:
            open_bracket_counter += 1
        if s == ')' and open_bracket_counter >= 0:
            open_bracket_counter -= 1
        print(s, open_bracket_counter)

    if open_bracket_counter != 0:
        return 0
    if open_bracket_counter == 0:
        return 1



print(nesting('((((76)(())(()))'))