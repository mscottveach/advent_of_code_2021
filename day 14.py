from collections import Counter


def apply_insertions():
    rules = {}
    poly_counts = {}
    letter_counts = {}
    with open('14-1-input.txt') as f:
        polymer = f.readline().strip()
        f.readline()
        poly_len = len(polymer)
        for char in polymer:
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1

        line = f.readline()
        while line:
            x,y = (line.strip()).split(' -> ')
            #print(x, y)
            rules[x] = y.strip()
            poly_counts[x] = 0
            line = f.readline()

    poly_len = len(polymer)
    for idx, a_poly in enumerate(polymer):
        if idx < (poly_len - 1):
            polydex = a_poly.strip() + polymer[idx + 1].strip()
            poly_counts[polydex] += 1

    print(poly_counts)
    for idx in range(0,40):
        print(idx)
        new_poly_counts = {}
        for key in poly_counts:
            if poly_counts[key] > 0:
                insertion = rules[key]
                new_key_a = key[0] + insertion
                new_key_b = insertion + key[1]
                if insertion in letter_counts:
                    letter_counts[insertion] += poly_counts[key]
                else:
                    letter_counts[insertion] = poly_counts[key]
                if new_key_a in new_poly_counts:
                    new_poly_counts[new_key_a] += poly_counts[key]
                else:
                    new_poly_counts[new_key_a] = poly_counts[key]
                if new_key_b in new_poly_counts:
                    new_poly_counts[new_key_b] += poly_counts[key]
                else:
                    new_poly_counts[new_key_b] = poly_counts[key]
        poly_counts = new_poly_counts

    print(letter_counts)
    max_idx = max(letter_counts, key=letter_counts.get)
    min_idx = min(letter_counts, key=letter_counts.get)
    print(letter_counts[max_idx] - letter_counts[min_idx])

    # for i in range(0, 40):
        #     print(i)
        #     poly_len = len(polymer)
        #     new_polymer = ''
        #
        #     polymer = new_polymer
        #
        # res = Counter(polymer)
        # max_idx = max(res, key=res.get)
        # min_idx = min(res, key=res.get)
        # print(res[max_idx] - res[min_idx])


if __name__ == '__main__':
    apply_insertions()