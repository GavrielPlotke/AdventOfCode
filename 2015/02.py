def paper(dim):
  a, b, c = sorted(int(x) for x in dim.strip().split('x'))
  s1 = a * b
  s2 = a * c
  s3 = b * c
  return s1 * 3 + s2 * 2 + s3 * 2

def ribbon(dim):
  a, b, c = sorted(int(x) for x in dim.strip().split('x'))
  return 2 * a + 2 * b + a * b * c

assert paper('2x3x4') == 58
assert paper('1x1x10') == 43
assert ribbon('2x3x4') == 34
assert ribbon('1x1x10') == 14


lines = open('02.input').readlines()
print 'paper:', sum(paper(line) for line in lines)
print 'ribbon:', sum(ribbon(line) for line in lines)


