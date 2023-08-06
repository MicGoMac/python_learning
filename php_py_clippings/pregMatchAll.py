import re
'''
doubt:
full use of search obj, compare to php pregmatch

test use findall on web scrapping

confirm 
sub == str_replace?

split == split function?, but with multi result?

'''

pattern="quick.*fox"

t='''The quick brown fox jumps over the lazy dog The quick brown fox jumps over the lazy dog
not cat not fox end'''

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
