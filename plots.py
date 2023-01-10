import pandas as pd
import matplotlib.pyplot as plt

exact_counts_du = pd.read_csv("results/exact_count_oliver_twist_DU.txt", sep=" ", header=0)
exact_counts_eng = pd.read_csv("results/exact_count_oliver_twist_ENG.txt", sep=" ", header=0)
exact_counts_fr = pd.read_csv("results/exact_count_oliver_twist_FR.txt", sep=" ", header=0)
exact_counts_ge = pd.read_csv("results/exact_count_oliver_twist_GE.txt", sep=" ", header=0)

plt.bar(exact_counts_du["letter"], exact_counts_du["count"], color="green")
plt.title("Exact counter for Dutch book")
plt.xlabel("Letter")
plt.ylabel("Count")
plt.savefig("results/plots/exact_count_DU.png")
plt.clf()

plt.bar(exact_counts_eng["letter"], exact_counts_eng["count"], color="green")
plt.title("Exact counter for English book")
plt.xlabel("Letter")
plt.ylabel("Count")
plt.savefig("results/plots/exact_count_ENG.png")
plt.clf()

plt.bar(exact_counts_fr["letter"], exact_counts_fr["count"], color="green")
plt.title("Exact counter for French book")
plt.xlabel("Letter")
plt.ylabel("Count")
plt.savefig("results/plots/exact_count_FR.png")
plt.clf()

plt.bar(exact_counts_ge["letter"], exact_counts_ge["count"], color="green")
plt.title("Exact counter for German book")
plt.xlabel("Letter")
plt.ylabel("Count")
plt.savefig("results/plots/exact_count_GE.png")
plt.clf()

fixed_prob_counts_du = pd.read_csv("results/fixed_prob_oliver_twist_DU.txt", sep=" ", header=0)
fixed_prob_counts_eng = pd.read_csv("results/fixed_prob_oliver_twist_ENG.txt", sep=" ", header=0)
fixed_prob_counts_fr = pd.read_csv("results/fixed_prob_oliver_twist_FR.txt", sep=" ", header=0)
fixed_prob_counts_ge = pd.read_csv("results/fixed_prob_oliver_twist_GE.txt", sep=" ", header=0)

plt.bar(fixed_prob_counts_du["letter"], fixed_prob_counts_du["count"], color="orange")
plt.title("Fixed probability counter for Dutch book")
plt.xlabel("Letter")
plt.ylabel("Count")
plt.savefig("results/plots/fixed_prob_count_DU.png")
plt.clf()

plt.bar(fixed_prob_counts_eng["letter"], fixed_prob_counts_eng["count"], color="orange")
plt.title("Fixed probability counter for English book")
plt.xlabel("Letter")
plt.ylabel("Count")
plt.savefig("results/plots/fixed_prob_count_ENG.png")
plt.clf()

plt.bar(fixed_prob_counts_fr["letter"], fixed_prob_counts_fr["count"], color="orange")
plt.title("Fixed probability counter for French book")
plt.xlabel("Letter")
plt.ylabel("Count")
plt.savefig("results/plots/fixed_prob_count_FR.png")
plt.clf()

plt.bar(fixed_prob_counts_ge["letter"], fixed_prob_counts_ge["count"], color="orange")
plt.title("Fixed probability counter for German book")
plt.xlabel("Letter")
plt.ylabel("Count")
plt.savefig("results/plots/fixed_prob_count_GE.png")
plt.clf()

frequent_counts_du = pd.read_csv("results/frequent_count_oliver_twist_DU.txt", sep=" ", header=0)
frequent_counts_eng = pd.read_csv("results/frequent_count_oliver_twist_ENG.txt", sep=" ", header=0)
frequent_counts_fr = pd.read_csv("results/frequent_count_oliver_twist_FR.txt", sep=" ", header=0)
frequent_counts_ge = pd.read_csv("results/frequent_count_oliver_twist_GE.txt", sep=" ", header=0)

k3 = frequent_counts_du[frequent_counts_du["k"] == 3]
k5 = frequent_counts_du[frequent_counts_du["k"] == 5]
k10 = frequent_counts_du[frequent_counts_du["k"] == 10]

