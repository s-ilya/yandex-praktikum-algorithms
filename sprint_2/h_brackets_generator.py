def generate_parenthesis(n, current='', opened=0, closed=0, collected=None):
    if collected is None:
        collected = set()

    if closed == n:
        collected.add(current)

    if opened < n:
        generate_parenthesis(n, current=current + '(', opened=opened + 1, closed=closed, collected=collected)

    if closed < opened:
        generate_parenthesis(n, current=current + ')', opened=opened, closed=closed + 1, collected=collected)

    return collected


if __name__ == '__main__':
    with open('input.txt', mode='r') as input_txt, open('output.txt', mode='w') as output_txt:
        n = int(input_txt.readline())
        output_txt.write('\n'.join(sorted(generate_parenthesis(n))))
