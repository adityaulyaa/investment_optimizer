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

def generate_individual():

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
            reksa
        ):
            return (
                tabungan,
                emas,
                reksa
            )


# =====================================
# FITNESS
# =====================================

def fitness(individual, modal):

    t, e, r = individual

    if not is_valid_allocation(
        t,
        e,
        r
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
    k=3
):

    candidates = random.sample(
        population,
        k
    )

    return max(
        candidates,
        key=lambda ind:
        fitness(ind, modal)
    )


# =====================================
# CROSSOVER
# =====================================

def crossover(parent1, parent2):

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
        child_r
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

def mutate(individual):

    if random.random() > MUTATION_RATE:
        return individual

    return generate_individual()


# =====================================
# MAIN GA
# =====================================

def genetic_algorithm(modal):

    start_time = perf_counter()

    population = [
        generate_individual()
        for _ in range(
            POPULATION_SIZE
        )
    ]

    best_individual = None
    best_fitness = 0

    for _ in range(
        GENERATIONS
    ):

        new_population = []

        for _ in range(
            POPULATION_SIZE
        ):

            parent1 = tournament_selection(
                population,
                modal
            )

            parent2 = tournament_selection(
                population,
                modal
            )

            child = crossover(
                parent1,
                parent2
            )

            child = mutate(
                child
            )

            new_population.append(
                child
            )

        population = new_population

        generation_best = max(
            population,
            key=lambda ind:
            fitness(
                ind,
                modal
            )
        )

        generation_fitness = fitness(
            generation_best,
            modal
        )

        if generation_fitness > best_fitness:

            best_fitness = generation_fitness

            best_individual = generation_best

    runtime = (
        perf_counter()
        - start_time
    )

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

        "generations":
            GENERATIONS
    }


if __name__ == "__main__":

    result = genetic_algorithm(
        100_000_000
    )

    print(
        "\n=== GENETIC ALGORITHM ==="
    )

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
        f"Generasi : {result['generations']}"
    )