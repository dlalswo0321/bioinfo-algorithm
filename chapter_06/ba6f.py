# BA6F: Chromosome to Cycle
def parse_chromosome(line: str):
    # "(+1 -2 -3 +4)" → [1, -2, -3, 4]
    line = line.strip()
    line = line[1:-1]
    return list(map(int, line.split()))

def chromosome_to_cycle(chrom):
    nodes = []
    for i in chrom:
        if i > 0:
            nodes.append(2*i - 1)
            nodes.append(2*i)
        else:
            i = -i
            nodes.append(2*i)
            nodes.append(2*i - 1)
    return nodes

def main():
    try:
        with open("input/rosalind_ba6f.txt", "r") as f:
            line = f.readline().strip()
    except:
        line = "(+1 -2 -3 +4)"
    chrom = parse_chromosome(line)
    nodes = chromosome_to_cycle(chrom)
    print("(" + " ".join(map(str, nodes)) + ")")

if __name__ == "__main__":
    main()
