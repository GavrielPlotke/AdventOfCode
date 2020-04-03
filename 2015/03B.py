
def houses(data12):
  data1 = ''.join(c for i,c in enumerate(data12) if i%2 == 0) 
  data2 = ''.join(c for i,c in enumerate(data12) if i%2 == 1) 
  setNE = set()
  for data in (data1, data2):
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

assert houses('^v') == 3
assert houses('^>v<') == 3
assert houses('^v^v^v^v^v') == 11

data = open('03.input').read()
print 'len(data) =', len(data)
print 'houses =', houses(data)
