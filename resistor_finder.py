available_resistor = '100	120	220	330	390	470	680	820	1000	1200	2200	4700	8200	10000	51000	100000'.split()
available_resistor = list(map(int,available_resistor))
print(available_resistor)

def parallel_sum(*resistor):
    return float(f'{1/sum([1/res for res in resistor]):.4f}')
parallel = {}
for res1 in available_resistor:
    for res2 in available_resistor:
        if (res2,res1) not in parallel:
            parallel[(res1,res2)] = parallel_sum(res1,res2)


for combination,resistance in parallel.items():
    print(combination,": ",resistance)
print(parallel_sum(10,10))
R_needed = float(input("Enter the Resistor you need: "))

if R_needed not in available_resistor:
    matching = []
    for association in parallel:
        Req = parallel[association]
        if abs(Req-R_needed) <= R_needed * 0.05:
            matching.append((association,Req,Req-R_needed))
    matching = sorted([[abs(values[2]),values[1],values[0]] for values in matching])
    matching = [[values[2],values[1],values[0]] for values in matching]
    print(f"tolerance(+/-) = {R_needed * 0.05} (5%)")
    print(f"{'Combination':<16} {'Req':^9}   Difference from target R")
    print('-'*40)
    for combination, req, differece in matching:
        print(f"{str(combination):<16}|{f'{req:.3f}':^9}|{f'{differece:.3f}':^9}")
    
else:
    print(R_needed)



