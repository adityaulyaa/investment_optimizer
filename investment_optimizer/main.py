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


def run_all_algorithms(
    modal,
    risk_limit
):

    print("\n")
    print("=" * 100)

    print(
        f"OPTIMASI INVESTASI - MODAL Rp {modal:,.0f}"
    )

    print(
        f"Risk Limit : {risk_limit}"
    )

    print("=" * 100)

    # =====================
    # JALANKAN ALGORITMA
    # =====================

    bb_result = branch_and_bound(
        modal,
        risk_limit
    )

    dp_result = dynamic_programming(
        modal,
        risk_limit
    )

    ga_result = genetic_algorithm(
        modal,
        risk_limit
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

    MODAL = 100_000_000

    risk_scenarios = [
        3.5,
        4.0,
        4.5
    ]

    all_results = []

    for i, risk_limit in enumerate(
        risk_scenarios,
        start=1
    ):

        print("\n")
        print("#" * 100)

        print(
            f"SCENARIO {i}"
        )

        print(
            f"MODAL = Rp {MODAL:,.0f}"
        )

        print(
            f"RISK LIMIT = {risk_limit}"
        )

        print("#" * 100)

        results = run_all_algorithms(
            MODAL,
            risk_limit
        )

        all_results.append({
            "scenario": i,
            "risk_limit": risk_limit,
            "results": results
        })