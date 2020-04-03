def elevator(data):
  opens = tuple(x for x in data if x == '(')
  closes = tuple(x for x in data if x == ')')
  floor = len(opens) - len(closes)
  return floor

assert elevator('(())') == 0
assert elevator('()()') == 0
assert elevator('(((') == 3
assert elevator('(()(()(') == 3
assert elevator('))(((((') == 3
assert elevator('())') == -1
assert elevator('))(') == -1
assert elevator(')))') == -3
assert elevator(')())())') == -3

data = open('01.input').read()


print elevator(data)