plt.bar(k3["letter"], k3["count"], color="green", width=0.2)
plt.title("Frequent counter for Dutch book (k = 3)")
plt.xlabel("Letter")
plt.ylabel("Count")
plt.savefig("results/plots/frequent_count_DU_k3.png")
plt.clf()

plt.bar(k5["letter"], k5["count"], color="yellow", width=0.2)
plt.title("Frequent counter for Dutch book (k = 5)")
plt.xlabel("Letter")
plt.ylabel("Count")
plt.savefig("results/plots/frequent_count_DU_k5.png")
plt.clf()

plt.bar(k10["letter"], k10["count"], color="red", width=0.2)
plt.title("Frequent counter for Dutch book (k = 10)")
plt.xlabel("Letter")
plt.ylabel("Count")
plt.savefig("results/plots/frequent_count_DU_k10.png")
plt.clf()

k3 = frequent_counts_eng[frequent_counts_eng["k"] == 3]
k5 = frequent_counts_eng[frequent_counts_eng["k"] == 5]
k10 = frequent_counts_eng[frequent_counts_eng["k"] == 10]

plt.bar(k3["letter"], k3["count"], color="green", width=0.2)
plt.title("Frequent counter for English book (k = 3)")
plt.xlabel("Letter")
plt.ylabel("Count")
plt.savefig("results/plots/frequent_count_ENG_k3.png")
plt.clf()

plt.bar(k5["letter"], k5["count"], color="yellow", width=0.2)
plt.title("Frequent counter for English book (k = 5)")
plt.xlabel("Letter")
plt.ylabel("Count")
plt.savefig("results/plots/frequent_count_ENG_k5.png")
plt.clf()

plt.bar(k10["letter"], k10["count"], color="red", width=0.2)
plt.title("Frequent counter for English book (k = 10)")
plt.xlabel("Letter")
plt.ylabel("Count")
plt.savefig("results/plots/frequent_count_ENG_k10.png")
plt.clf()

k3 = frequent_counts_fr[frequent_counts_fr["k"] == 3]
k5 = frequent_counts_fr[frequent_counts_fr["k"] == 5]
k10 = frequent_counts_fr[frequent_counts_fr["k"] == 10]

plt.bar(k3["letter"], k3["count"], color="green", width=0.2)
plt.title("Frequent counter for French book (k = 3)")
plt.xlabel("Letter")
plt.ylabel("Count")
plt.savefig("results/plots/frequent_count_FR_k3.png")
plt.clf()

plt.bar(k5["letter"], k5["count"], color="yellow", width=0.2)
plt.title("Frequent counter for French book (k = 5)")
plt.xlabel("Letter")
plt.ylabel("Count")
plt.savefig("results/plots/frequent_count_FR_k5.png")
plt.clf()

plt.bar(k10["letter"], k10["count"], color="red", width=0.2)
plt.title("Frequent counter for French book (k = 10)")
plt.xlabel("Letter")
plt.ylabel("Count")
plt.savefig("results/plots/frequent_count_FR_k10.png")
plt.clf()

k3 = frequent_counts_ge[frequent_counts_ge["k"] == 3]
k5 = frequent_counts_ge[frequent_counts_ge["k"] == 5]
k10 = frequent_counts_ge[frequent_counts_ge["k"] == 10]

plt.bar(k3["letter"], k3["count"], color="green", width=0.2)
plt.title("Frequent counter for German book (k = 3)")
plt.xlabel("Letter")
plt.ylabel("Count")
plt.savefig("results/plots/frequent_count_GE_k3.png")
plt.clf()

plt.bar(k5["letter"], k5["count"], color="yellow", width=0.2)
plt.title("Frequent counter for German book (k = 5)")
plt.xlabel("Letter")
plt.ylabel("Count")
plt.savefig("results/plots/frequent_count_GE_k5.png")
plt.clf()

plt.bar(k10["letter"], k10["count"], color="red", width=0.2)
plt.title("Frequent counter for German book (k = 10)")
plt.xlabel("Letter")
plt.ylabel("Count")
plt.savefig("results/plots/frequent_count_GE_k10.png")
plt.clf()