def elevator(data):
  waiting = True
  floor = 0
  for idx, paren in enumerate(data):
    if paren == '(':
      floor += 1
    elif paren == ')':
      floor -= 1
    if floor == -1 and waiting:
      waiting = False
      print 'First time in basement =', idx + 1
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
