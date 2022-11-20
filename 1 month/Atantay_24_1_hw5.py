data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")
designation = []
codes = []
for i in data:
    if isinstance(i, str ):
        designation.append(i)
codes.append(designation.pop(2))
codes.append(designation.pop(3))
codes.append(designation.pop(3))
codes.append(designation.pop(4))
codes.append(designation.pop(-1))
operators = {}
count=0
while count != len(codes):
    operators[designation[count]] = [codes[count]]
    count+=1
del operators['Katel']
del operators['Fonex']
operators['O!'].append('0700')
operators['O!'].append('0500')
operators['Megacom'].append('0999')
operators['Megacom'].append('0555')
operators['Beeline'].append('0222')
operators['Beeline'].append('0777')
for designation, codes in operators.items():
    print(f"{designation}: {codes}")
