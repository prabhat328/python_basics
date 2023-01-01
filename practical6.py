# Practical 6

# A
import re
stri = "Hello World123@#$%"
st0 = re.findall("\s",stri)
st1 = re.findall("\S",stri)

stri = "Hello@ 79_#World"
st2 = re.findall("\w",stri)
st3 = re.findall("\W",stri)
st4 = re.findall("\d",stri)
st5 = re.findall("\D",stri)
# st6 = re.findall("\s",stri)
print(st0)
print(st1)
print(st2)
print(st3)
print(st4)
print(st5)

# B
import re
str1 = "Batch 3 is performing practical"
sp1 = re.findall("[a-p]", str1)
print(sp1)
sp2 = re.findall("^Batch", str1)
print(sp2)
sp3 = re.findall("cal$", str1)
if sp3:
  print("True")
else:
  print("False")
