import random

import sympy

from .meta import GeneratedDataIncorrect, Problem


def seznam_polovic(od=-10, do=10):
    """
    Funkcija sestavi seznam vseh celih iz polovic med vrednostima od in do (brez 0).
    [1/2, 1, 3/2, 2, 5/2, 3, 7/2]
    """
    return [sympy.Rational(x, 2) for x in range(2 * od, 2 * (do + 1)) if x != 0]


def seznam_tretjin(od=-10, do=10):
    """
    >>> seznam_tretjin(od=0, do=3)
    [1/3, 2/3, 1, 4/3, 5/3, 2, 7/3, 8/3, 3, 10/3, 11/3]
    """
    return [sympy.Rational(x, 3) for x in range(3 * od, 3 * (do + 1)) if x != 0]


def generiraj_nicelno_obliko_kvadratne(od=-5, do=5):
    """
    Vrne naključno kvadratno funkcijo v ničelni obliki.
    >>> nicelna_oblika(od=-2)
    (2, -2, 3/2, 2*(x - 3/2)*(x + 2))
    """

    a = random.choice(seznam_polovic(-4, 4) + seznam_tretjin(-4, 4))
    x1 = random.choice(seznam_polovic(od, do) + seznam_tretjin(od, do))
    x2 = random.choice(seznam_polovic(od, do) + seznam_tretjin(od, do))
    x = sympy.symbols("x")
    # nicelna = a * (x - x1) * (x - x2)
    nicelna = sympy.Mul(a, x - x1, x - x2, evaluate=False)
    return (a, x1, x2, nicelna)


def generiraj_splosno_obliko_kvadratne():
    """
    Vrne naključno kvadratno funkcijo v splošni obliki.
    """

    x = sympy.symbols("x")
    a = random.choice(seznam_polovic(-4, 4) + seznam_tretjin(-4, 4))
    b = random.choice(seznam_polovic(-4, 4) + seznam_tretjin(-4, 4))
    c = random.choice(seznam_polovic(-4, 4) + seznam_tretjin(-4, 4))
    splosna_oblika_kvadratne = a * x**2 + b * x + c
    return (a, b, c, splosna_oblika_kvadratne)


def izracunaj_nicle_splosne_kvadratne(a, b, c):
    """
    Iz podanih koeficientov kvadratne funkcije izračuna ničli funkcije.
    """

    diskriminanta = diskriminanta_splosne_kvadratne(a, b, c)
    if diskriminanta >= 0:
        koren_diskriminante = sympy.sqrt(diskriminanta)
    else:
        koren_diskriminante = sympy.sqrt(-diskriminanta) * sympy.I
    prva_nicla = (-b + koren_diskriminante) / (2 * a)
    druga_nicla = (-b - koren_diskriminante) / (2 * a)
    return (prva_nicla, druga_nicla)


def izracunaj_teme_iz_splosne_kvadratne(a, b, c):
    """
    Iz podanih koeficientov kvadratne funkcije koordinati temena.
    """
    x_temena = -b / (2 * a)
    y_temena = -(diskriminanta_splosne_kvadratne(a, b, c)) / (4 * a)
    return (x_temena, y_temena)


def diskriminanta_splosne_kvadratne(a, b, c):
    """
    Iz podanih koeficientov kvadratne funkcije izračuna diskriminanto.
    """
    return b**2 - 4 * a * c


# Naloga z iskanjem ničel polinoma se skriva pod razno.py, verjetno jo bomo prestavili sem
# Grafa še ne bomo


class IzracunNicelVPrimeruDvojneNicle(Problem):
    """Problem, v katerem je treba poiskati ničle danega polinoma, pri čemer je neka ničla dvojna."""

    default_instruction = r"Pokaži, da je število $@dvojna_nicla$ dvojna ničla polinoma $p(x)=@polinom$ in poišči še preostali ničli."
    default_solution = r"$x_3=@tretja_nicla$, $x_4=@cetrta_nicla$"

    class Meta:
        verbose_name = "Polinomi / iskanje ničel v primeru dvojne ničle"

    def generate(self):
        x = sympy.symbols("x")
        dvojna_nicla = random.choice(
            [-5, -4, -3, -2, -1, 2, 3, 4, 5]
        )  # Nočemo da je dvojna ničla, 0 ali 1 ker prelahko

        [a, b, c, splosna] = generiraj_splosno_obliko_kvadratne()
        [tretja_nicla, cetrta_nicla] = izracunaj_nicle_splosne_kvadratne(a, b, c)

        if not (tretja_nicla != dvojna_nicla and cetrta_nicla != dvojna_nicla):
            raise GeneratedDataIncorrect

        polinom = sympy.expand(sympy.Mul((x - dvojna_nicla) ** 2, splosna))
        return {
            "polinom": sympy.latex(polinom),
            "dvojna_nicla": sympy.latex(dvojna_nicla),
            "tretja_nicla": sympy.latex(tretja_nicla),
            "cetrta_nicla": sympy.latex(cetrta_nicla),
        }


# __MOJ DEL__#########################################################################################################################################################

# __NAVODILO__#########################################################################################################################################################


