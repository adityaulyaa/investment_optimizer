import sys
import os

# =====================================
# FIX PROJECT ROOT
# =====================================

project_root = os.path.dirname(
    os.path.abspath(__file__)
)

if project_root not in sys.path:
    sys.path.append(project_root)

# =====================================
# IMPORT ALGORITHMS
# =====================================

from Algorithms.branch_bound import (
    branch_and_bound
)

from Algorithms.dynamic_programming import (
    dynamic_programming
)

from Algorithms.genetic_algorithm import (
    genetic_algorithm
)

# =====================================
# IMPORT UTILS
# =====================================

from Utils.metrics import (
    print_result,
    print_comparison_table
)


def run_all_algorithms(modal):

    print("\n")
    print("=" * 100)

    print(
        f"OPTIMASI INVESTASI - MODAL Rp {modal:,.0f}"
    )

    print("=" * 100)

    # =====================
    # JALANKAN ALGORITMA
    # =====================

    bb_result = branch_and_bound(
        modal
    )

    dp_result = dynamic_programming(
        modal
    )

    ga_result = genetic_algorithm(
        modal
    )

    results = [
        bb_result,
        dp_result,
        ga_result
    ]

    # =====================
    # DETAIL HASIL
    # =====================

    for result in results:

        print_result(
            result
        )

        print("\n" + "-" * 100)

    # =====================
    # TABEL PERBANDINGAN
    # =====================

    print_comparison_table(
        results
    )

    return results


if __name__ == "__main__":

    scenarios = [
        10_000_000,
        100_000_000,
        1_000_000_000
    ]

    all_results = []

    for i, modal in enumerate(
        scenarios,
        start=1
    ):

        print("\n")
        print("#" * 100)

        print(
            f"SCENARIO {i}"
        )

        print(
            f"MODAL = Rp {modal:,.0f}"
        )

        print("#" * 100)

        results = run_all_algorithms(
            modal
        )

        all_results.append({
            "scenario": i,
            "modal": modal,
            "results": results
        })