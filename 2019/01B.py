def calc_fuel(mass):
  fuel = int(float(mass) / 3.0) - 2
  if fuel <= 0:
    return 0
  return fuel + calc_fuel(fuel)

def calc_fuel_all(modules):
  return sum(
    calc_fuel(module) for module in modules
  ) 

tests = ( (12,2), (14,2), (1969,966), (100756,50346) )

for mass, fuel in tests:
  assert calc_fuel_all( (mass,) ) == fuel

print calc_fuel_all( open('01.input') )