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

    all_valid_solutions = []

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

            all_valid_solutions.append(
                solution
            )

            if solution["wealth"] > best_wealth:
                best_wealth = solution["wealth"]
                best_solution = solution

    runtime = perf_counter() - start_time

    # Urutkan berdasarkan wealth
    all_valid_solutions.sort(
        key=lambda x: x["wealth"],
        reverse=True
    )

    top_3 = all_valid_solutions[:3]

    result = {
        "algorithm": "Branch and Bound",

        "tabungan": best_solution["tabungan"],
        "emas": best_solution["emas"],
        "reksa": best_solution["reksa"],

        "wealth": best_solution["wealth"],
        "risk": best_solution["risk"],

        "runtime": runtime,

        "total_generated": explored_nodes,
        "pruned_count": pruned_nodes,
        "valid_count": len(all_valid_solutions),

        "top_3": top_3
    }

    return result


if __name__ == "__main__":

    result = branch_and_bound(
        100_000_000
    )

    print("\n=== BRANCH AND BOUND ===")

    print(
        f"Total Kombinasi Dibangkitkan : {result['total_generated']}"
    )

    print(
        f"Kombinasi Terpruning         : {result['pruned_count']}"
    )

    print(
        f"Kombinasi Valid             : {result['valid_count']}"
    )

    print("\nTOP 3 SOLUSI")

    for i, sol in enumerate(
        result["top_3"],
        start=1
    ):

        print(f"\n#{i}")

        print(
            f"Tabungan : {sol['tabungan']}%"
        )

        print(
            f"Emas     : {sol['emas']}%"
        )

        print(
            f"Reksa    : {sol['reksa']}%"
        )

        print(
            f"Risk     : {sol['risk']:.2f}"
        )

        print(
            f"Wealth   : Rp {sol['wealth']:,.2f}"
        )

    print(
        f"\nRuntime  : {result['runtime']:.6f} detik"
    )