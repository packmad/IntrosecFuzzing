def is_perfect_number(n: int) -> bool:
    div_sum = 1
    for i in range(2, n//2+1):
        if n % i == 0:
            div_sum += i
    return div_sum == n and div_sum != 1


def first_odd_perfect_number() -> int:
    i = 1
    while True:
        i += 2
        print('Testing:', i)
        if is_perfect_number(i):
            return i


if __name__ == "__main__":
    pn = list()
    for x in range(0, 10000):
        if is_perfect_number(x):
            pn.append(x)
    assert pn == [6, 28, 496, 8128]
    assert first_odd_perfect_number() % 2 == 1
