# listfunctions.py

def minmax(seq):
    return min(seq), max(seq)

if __name__ == "__main__":
    s = [10, 20, 30, 40]
    minV, maxV = minmax(s)
    print minV, maxV
