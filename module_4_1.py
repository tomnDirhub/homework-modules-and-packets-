from fake_math import divide as fake_div
from true_math import divide as true_div

res1 = fake_div(39, 13)
res2 = fake_div(12, 0)
res3 = true_div(64, 8)
res4 = true_div(54, 0)
print(res1, res2, res3, res4, sep = "\n")
