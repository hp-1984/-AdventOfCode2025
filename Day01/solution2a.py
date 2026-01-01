poz = 50
passwd = 0

def dial(poz, direction, step):
  if direction == 'R':
    poz = (poz + step) % 100
  elif direction == 'L':
    poz = (poz - step) % 100
  return poz

def passwd_round(poz, direction, step):

  if direction == 'R':
    zero = (100 - poz ) % 100
  else:
    zero = poz % 100
  #print("zero", zero, direction, poz)
  if zero == 0:
    zero = 100

  if step < zero:
    return 0
  return 1 + (step - zero) // 100

with open('input2.txt', 'r') as f:
  for sor in f:
    s = sor.strip()
    if s and len(s) >= 2:
      #print(f"{s[0]}, {int(s[1:])}")
      direction = s[0]
      step = int(s[1:])
      passwd += passwd_round(poz, direction, step)
      poz = dial(poz, direction, step)


print("Pozition", poz)
print("Password", passwd)
