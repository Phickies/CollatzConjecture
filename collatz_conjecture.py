def collatz(n: int) -> int:
    if n % 2 == 0:
        return int(n/2)
    else:
        return n*3 + 1


def collatz_step_count(n: int) -> int:
    step_count = 0
    while n != 1:
        n = collatz(n)
        step_count += 1
    return step_count
