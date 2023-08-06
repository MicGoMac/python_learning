import re

pattern="quick.*fox"

t="The quick brown fox jumps over the lazy dog The quick brown fox jumps over the lazy dog"

res = (re.search(pattern, t))
#res = None if no matched
print("search returns obj")
print(res)
print(res.span())
print(res.group())
print(res.string)


print("\nfindall")
res = (re.findall(pattern, t))
print(res)

print("\nsplit")
res = (re.split(pattern, t))
print(res)

print("\nreplace")
res = (re.sub(pattern, "The cat", t))
print(res)
