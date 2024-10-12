unit = input("BMI Satuan (K)g atau (l)bs? ")
if unit.upper() == "K":
    berat = float(input("Berapa berat kamu? (kg) "))
    tinggi = float(input("Berapa tinggi kamu? (cm) "))
    tinggi = tinggi * 0.01
    bmi = berat / tinggi ** 2
else:
    berat = float(input("Berapa berat kamu? (lbs) "))
    tinggi = float(input("Berapa tinggi kamu? (ft) "))
    berat = berat / 2.20462
    tinggi = tinggi / 0.032808
    bmi = berat / tinggi ** 2
print("BMI kamu adalah " + str(bmi.__round__(1)))
if bmi < 18.5:
    print("Underweight, get something to eat")
elif bmi < 17:
    print("You are starving")
elif bmi > 30:
    print("Obesity")
elif bmi > 25:
    print("Overweight dont forget to exercise")
else:
    print("You are normal")