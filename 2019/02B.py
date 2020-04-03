def run12(pgm, s1, s2):
  pgm = [i for i in pgm]
  pgm[1:3] = [s1, s2]
  return run(pgm)[0]

def run(pgm):
  pc = 0
  while pgm[pc] != 99:
    op, s1, s2, t = pgm[pc:pc+4]
    if op == 1:
      pgm[t] = pgm[s1] + pgm[s2]
      pc += 4
    elif op == 2:
      pgm[t] = pgm[s1] * pgm[s2]
      pc += 4
    else:
      msg = 'Bad Op: ' + str(op)
      raise Exception(msg)
  return pgm


assert run([1,0,0,0,99]) == [2,0,0,0,99]
assert run([2,3,0,3,99]) == [2,3,0,6,99]
assert run([2,4,4,5,99,0]) == [2,4,4,5,99,9801]
assert run([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99]

pgm = [int(i) for i in open('02.input').read().strip().split(',')]
result = run12(pgm, 12, 2)
print result

# assist = s1 * 243000 + s2 + 250702

def find_parms(result):
  s2 = (result - 250702) % 243000
  s1 = ((result - 250702) - s2) // 243000
  return s1, s2

s1, s2 = find_parms(19690720)
assert run12(pgm, s1, s2) == 19690720
print s1, s2


