import csv

file = "signups.csv"

data = []
f = open(file)
reader = csv.DictReader(f)
for row in reader:
    data.append(row)
f.close()

total = len(data)
by_industry = {}
sizes = []

for row in data:
    ind = row["industry"]
    if ind in by_industry:
        by_industry[ind] = by_industry[ind] + 1
    else:
        by_industry[ind] = 1
    s = row["employee_count"]
    sizes.append(int(s))

print("total signups:", total)
print("by industry:")
for k in by_industry:
    print(k, by_industry[k])

avg = 0
for s in sizes:
    avg = avg + s
avg = avg / len(sizes)
print("avg employees:", avg)

# quick hack to also flag "hot" leads, anyone under 10 employees
# TODO clean this up later lol
hot = []
for row in data:
    if int(row["employee_count"]) < 10:
        hot.append(row["company_name"])

print("hot leads:", hot)
