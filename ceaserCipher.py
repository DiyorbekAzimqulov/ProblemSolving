# https://www.hackerrank.com/challenges/caesar-cipher-1/problem
def caesarCipher(s: str, k: int):
    k %= 26
    cipher_text = ''
    for i in s:
        if i.isalpha():
            if i.isupper():
                pos = ord(i) + k
                if pos > 90:
                    pos = 64 + (pos - 90)
                cipher_text += chr(pos)
            else:
                pos = ord(i) + k
                if pos > 122:
                    pos = 96 + (pos - 122)
                cipher_text += chr(pos)
        else:
            cipher_text += i
    return cipher_text

s = "www.abc.xy"
k = 87
print(caesarCipher(s, k))
