


def houses(data):
  setNE = set()
  north, east = 0, 0
  setNE.add( (north, east) )
  for op in data:
    if op == '<':
      east -= 1
    elif op == '>':
      east += 1
    elif op == '^':
      north += 1
    elif op == 'v':
      north -= 1
    setNE.add( (north, east) )
  return len(setNE)

assert houses('>') == 2
assert houses('^>v<') == 4
assert houses('^v^v^v^v^v') == 2

data = open('03.input').read()
print 'len(data) =', len(data)
print 'houses =', houses(data)
