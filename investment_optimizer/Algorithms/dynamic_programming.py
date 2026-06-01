import sys
import os
from time import perf_counter
from functools import lru_cache

# =====================================
# FIX IMPORT PROJECT ROOT
# =====================================

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


def dynamic_programming(modal):

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
            reksa
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

            if result["wealth"] > best_wealth:
                best_wealth = result["wealth"]
                best_solution = result

    runtime = perf_counter() - start_time

    return {
        "algorithm": "Dynamic Programming",
        "tabungan": best_solution["tabungan"],
        "emas": best_solution["emas"],
        "reksa": best_solution["reksa"],
        "wealth": best_solution["wealth"],
        "risk": best_solution["risk"],
        "runtime": runtime,
        "states_visited": states_visited
    }


if __name__ == "__main__":

    result = dynamic_programming(
        100_000_000
    )

    print("\n=== DYNAMIC PROGRAMMING ===")

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
        f"States   : {result['states_visited']}"
    )