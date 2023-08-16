import math

def get_prime_quotient(string: str):
    for index in range(1, len(string)+1):
        splited = string.split(string[:index])
        if not any(element for element in splited):
            return string[:index], len(splited) - 1



class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        prime1, quotient1 = get_prime_quotient(str1)
        prime2, quotient2 = get_prime_quotient(str2)
        if prime1 != prime2:
            return ''
        return prime1 * math.gcd(quotient1, quotient2)
