import string


def valid_palindrome(s):
    rr = ""
    ss = "".join(filter(lambda x: x in string.ascii_letters + string.digits, s)).lower()
    return True if ss.lower() == ss.lower()[::-1] else False


s = "A man, a plan, a canal: Panama"
resoult = valid_palindrome(s)
print(resoult)
