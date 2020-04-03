
def calc(DAG, target):
  print '  ', target
  if type(target) == int:
     return target
  instruction = DAG[target]
  value = instruction[0]
  if value == None:
    fun = instruction[1]
    value = fun(*instruction[2:]) & (2**16 - 1)
    DAG[target][0] = value
  return value
      

def fix_args(*args):
  return [int(arg) if arg.isdigit() else arg for arg in args]

def form(DAG, ops, line):
  tokens = line.split()
  if len(tokens) == 3:
     assert tokens[1] == '->'
     args = fix_args(tokens[0])
     target = tokens[2]
     op = 'ASSIGN'
  elif len(tokens) == 4:
     assert tokens[0] == 'NOT'
     assert tokens[2] == '->'
     args = fix_args(tokens[1])
     target = tokens[3]
     op = tokens[0]     
  elif len(tokens) == 5:
     assert tokens[3] == '->'
     args = fix_args(tokens[0], tokens[2])
     target = tokens[4]
     op = tokens[1]     
  else:
     raise Exception("Invalid len(tokens): " + len(tokens))
  assert target not in DAG
  assert op in ops
  DAG[target] = [None, ops[op]] + args
  
  

def run(lines):
  DAG = {}
  ops = dict(
    ASSIGN = lambda x : calc(DAG, x) ,
    NOT    = lambda x : ~ calc(DAG, x) ,
    AND    = lambda x,y : calc(DAG, x) & calc(DAG, y) ,
    OR     = lambda x,y : calc(DAG, x) | calc(DAG, y) ,
    LSHIFT = lambda x,y : calc(DAG, x) << calc(DAG, y) ,
    RSHIFT = lambda x,y : calc(DAG, x) >> calc(DAG, y) ,
  )
  for line in lines:
    form(DAG, ops, line)
  for key in DAG:
    print 'key =', key
    calc(DAG, key)
  return DAG

lines = '''
123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
'''.strip().split('\n')

DAG = run(lines)

keyvals = [ (key, int(val)) for key, val in (keyval.split(': ') for keyval in '''
d: 72
e: 507
f: 492
g: 114
h: 65412
i: 65079
x: 123
y: 456
'''.strip().split('\n')
)]

for key, val in keyvals:
  assert DAG[key][0] == val


lines = open('07.input').readlines()

DAG = run(lines)

value = DAG['a'][0]
print "DAG['a'][0] =", value

# # #  Part 2  # # #

for key in DAG:
  DAG[key][0] = None

DAG['b'][0] = value
print "calc(DAG, 'a') =", calc(DAG, 'a')

