import csv

with open('/content/sample_data/mnist_train_small.csv', 'r') as file:
    reader = csv.reader(file)

import one_gram_reader
import matplotlib.pyplot as plt

def n_counts(years, counts, total):
    n_c = []
    for i in range(len(years)):
        n_c.append(counts[i]/total[years[i]])
    return n_c
    
def p_words(words, year_range, wfile, tfile):
    cls = ["b", "g", "r", "y", "p", "o"]
    a = 0
    for w in words:
        n = w
        years, counts = one_gram_reader.read_wfile(w, year_range, wfile)
        total = one_gram_reader.read_total_counts(tfile)
        n_c = n_c(years, counts, total)
        cl = cls[a]
        a += 1
        plt.xlabel("Year")
        plt.ylabel("Relative frequency")
        plt.plot(years, n_c, cl, label = n)
    plt.legend(framealpha=1, frameon=True)
    plt.grid(cl='#828835', linestyle='dashed', linewidth=0.5)
    plt.show()
