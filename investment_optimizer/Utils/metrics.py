# =====================================
# FORMAT CURRENCY
# =====================================

def format_currency(value):

    return f"Rp {value:,.2f}"


# =====================================
# PRINT TOP 3
# =====================================

def print_top_3(top_3):

    print("\nTOP 3 SOLUSI")

    for i, sol in enumerate(
        top_3,
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
            f"Wealth   : {format_currency(sol['wealth'])}"
        )


# =====================================
# PRINT SINGLE RESULT
# =====================================

def print_result(result):

    print(
        f"\n=== {result['algorithm'].upper()} ==="
    )

    # ==========================
    # BRANCH & BOUND
    # ==========================

    if result["algorithm"] == "Branch and Bound":

        print(
            f"Total Kombinasi Dibangkitkan : {result['total_generated']}"
        )

        print(
            f"Kombinasi Terpruning         : {result['pruned_count']}"
        )

        print(
            f"Kombinasi Valid              : {result['valid_count']}"
        )

    # ==========================
    # DYNAMIC PROGRAMMING
    # ==========================

    elif result["algorithm"] == "Dynamic Programming":

        print(
            f"Total Kombinasi Dibangkitkan : {result['total_generated']}"
        )

        print(
            f"Kombinasi Tidak Valid        : {result['invalid_count']}"
        )

        print(
            f"Kombinasi Valid              : {result['valid_count']}"
        )

    # ==========================
    # GENETIC ALGORITHM
    # ==========================

    elif result["algorithm"] == "Genetic Algorithm":

        print(
            f"Population Size             : {result['population_size']}"
        )

        print(
            f"Generations                 : {result['generations']}"
        )

        print(
            f"Individuals Evaluated       : {result['individuals_evaluated']}"
        )

        print(
            f"Solusi Valid                : {result['valid_count']}"
        )

    # ==========================
    # TOP 3
    # ==========================

    print_top_3(
        result["top_3"]
    )

    # ==========================
    # BEST SOLUTION
    # ==========================

    print("\nBEST SOLUTION")

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
        f"Risk     : {result['risk']:.2f}"
    )

    print(
        f"Wealth   : {format_currency(result['wealth'])}"
    )

    print(
        f"Runtime  : {result['runtime']:.6f} detik"
    )


# =====================================
# PRINT COMPARISON TABLE
# =====================================

def print_comparison_table(results):

    print("\n")
    print("=" * 100)

    print(
        "PERBANDINGAN ALGORITMA"
    )

    print("=" * 100)

    print(
        f"{'Algorithm':<25}"
        f"{'Tabungan':<12}"
        f"{'Emas':<10}"
        f"{'Reksa':<10}"
        f"{'Risk':<10}"
        f"{'Runtime':<15}"
    )

    print("-" * 100)

    for result in results:

        print(
            f"{result['algorithm']:<25}"
            f"{str(result['tabungan']) + '%':<12}"
            f"{str(result['emas']) + '%':<10}"
            f"{str(result['reksa']) + '%':<10}"
            f"{result['risk']:<10.2f}"
            f"{result['runtime']:<15.6f}"
        )

    print("=" * 100)