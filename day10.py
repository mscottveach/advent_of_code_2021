import statistics

OPENING_SYMBOLS = ['{', '(', '[', '<']
CLOSING_SYMBOLS = ['}', ')', ']', '>']
MATCHING_SYMBOL = {'}':'{', ')':'(', ']':'[', '>':'<'}
MATCHING_SYMBOL_REV = {'{':'}', '(':')', '[':']', '<':'>'}
SCORES = {'}':1197, ')':3,']':57,'>':25137}
PART_TWO_SCORES = {'}':3, ')':1, ']':2, '>':4}

def check_for_corrupted():

    corrupted = []
    the_comp_scores = []
    with open('10-1-input.txt') as f:
        line = f.readline()

        while line:
            stack = []
            is_corrupted = False
            for char in line:
                if char in OPENING_SYMBOLS:
                    stack.append(char)
                elif char in CLOSING_SYMBOLS:
                    if MATCHING_SYMBOL[char] == stack[-1]:
                        stack.pop()
                    else:
                        corrupted.append(char)
                        is_corrupted = True
                        break
            completion = []
            comp_score = 0
            if not is_corrupted:
                while len(stack) > 0:
                    a_char = stack.pop()
                    completion.append(MATCHING_SYMBOL_REV[a_char])
                for elem in completion:
                    comp_score *= 5
                    comp_score += PART_TWO_SCORES[elem]
                if comp_score > 0:
                    the_comp_scores.append(comp_score)
            line = f.readline()

    score = 0
    for char in corrupted:
        score += SCORES[char]
    print(score)

    the_comp_scores = sorted(the_comp_scores)
    final_comp_score = statistics.median(the_comp_scores)
    print(final_comp_score)

if __name__ == '__main__':
    check_for_corrupted()