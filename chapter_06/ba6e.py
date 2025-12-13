# BA6E: Shared k-mers

from collections import defaultdict

def revcomp(s: str) -> str:
    comp = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    return ''.join(comp[c] for c in reversed(s))

def shared_kmers(k: int, s: str, t: str):
    pos_in_t = defaultdict(list)
    for y in range(len(t) - k + 1):
        pos_in_t[t[y:y+k]].append(y)

    out = []
    for x in range(len(s) - k + 1):
        kmer = s[x:x+k]
        rk = revcomp(kmer)

        # direct match
        for y in pos_in_t.get(kmer, []):
            out.append((x, y))

        # reverse-complement match (avoid double counting when kmer == rk)
        if rk != kmer:
            for y in pos_in_t.get(rk, []):
                out.append((x, y))

    return out

def main():
    try:
        with open("input/rosalind_ba6e.txt", "r") as f:
            data = f.read().strip().split('\n')
            k = int(data[0])
            s = data[1]
            t = data[2]
    except:
        k = 3
        s = "AAACTCATC"
        t = "TTTCAAATC"


    pairs = shared_kmers(k, s, t)
    print("\n".join(f"({x}, {y})" for x, y in pairs))
    with open("output/6e.txt", "w") as f:
        f.write("\n".join(f"({x}, {y})" for x, y in pairs))

if __name__ == "__main__":
    main()
