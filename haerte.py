from timeit import default_timer as timer

zahl = 10
haertesteZahl = zahl

def haerte(zahl):
  haerte=0
  zahlstring = str(zahl);
  product = 1
  while len(zahlstring) > 1:
    if "0" in zahlstring:
      break
    product = 1

    for i in zahlstring:
      product = product * int(i)
      
      
    zahlstring = str(product)
    haerte += 1
    

  return haerte

hAlt = 1
while True:
  start = timer()

  if haerte(zahl) > haerte(haertesteZahl):
    haertesteZahl = zahl

  hAlt = haerte(zahl)

  end = timer()

  if zahl%(10**(len(str(zahl))-1)) == 0:
    print("zahl =", zahl)
    print("haertestezahl =", haertesteZahl, " Haerte =", haerte(haertesteZahl))
    print("Zeit pro Berechnung =", end-start, "s")
  zahl += 1