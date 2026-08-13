import csv

file = "signups.csv"

data = []
f = open(file)
# LEARN: csv.DictReader turns each row into a dict keyed by the header row,
# so row["industry"] works instead of having to know column positions.
reader = csv.DictReader(f)
for row in reader:
    data.append(row)
# LEARN: this file is never closed if anything above throws an exception.
# The standard fix is `with open(file) as f:`, which closes it automatically
# even on error. This script doesn't do that, on purpose, it's the kind of
# thing that's easy to skip when you're moving fast.
f.close()

total = len(data)
by_industry = {}
sizes = []

for row in data:
    ind = row["industry"]
    # LEARN: this "check if key exists, then increment or initialize" pattern
    # is what collections.Counter (from the standard library) does in one line.
    if ind in by_industry:
        by_industry[ind] = by_industry[ind] + 1
    else:
        by_industry[ind] = 1
    s = row["employee_count"]
    # LEARN: every value from csv.DictReader is a string, even the numbers.
    # int(s) here converts it. Forgetting this is a very common CSV bug,
    # you'd get "4" + "2" = "42" instead of 4 + 2 = 6 if you skipped it.
    sizes.append(int(s))

print("total signups:", total)
print("by industry:")
for k in by_industry:
    print(k, by_industry[k])

avg = 0
for s in sizes:
    avg = avg + s
avg = avg / len(sizes)
# LEARN: this is a hand-rolled version of sum(sizes) / len(sizes). It also
# has a bug: if sizes is empty, this raises ZeroDivisionError. Nothing here
# checks for that, which is exactly the kind of thing a test would catch.
print("avg employees:", avg)

# quick hack to also flag "hot" leads, anyone under 10 employees
# TODO clean this up later lol
hot = []
for row in data:
    if int(row["employee_count"]) < 10:
        hot.append(row["company_name"])

# LEARN: this loop duplicates work already done above (looping over `data`,
# re-parsing employee_count as int again). Small on a 10-row CSV; on a
# 100,000-row one, every pass over the same data is a real cost.
print("hot leads:", hot)
