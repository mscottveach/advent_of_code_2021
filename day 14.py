from collections import Counter

def apply_insertions():
    rules = {}
    with open('14-1-input.txt') as f:
        polymer = f.readline().strip()
        f.readline()
        line = f.readline()
        while line:
            x,y = (line.strip()).split(' -> ')
            #print(x, y)
            rules[x] = y.strip()
            line = f.readline()

        print(rules)

        for i in range(0, 10):
            poly_len = len(polymer)
            new_polymer = ''
            for idx, a_poly in enumerate(polymer):
                if idx == (poly_len - 1):
                    new_polymer += a_poly
                else:
                    polydex = a_poly.strip() + polymer[idx + 1].strip()
                    insertion = rules[polydex]
                    new_polymer += a_poly + insertion
            polymer = new_polymer

        res = Counter(polymer)
        max_idx = max(res, key=res.get)
        min_idx = min(res, key=res.get)
        print(res[max_idx] - res[min_idx])


if __name__ == '__main__':
    apply_insertions()