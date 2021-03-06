def lights(grid, line):
  a1, a2 = line.strip().split(' through ')
  op, a1 = a1.rsplit(None,1)
  a1 = tuple(int(x) for x in a1.split(','))
  a2 = tuple(int(x) for x in a2.split(','))
  print op, a1, a2
  if op == 'toggle':
    for i1 in range(a1[0], a2[0]+1):
      for i2 in range(a1[1], a2[1]+1):
        grid[i1][i2] = not grid[i1][i2]
  elif op == 'turn on':
    for i1 in range(a1[0], a2[0]+1):
      for i2 in range(a1[1], a2[1]+1):
        grid[i1][i2] = True
  elif op == 'turn off':
    for i1 in range(a1[0], a2[0]+1):
      for i2 in range(a1[1], a2[1]+1):
        grid[i1][i2] = False

def run(lines):
  grid = [ [False for i in range(1000)] for j in range(1000) ]
  for line in lines:
    lights(grid, line)
  return grid

lines = '''
turn on 100,100 through 199,299
turn off 150,200 through 249,399
toggle 125,225 through 224,274
'''.strip().split('\n')
grid = run(lines)
assert sum(sum(1 for cell in row if cell) for row in grid) == 17500

lines = open('06.input').readlines()
grid = run(lines)
print 'Lights:', sum(sum(1 for cell in row if cell) for row in grid)
