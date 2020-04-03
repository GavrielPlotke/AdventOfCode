import md5

def coin(secret, zero_count):
  zeros = '0' * zero_count
  i = 0
  while True:
    i += 1
    m = md5.new(secret + str(i))
    h = m.hexdigest()
    if h.startswith(zeros):
      return i

assert coin('abcdef', 5) == 609043
assert coin('pqrstuv', 5) == 1048970

data = open('04.input').read()
print coin(data, 5)
print coin(data, 6)
