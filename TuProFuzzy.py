import csv
def kurvaNaik(x,a,b):
    return (x-a)/(b-a)
def kurvaTurun(x,c,d):
    return -1*(x-d)/(d-c)
def salaryNaik(salary,a,b):
    return kurvaNaik(salary,a,b)
def salaryTurun(salary,c,d):
    return kurvaTurun(salary,c,d)
def debtNaik(debt,a,b):
    return kurvaNaik(debt,a,b)
def debtTurun(debt,c,d):
    return kurvaTurun(debt,c,d)
def bandinginMin(nilai1,nilai2):
    if nilai1 >= nilai2 :
        return nilai2
    else :
        return nilai1
def defuzzification(resultEndTDB,resultEndBB):
    if resultEndBB + resultEndTDB == 0 :
        hasil = 1
    else :
        hasil = resultEndBB + resultEndTDB
    return (resultEndTDB * 20 + resultEndBB * 60) / hasil
hasilDefuzz = []
hasilAsli = []
noKeluargaYangButuhBantuan = []
with open('DataTugas2.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader :
        if line_count == 0:
            line_count += 1
        else:
            beriBantuan = 0
            tidakBeriBantuan = 0
            BB = 0
            TDB = 0
            salary = float(row[1])
            debt = float(row[2])
            noKeluarga = int(row[0])
            if salary >= 0 and salary <= 0.5 :
                kBawah = 1
                kTengah = 0
                kAtas = 0
                # statusSalary.append('kBawah')
            elif salary > 0.5 and salary < 0.6 :
                c = 0.5
                d = 0.6
                kBawah = salaryTurun(salary,c,d)
                kTengah = salaryNaik(salary,c,d)
                kAtas = 0
                # statusSalary.append('kBawah')
                # statusSalary.append('kTengah')
            elif salary >= 0.6 and salary <= 1.0 :
                kBawah = 0
                kTengah = 1
                kAtas = 0
                # statusSalary.append('kTengah')
            elif salary > 1.0 and salary < 1.1 :
                c = 1.0
                d = 1.1
                kBawah = 0
                kTengah = salaryTurun(salary, c, d)
                kAtas = salaryNaik(salary, c, d)
                # statusSalary.append('kTengah')
                # statusSalary.append('kAtas')
            elif salary >= 1.1 and salary <= 2.0 :
                kBawah = 0
                kTengah = 0
                kAtas = 1
                # statusSalary.append('kAtas')
            if debt >= 0 and debt <= 25 :
                if debt >= 20 and debt <= 25 :
                    tidakMiskin = 1
                    hampirMiskin = debtNaik(debt,20,28)
                    miskin = 0
                    tidakMiskin = 0
                    # statusDebt.append('tidakMiskin')
                    # statusDebt.append('hampirMiskin')
                else:
                    tidakMiskin = 1
                    hampirMiskin = 0
                    miskin = 0
                    sangatMiskin = 0
                    # statusDebt.append('tidakMiskin')
            elif debt > 25 and debt < 28 :
                tidakMiskin = debtTurun(debt,25,30)
                hampirMiskin = debtNaik(debt,20,28)
                miskin = 0
                sangatMiskin = 0
                # statusDebt.append('tidakMiskin')
                # statusDebt.append('hampirMiskin')
            elif debt >= 28 and debt <= 45 :
                if debt >= 28 and debt <= 30 :
                    tidakMiskin = debtTurun(debt,25,30)
                    hampirMiskin = 1
                    miskin = 0
                    tidakMiskin = 0
                    # statusDebt.append('tidakMiskin')
                    # statusDebt.append('hampirMiskin')
                elif debt >= 40 and debt <= 45 :
                    tidakMiskin = 0
                    hampirMiskin = 1
                    miskin = debtNaik(debt,40,48)
                    sangatMiskin = 0
                    # statusDebt.append('hampirMiskin')
                    # statusDebt.append('miskin')
                else :
                    tidakMiskin = 0
                    hampirMiskin = 1
                    miskin = 0
                    sangatMiskin = 0
                    # statusDebt.append('hampirMiskin')
            elif debt > 45 and debt < 48 :
                tidakMiskin = 0
                hampirMiskin = debtTurun(debt,45,50)
                miskin = debtNaik(debt,40,48)
                sangatMiskin = 0
                # statusDebt.append('hampirMiskin')
                # statusDebt.append('miskin')
            elif debt >= 48 and debt <= 65 :
                if debt >= 48 and debt <= 50 :
                    tidakMiskin = 0
                    hampirMiskin = debtTurun(debt,45,50)
                    miskin = 1
                    sangatMiskin = 0
                    # statusDebt.append('hampirMiskin')
                    # statusDebt.append('miskin')
                elif debt >= 60 and debt <= 65 :
                    tidakMiskin = 0
                    hampirMiskin= 0
                    miskin = 1
                    sangatMiskin = debtNaik(debt,60,68)
                    # statusDebt.append('miskin')
                    # statusDebt.append('sangatMiskin')
                else :
                    tidakMiskin = 0
                    hampirMiskin = 0
                    miskin = 1
                    sangatMiskin = 0
                    # statusDebt.append('miskin')
            elif debt > 65 and debt <68 :
                tidakMiskin = 0
                hampirMiskin = 0
                miskin = debtTurun(debt,65,70)
                sangatMiskin = debtNaik(debt,60,68)
                # statusDebt.append('miskin')
                # statusDebt.append('sangatMiskin')
            elif debt >= 68 and debt <= 99 :
                if debt >= 68 and debt <=70 :
                    tidakMiskin = 0
                    hampirMiskin = 0
                    miskin = debtTurun(debt,65,70)
                    sangatMiskin = 1
                    # statusDebt.append('miskin')
                    # statusDebt.append('sangatMiskin')
                else :
                    tidakMiskin=0
                    hampirMiskin = 0
                    miskin = 0
                    sangatMiskin = 1
                    # statusDebt.append('sangatmiskin')
            if tidakMiskin != 0 and kBawah != 0 :
                 BB = bandinginMin(tidakMiskin,kBawah)
                 if BB == 0 :
                    beriBantuan = BB
                 else :
                    if BB > beriBantuan :
                        beriBantuan = BB
            if hampirMiskin != 0 and kBawah != 0 :
                BB = bandinginMin(hampirMiskin,kBawah)
                if BB == 0 :
                    beriBantuan = BB
                else :
                    if BB > beriBantuan :
                        beriBantuan = BB
            if miskin != 0 and kBawah != 0 :
                BB = bandinginMin(miskin,kBawah)
                if BB == 0 :
                    beriBantuan = BB
                else :
                    if BB > beriBantuan :
                        beriBantuan = BB
            if sangatMiskin != 0 and kBawah != 0 :
                BB = bandinginMin(sangatMiskin,kBawah)
                if BB == 0 :
                     beriBantuan = BB
                else :
                    if BB > beriBantuan :
                        beriBantuan = BB
            if sangatMiskin != 0 and kTengah != 0 :
                BB = bandinginMin(sangatMiskin,kTengah)
                if BB == 0 :
                    beriBantuan = BB
                else :
                     if BB > beriBantuan :
                        beriBantuan = BB
            if miskin != 0 and kTengah != 0 :
                BB = bandinginMin(miskin,kTengah)
                if BB == 0 :
                    beriBantuan = BB
                else :
                    if BB > beriBantuan :
                        beriBantuan = BB
            if hampirMiskin != 0 and kTengah != 0 :
                TDB = bandinginMin(hampirMiskin,kTengah)
                if TDB == 0 :
                    tidakBeriBantuan = TDB
                else :
                    if TDB > tidakBeriBantuan :
                        tidakBeriBantuan = TDB
            if sangatMiskin != 0 and kTengah != 0 :
                TDB = bandinginMin(sangatMiskin,kTengah)
                if TDB == 0 :
                    tidakBeriBantuan = TDB
                else :
                    if TDB > tidakBeriBantuan :
                        tidakBeriBantuan = TDB
            if tidakMiskin != 0 and kAtas != 0 :
                TDB = bandinginMin(tidakMiskin,kAtas)
                if TDB == 0 :
                    tidakBeriBantuan = TDB
                else :
                    if TDB > tidakBeriBantuan :
                        tidakBeriBantuan = TDB
            if hampirMiskin != 0 and kAtas != 0 :
                TDB = bandinginMin(hampirMiskin,kAtas)
                if TDB == 0 :
                    tidakBeriBantuan = TDB
                else :
                    if TDB > tidakBeriBantuan :
                        tidakBeriBantuan = TDB
            if miskin != 0 and kAtas != 0 :
                TDB = bandinginMin(miskin,kAtas)
                if TDB == 0 :
                    tidakBeriBantuan = TDB
                else :
                    if TDB > tidakBeriBantuan :
                        tidakBeriBantuan = TDB
            if sangatMiskin != 0 and kAtas != 0 :
                 TDB = bandinginMin(sangatMiskin,kAtas)
                 if TDB == 0 :
                    tidakBeriBantuan = TDB
                 else :
                    if TDB > tidakBeriBantuan :
                        tidakBeriBantuan = TDB
            hasilDefuzz.append(defuzzification(TDB,BB))
            noKeluargaYangButuhBantuan.append(noKeluarga)
        line_count += 1

    noKeluargatmp =  []
    hasilSort = sorted(hasilDefuzz)
    # print(hasilSort)
    for i in range(80,100) :
        hasilAsli.append(hasilSort[i])
    for j in range(0,20):
        for k in range(0,99):
            if (hasilAsli[j] == hasilDefuzz[k]):
                if noKeluargaYangButuhBantuan[k] not in noKeluargatmp:
                    noKeluargatmp.append(noKeluargaYangButuhBantuan[k])
with open('TebakanTugas2.csv', mode='w') as TebakanTugas2:
        spamwriter = csv.writer(TebakanTugas2, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for i in range(2,len(noKeluargatmp)):
            spamwriter.writerow([noKeluargatmp[i]])
