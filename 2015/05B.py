def pairs(word):
  for i in range(0, len(word)-2):
    if word[i:i+2] in word[i+2:]:
      return True
  return False

def sandwitch(word):
  for i in range(0, len(word)-2):
    if word[i] == word[i+2]:
      return True
  return False

def nice(word):
  word = word.strip()
  return pairs(word) and sandwitch(word)

assert pairs('xy0xy')
assert pairs('xyxy')
assert pairs('aaa') == False
assert sandwitch('y0y')

assert nice('qjhvhtzxzqqjkmpb') == True
assert nice('xxyxx') == True 
assert nice('uurcxstgmygtbstg') == False
assert nice('ieodomkazucvgmuy') == False

lines = open('05.input').readlines()
print 'Nice Words:', sum(1 for word in lines if nice(word))
