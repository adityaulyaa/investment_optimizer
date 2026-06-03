import sys
import os
import random
from time import perf_counter

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
    create_solution,
    is_valid_allocation
)

# =====================================
# PARAMETER GA
# =====================================

POPULATION_SIZE = 50
GENERATIONS = 100

CROSSOVER_RATE = 0.8
MUTATION_RATE = 0.1


# =====================================
# MEMBUAT INDIVIDU VALID
# =====================================

def generate_individual(
    risk_limit=4.0
):

    while True:

        tabungan = random.choice(
            range(10, 101, 5)
        )

        emas = random.choice(
            range(0, 101 - tabungan, 5)
        )

        reksa = 100 - tabungan - emas

        if is_valid_allocation(
            tabungan,
            emas,
            reksa,
            risk_limit
        ):
            return (
                tabungan,
                emas,
                reksa
            )


# =====================================
# FITNESS
# =====================================

def fitness(
    individual,
    modal,
    risk_limit=4.0
):

    t, e, r = individual

    if not is_valid_allocation(
        t,
        e,
        r,
        risk_limit
    ):
        return 0

    return create_solution(
        t,
        e,
        r,
        modal
    )["wealth"]


# =====================================
# SELEKSI
# =====================================

def tournament_selection(
    population,
    modal,
    risk_limit=4.0,
    k=3
):

    candidates = random.sample(
        population,
        k
    )

    return max(
        candidates,
        key=lambda ind:
        fitness(
            ind,
            modal,
            risk_limit
        )
    )


# =====================================
# CROSSOVER
# =====================================

def crossover(
    parent1,
    parent2,
    risk_limit=4.0
):

    if random.random() > CROSSOVER_RATE:
        return parent1

    t1, e1, r1 = parent1
    t2, e2, r2 = parent2

    child_t = t1
    child_e = e2

    child_r = 100 - child_t - child_e

    if is_valid_allocation(
        child_t,
        child_e,
        child_r,
        risk_limit
    ):
        return (
            child_t,
            child_e,
            child_r
        )

    return parent1


# =====================================
# MUTASI
# =====================================

def mutate(
    individual,
    risk_limit=4.0
):

    if random.random() > MUTATION_RATE:
        return individual

    return generate_individual(
        risk_limit
    )


# =====================================
# MAIN GA
# =====================================

def genetic_algorithm(
    modal,
    risk_limit=4.0
):

    start_time = perf_counter()

    population = [
        generate_individual(
            risk_limit
        )
        for _ in range(
            POPULATION_SIZE
        )
    ]

    best_individual = None
    best_fitness = 0
    all_individuals = []

    for _ in range(
        GENERATIONS
    ):

        new_population = []

        for _ in range(
            POPULATION_SIZE
        ):

            parent1 = tournament_selection(
                population,
                modal,
                risk_limit
            )

            parent2 = tournament_selection(
                population,
                modal,
                risk_limit
            )

            child = crossover(
                parent1,
                parent2,
                risk_limit
            )

            child = mutate(
                child,
                risk_limit
            )

            new_population.append(
                child
            )

        population = new_population

        all_individuals.extend(
            population
        )

        generation_best = max(
            population,
            key=lambda ind:
            fitness(
                ind,
                modal,
                risk_limit
            )
        )

        generation_fitness = fitness(
            generation_best,
            modal,
            risk_limit
        )

        if generation_fitness > best_fitness:

            best_fitness = generation_fitness

            best_individual = generation_best

    runtime = (
        perf_counter()
        - start_time
    )

    unique_solutions = []

    seen = set()

    for individual in all_individuals:

        t, e, r = individual

        key = (t, e, r)

        if key in seen:
            continue

        seen.add(key)

        solution = create_solution(
            t,
            e,
            r,
            modal
        )

        unique_solutions.append(
            solution
        )

    unique_solutions.sort(
        key=lambda x: x["wealth"],
        reverse=True
    )

    top_3 = unique_solutions[:3]

    t, e, r = best_individual

    solution = create_solution(
        t,
        e,
        r,
        modal
    )

    return {
        "algorithm":
            "Genetic Algorithm",

        "risk_limit":
            risk_limit,

        "tabungan":
            solution["tabungan"],

        "emas":
            solution["emas"],

        "reksa":
            solution["reksa"],

        "wealth":
            solution["wealth"],

        "risk":
            solution["risk"],

        "runtime":
            runtime,

        # =====================
        # DATA UNTUK GUI
        # =====================

        "total_generated":
            len(all_individuals),

        "valid_count":
            len(unique_solutions),

        "invalid_count":
            len(all_individuals)
            - len(unique_solutions),

        # =====================
        # DATA KHUSUS GA
        # =====================

        "population_size":
            POPULATION_SIZE,

        "generations":
            GENERATIONS,

        "individuals_evaluated":
            len(all_individuals),

        "top_3":
            top_3
    }


if __name__ == "__main__":

    result = genetic_algorithm(
        100_000_000
    )

    print(
        "\n=== GENETIC ALGORITHM ==="
    )

    print(
        f"Population Size           : {result['population_size']}"
    )

    print(
        f"Generations               : {result['generations']}"
    )

    print(
        f"Individuals Evaluated     : {result['individuals_evaluated']}"
    )

    print(
        f"Solusi Valid              : {result['valid_count']}"
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