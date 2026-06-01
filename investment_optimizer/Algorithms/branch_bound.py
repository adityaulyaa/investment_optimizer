import sys
import os
from time import perf_counter

project_root = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

if project_root not in sys.path:
    sys.path.append(project_root)

from Models.investment_model import (
    ALLOCATION_STEP,
    create_solution,
    is_valid_allocation
)


def branch_and_bound(modal):
    """
    Branch and Bound untuk mencari
    kombinasi investasi terbaik.
    """

    start_time = perf_counter()

    best_solution = None
    best_wealth = float("-inf")

    explored_nodes = 0
    pruned_nodes = 0

    # Branching
    for tabungan in range(
        10,
        101,
        ALLOCATION_STEP
    ):

        for emas in range(
            0,
            101 - tabungan,
            ALLOCATION_STEP
        ):

            reksa = 100 - tabungan - emas

            explored_nodes += 1

            # Pruning
            if not is_valid_allocation(
                tabungan,
                emas,
                reksa
            ):
                pruned_nodes += 1
                continue

            solution = create_solution(
                tabungan,
                emas,
                reksa,
                modal
            )

            if solution["wealth"] > best_wealth:
                best_wealth = solution["wealth"]
                best_solution = solution

    runtime = perf_counter() - start_time

    result = {
        "algorithm": "Branch and Bound",
        "tabungan": best_solution["tabungan"],
        "emas": best_solution["emas"],
        "reksa": best_solution["reksa"],
        "wealth": best_solution["wealth"],
        "risk": best_solution["risk"],
        "runtime": runtime,
        "explored_nodes": explored_nodes,
        "pruned_nodes": pruned_nodes
    }

    return result


if __name__ == "__main__":

    result = branch_and_bound(
        100_000_000
    )

    print("\n=== BRANCH AND BOUND ===")

    print(
        f"Tabungan : {result['tabungan']}%"
    )

    print(
        f"Emas     : {result['emas']}%"
    )

    print(
        f"Reksa    : {result['reksa']}%"
    )

    print(
        f"Wealth   : Rp {result['wealth']:,.2f}"
    )

    print(
        f"Risk     : {result['risk']:.2f}"
    )

    print(
        f"Runtime  : {result['runtime']:.6f} detik"
    )

    print(
        f"Explored : {result['explored_nodes']}"
    )

    print(
        f"Pruned   : {result['pruned_nodes']}"
    )