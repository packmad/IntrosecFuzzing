from myfuzzer.Coverage import StatementCoverage
from myfuzzer.Fuzzer import MutationCoverageFuzzer
from myfuzzer.Runner import FunctionCoverageRunner


def shipping_cost(weight, distance):

    if weight <= 0:
        return 0
    elif weight <= 5:
        cost = 10
    elif weight <= 10:
        cost = 15
    else:
        cost = 20
    if distance <= 0:
        return 0
    elif distance <= 100:
        cost += 5
    elif distance <= 500:
        cost += 10
    else:
        cost += 20
    return cost


if __name__ == '__main__':
    mutation_fuzzer = MutationCoverageFuzzer(seed=[(1, 2)])
    runner = FunctionCoverageRunner(shipping_cost, StatementCoverage)
    mutation_fuzzer.runs(runner, trials=100)
    print(mutation_fuzzer.population)
    print(runner.coverage())
