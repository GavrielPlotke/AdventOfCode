def calc_fuel(modules):
  return sum(
    int(float(module) / 3.0) - 2 for module in modules
  ) 

tests = ( (12,2), (14,2), (1969,654), (100756,33583) )

for mass, fuel in tests:
  assert calc_fuel( (mass,) ) == fuel

print calc_fuel( open('01.input') )