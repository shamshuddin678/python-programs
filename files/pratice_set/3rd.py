def generateTable(n):
    table = ""
    for i in range(1,11):
        table += f"{n} x {i} = {n*i}\n"

    with open(f"files/pratice_set/tables/table_{n}.txt","w") as f:
        f.write(table)

for i in range(10,13):
    generateTable(i)