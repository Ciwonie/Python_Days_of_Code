import chardet

with open("ot_bytes.txt", "r", encoding="iso-3166") as f:
    for line in f:
        print(line, end="\n")
        print(chardet.detect(line), end="\n")

# 0c e2 80 a2 e2 80 99 e2 80 9e e2 80 9e e2 80 9e
# \xe2\x80\x9e\xe2\x80\x9e\r\n'
# iso 639-3

"""
Hypothesis: i believe the courses file was encoded in swiss german. I believe I need to use
iso 639-3 to decode swiss german, then translate the decoded text to english.
"""

# print(byte_sting.decode())
