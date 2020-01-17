import re


re_email = re.compile(r'^.*\@.*.com$')

m1 = re_email.match('issac@outlook.com')
m2 = re_email.match('bill.gates@microsoft.com')
m3 = re_email.match('bobou#tlook.com')
m4 = re_email.match('mr-bob@example.com')

print(m1)
print(m2)
print(m3)
print(m4)









