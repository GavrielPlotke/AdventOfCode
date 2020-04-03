
def nice(word):
  vowel = 0
  double = 0
  bad = 0
  prior = ''
  for char in word.strip():
    if char in 'aeiou':
      vowel += 1
    if char == prior:
      double += 1
    if prior+char in ('ab','cd','pq','xy'):
      bad += 1
    prior = char
  if vowel >= 3 and double >= 1 and bad == 0:
    return True
  return False

assert nice('ugknbfddgicrmopn') == True
assert nice('aaa') == True 
assert nice('jchzalrnumimnmhp') == False
assert nice('haegwjzuvuyypxyu') == False
assert nice('dvszwmarrgswjxmb') == False

lines = open('05.input').readlines()
print 'Nice Words:', sum(1 for word in lines if nice(word))