class IzracunNicelPolovAsimptotRacionalne(Problem):
    """Problem, v katerem je treba poiskati ničle, pole in asimptoto dane racionalne funkcije."""

    default_instruction = (
        r"Izračunaj ničle, pole in asimptote dane racionalne funkcije $@dvojna_nicla$."
    )
    default_solution = (
        r"$nicle=@tretja_nicla$, $poli=@cetrta_nicla$, $asimptota=@cetrta_nicla$"
    )

    class Meta:
        verbose_name = "Racionalna funkcija / iskanje ničel, polov in enačbe asimptote"

    # __GENERIRAJ__#########################################################################################################################################################
    def seznam_polovic(od=-10, do=10):
        """
        Funkcija sestavi seznam vseh celih iz polovic med vrednostima od in do (brez 0).
        [1/2, 1, 3/2, 2, 5/2, 3, 7/2]
        """
        return [sympy.Rational(x, 2) for x in range(2 * od, 2 * (do + 1)) if x != 0]

    def seznam_tretjin(od=-10, do=10):
        """
        >>> seznam_tretjin(od=0, do=3)
        [1/3, 2/3, 1, 4/3, 5/3, 2, 7/3, 8/3, 3, 10/3, 11/3]
        """
        return [sympy.Rational(x, 3) for x in range(3 * od, 3 * (do + 1)) if x != 0]

    def generate(self):
        """
        Vrne racionalno funkcijo v splošni obliki.
        """
        x = 2

        x = sympy.symbols("x")
        p3 = random.choice(seznam_polovic(-4, 4) + seznam_tretjin(-4, 4))
        p2 = random.choice(seznam_polovic(-4, 4) + seznam_tretjin(-4, 4))
        p1 = random.choice(seznam_polovic(-4, 4) + seznam_tretjin(-4, 4))
        # p0 = random.choice(seznam_polovic(-4, 4) + seznam_tretjin(-4, 4))
        q2 = random.choice(seznam_polovic(-4, 4) + seznam_tretjin(-4, 4))
        q1 = random.choice(seznam_polovic(-4, 4) + seznam_tretjin(-4, 4))
        q0 = random.choice(seznam_polovic(-4, 4) + seznam_tretjin(-4, 4))
        splosna_oblika_racionalne = (p3 * x**3 + p2 * x**2 + p1 * x**1) / (
            q2 * x**2 + q1 * x**1 + q0
        )
        return {
            "koeficienti_polinoma_v_stevcu": [p3, p2, p1, 0],
            "koeficienti_polinoma_v_imenovalcu": [q2, q1, q0],
            "splosna_oblika_racionalne_funkcije": splosna_oblika_racionalne,
        }

    # __NICLE__#########################################################################################################################################################
    def izracunaj_nicle_splosne_racionalne(p3, p2, p1):
        """
        Iz podanih koeficientov kvadratne funkcije izračuna ničli funkcije. Ena ničla pa je vedno enaka x_0 = 0.
        """

        diskriminanta = diskriminanta_splosne_kvadratne(p3, p2, p1)
        if diskriminanta >= 0:
            koren_diskriminante = sympy.sqrt(diskriminanta)
        else:
            koren_diskriminante = sympy.sqrt(-diskriminanta) * sympy.I
        prva_nicla = (-p2 + koren_diskriminante) / (2 * p3)
        druga_nicla = (-p2 - koren_diskriminante) / (2 * p3)
        tretja_nicla = 0
        return {"nicle": (prva_nicla, druga_nicla, tretja_nicla)}

    # __POLI__#########################################################################################################################################################
    def izracunaj_pole_splosne_racionalne(q2, q1, q0):
        """
        Iz podanih koeficientov kvadratne funkcije izračuna ničli funkcije. Ena ničla pa je vedno enaka x_0 = 0.
        """

        diskriminanta = diskriminanta_splosne_kvadratne(q2, q1, q0)
        if diskriminanta >= 0:
            koren_diskriminante = sympy.sqrt(diskriminanta)
        else:
            koren_diskriminante = sympy.sqrt(-diskriminanta) * sympy.I
        prvi_pol = (-q1 + koren_diskriminante) / (2 * q2)
        drugi_pol = (-q1 - koren_diskriminante) / (2 * q2)
        return {"poli": (prvi_pol, drugi_pol)}

    # __DISKIMINANTA__#########################################################################################################################################################
    def diskriminanta_splosne_kvadratne(a, b, c):
        """
        Iz podanih koeficientov kvadratne funkcije izračuna diskriminanto.
        """
        return b**2 - 4 * c * a

    # __ASIMPTOTE__#########################################################################################################################################################
    def izracunaj_enacbo_asimptote(stevec, imenovalec):
        x = sympy.symbols("x")
        asimptota, r = sympy.div(stevec, imenovalec, x)
        return {"asimptota": asimptota}


# __TERMINAL__#########################################################################################################################################################
# print(generiraj_racionalno_funkcijo())
# print(izracunaj_nicle_splosne_racionalne(1, 4, 4))
# print(izracunaj_pole_splosne_racionalne(1, 4, 4))
# print(izracunaj_enacbo_asimptote(-3, 1))

# # a bi lahko kako nardil brez tega??
# x = sympy.symbols("x")
# print(izracunaj_enacbo_asimptote(x**3 + x, x**+1))
# print(IzracunNicelPolovAsimptotRacionalne().generate())
