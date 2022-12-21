import csv

import one_gram_reader
import matplotlib.pyplot as plt

import random as random

def normalized_counts(years, counts, total):
    years, counts = one_gram_reader.read_wfile(word, year_range, wfile)
    total = one_gram_reader.read_total_counts(tfile)
    nc = []
    for i in range(len(counts)):
        nc.append(counts[i]/total[years[i]])
    return nc
    
def plot_words(words, year_range, wfile, tfile):
    r = random.random()
    b = random.random()
    g = random.random()
    color = (r,b,g)
    for word in words:
        years, counts = one_gram_reader.read_wfile(word, year_range, wfile)
        total = one_gram_reader.read_total_counts(tfile)
        nc = normalized_counts(years, counts, total)
        
    plt.figure()
    plt.xlabel("Year")
    plt.ylabel("Relative frequency")
    plt.plot(years, nc, c = color)
    plt.legend(word)
    plt.grid(linestyle='dashed', linewidth=0.5)
    plt.show()
