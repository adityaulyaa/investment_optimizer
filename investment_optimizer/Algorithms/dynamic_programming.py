import sys
import os
from time import perf_counter
from functools import lru_cache

project_root = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

if project_root not in sys.path:
    sys.path.append(project_root)

# =====================================
# IMPORT MODEL
# =====================================

from Models.investment_model import (
    ALLOCATION_STEP,
    create_solution,
    is_valid_allocation
)


def dynamic_programming(
    modal,
    risk_limit=4.0
):

    start_time = perf_counter()

    states_visited = 0

    @lru_cache(maxsize=None)
    def dp(tabungan, emas):

        nonlocal states_visited

        states_visited += 1

        reksa = 100 - tabungan - emas

        if reksa < 0:
            return None

        if not is_valid_allocation(
            tabungan,
            emas,
            reksa,
            risk_limit
        ):
            return None

        solution = create_solution(
            tabungan,
            emas,
            reksa,
            modal
        )

        return solution

    best_solution = None
    best_wealth = float("-inf")
    all_valid_solutions = []

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

            result = dp(
                tabungan,
                emas
            )

            if result is None:
                continue

            all_valid_solutions.append(
                result
            )

            if result["wealth"] > best_wealth:
                best_wealth = result["wealth"]
                best_solution = result

    runtime = perf_counter() - start_time

    all_valid_solutions.sort(
        key=lambda x: x["wealth"],
        reverse=True
    )

    top_3 = all_valid_solutions[:3]

    return {
        "algorithm": "Dynamic Programming",

        "risk_limit": risk_limit,

        "tabungan": best_solution["tabungan"],
        "emas": best_solution["emas"],
        "reksa": best_solution["reksa"],

        "wealth": best_solution["wealth"],
        "risk": best_solution["risk"],

        "runtime": runtime,

        "total_generated": states_visited,
        "invalid_count": (
            states_visited
            - len(all_valid_solutions)
        ),
        "valid_count": len(
            all_valid_solutions
        ),

        "top_3": top_3
    }


if __name__ == "__main__":

    result = dynamic_programming(
        100_000_000
    )

    print(
        "\n=== DYNAMIC PROGRAMMING ==="
    )

    print(
        f"Total Kombinasi Dibangkitkan : {result['total_generated']}"
    )

    print(
        f"Kombinasi Tidak Valid        : {result['invalid_count']}"
    )

    print(
        f"Kombinasi Valid              : {result['valid_count']}"
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