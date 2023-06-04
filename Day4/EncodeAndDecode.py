# link = "https://leetcode.com/problems/encode-and-decode-strings/"

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

def encode(strs):
    s1="break"
    s2=""
    for x in strs:
        s2+=x
        s2+=s1
    return s2
def decode(s):
    a = s.split("break")
    return a[0:len(a)-1]

