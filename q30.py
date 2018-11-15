relatives={"Lisa":"daughter", "Bart":"son", "Marge":"mother", "Homer":"father", "Santa":"Dog"}
ages={"Lisa":8,"Bart":10,"Marge":35,"Homer":40,"Santa":2}
print("The Simpsons")
for i in relatives:
  print(i, "is a", relatives.get(i), "and is" ,ages.get(i), "years old")
