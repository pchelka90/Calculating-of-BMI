# Prośba o podanie wagi i wzrostu od użytkownika
waga = float(input("Podaj wagę (w kilogramach): "))
wzrost = float(input("Podaj wzrost (w metrach): "))

# Obliczenie indeksu masy ciała (BMI)
bmi = waga / (wzrost ** 2)

# Wyświetlenie kategorii BMI
print(f"Twój indeks masy ciała (BMI) wynosi: {bmi:.2f}")

if bmi < 18.5:
    print("Niedowaga")
elif 18.5 <= bmi < 24.9:
    print("Waga prawidłowa")
elif 25 <= bmi < 29.9:
    print("Nadwaga")
else:
    print("Otyłość")
