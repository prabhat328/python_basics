# A
class practical:
  def __init__(tp, fn, ln, rn):
    tp.name = fn
    tp.last = ln
    tp.roll = rn
    print(tp.name)

p1 = practical("Prabhat", "Tiwari", '079')
print(p1.last)

# B
class practical:
  def __init__(tp, fn, ln, rn):
    tp.name = fn
    tp.last = ln
    tp.roll = rn
    print(tp.name)
  def disp(tp):
    print(tp.name)
    print(tp.last)
    print(tp.roll)

class b3(practical):
  def __init__(tp, bn, fn, ln, rn):
    super().__init__(fn, ln, rn)
    tp.batch = bn
  def dis(tp):
    print(tp.batch)
ob1 = b3(3, "Prabhat", "Tiwari", "079")
ob1.dis()
ob1.disp()
