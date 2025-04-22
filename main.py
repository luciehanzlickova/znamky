znamky = []
for i in range(5):
    znamka = int(input(f"zadej {i+1}. znamku: "))
    znamky.append(znamka)

prumer = sum(znamky) / len(znamky)

print("zadane znamky jsou:")
for z in znamky:
    print(z)

print(f" prumer znamek je: {prumer:.2f}")
