"""
investment_model.py

Model investasi yang digunakan oleh:
- Branch and Bound
- Dynamic Programming
- Genetic Algorithm

Penelitian:
Analisis Komparatif Branch and Bound, Dynamic Programming,
dan Genetic Algorithm dalam Optimasi Alokasi Portofolio Investasi
"""

# =========================
# PARAMETER INVESTASI
# =========================

RETURN_TABUNGAN = 0.04
RETURN_EMAS = 0.08
RETURN_REKSA = 0.12

RISIKO_TABUNGAN = 1
RISIKO_EMAS = 3
RISIKO_REKSA = 6

YEARS = 5

# Constraint
MIN_TABUNGAN = 10
MAX_REKSA = 50
ALLOCATION_STEP = 5

# Batas risiko portofolio
RISK_LIMIT = 4.0


# =========================
# PERHITUNGAN WEALTH
# =========================

def calculate_wealth(tabungan_pct, emas_pct, reksa_pct, modal):
    """
    Menghitung total kekayaan akhir setelah 5 tahun.

    Parameters
    ----------
    tabungan_pct : int
    emas_pct : int
    reksa_pct : int
    modal : float

    Returns
    -------
    float
    """

    tabungan_amount = modal * (tabungan_pct / 100)
    emas_amount = modal * (emas_pct / 100)
    reksa_amount = modal * (reksa_pct / 100)

    wealth_tabungan = tabungan_amount * ((1 + RETURN_TABUNGAN) ** YEARS)
    wealth_emas = emas_amount * ((1 + RETURN_EMAS) ** YEARS)
    wealth_reksa = reksa_amount * ((1 + RETURN_REKSA) ** YEARS)

    total_wealth = (
        wealth_tabungan
        + wealth_emas
        + wealth_reksa
    )

    return total_wealth


# =========================
# PERHITUNGAN RISIKO
# =========================

def calculate_risk(tabungan_pct, emas_pct, reksa_pct):
    """
    Menghitung skor risiko portofolio.

    Risk =
    (T * 1) +
    (E * 3) +
    (R * 6)

    menggunakan proporsi 0-1
    """

    risk = (
        (tabungan_pct / 100) * RISIKO_TABUNGAN
        + (emas_pct / 100) * RISIKO_EMAS
        + (reksa_pct / 100) * RISIKO_REKSA
    )

    return risk


# =========================
# VALIDASI CONSTRAINT
# =========================

def is_valid_allocation(tabungan_pct, emas_pct, reksa_pct):
    """
    Memeriksa apakah kombinasi alokasi valid.
    """

    # Total harus 100%
    if (tabungan_pct + emas_pct + reksa_pct) != 100:
        return False

    # Minimum tabungan
    if tabungan_pct < MIN_TABUNGAN:
        return False

    # Maksimum reksa dana
    if reksa_pct > MAX_REKSA:
        return False

    # Kelipatan 5%
    allocations = [tabungan_pct, emas_pct, reksa_pct]

    for value in allocations:
        if value % ALLOCATION_STEP != 0:
            return False

    # Constraint risiko
    risk = calculate_risk(
        tabungan_pct,
        emas_pct,
        reksa_pct
    )

    if risk > RISK_LIMIT:
        return False

    return True


# =========================
# REPRESENTASI SOLUSI
# =========================

def create_solution(tabungan_pct, emas_pct, reksa_pct, modal):
    """
    Membuat objek solusi lengkap.
    """

    wealth = calculate_wealth(
        tabungan_pct,
        emas_pct,
        reksa_pct,
        modal
    )

    risk = calculate_risk(
        tabungan_pct,
        emas_pct,
        reksa_pct
    )

    return {
        "tabungan": tabungan_pct,
        "emas": emas_pct,
        "reksa": reksa_pct,
        "wealth": wealth,
        "risk": risk
    }


# =========================
# TEST SEDERHANA
# =========================

if __name__ == "__main__":

    modal = 100_000_000

    solution = create_solution(
        10,
        40,
        50,
        modal
    )

    print("=== TEST MODEL ===")
    print(solution)
    print(is_valid_allocation(10,40,50))