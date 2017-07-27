# Open a file with integers in it, if file has a filename,
# open it and recurse
# sum all numbers and return average
import sys

def sum_terms_from_file(fn, total_sum=0, terms=0):
    total_sum = total_sum
    terms = terms
    for line in iter(open(fn)):
        line = line.strip()
        if line.isdigit():
            terms += 1
            total_sum += int(line)
        else:
            total_sum, terms = sum_terms_from_file(line, total_sum, terms)
    return (total_sum, terms)

def total_avg(fn):
    total_sum, terms = sum_terms_from_file(fn)
    return total_sum/terms

if __name__ == "__main__":
    print total_avg(sys.argv[1])
