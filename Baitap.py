cannang = float(input("Nhập số cân nặng: "))
chieucao = float(input("Nhập chiều cao (cm): "))

chieucao_met = chieucao / 100

bmi = cannang / chieucao_met**2

if bmi < 16:
    print("Gầy cấp độ III")
elif (bmi >= 16) & (bmi < 17):
    print("Gầy cấp độ II")
elif (bmi >= 17) & (bmi < 18.5):
    print("Gầy cấp độ I")
elif (bmi >= 18.5) & (bmi < 25):
    print("Bình thường")
elif (bmi >= 25) & (bmi < 30):
    print("Thừa cân")
elif (bmi >= 30) & (bmi < 35):
    print("Béo phì cấp độ I")
elif (bmi >= 35) & (bmi < 40):
    print("Béo phì cấp độ II")
else:
    print("Béo phì cấp độ III")
