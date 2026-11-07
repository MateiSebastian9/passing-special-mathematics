"""Special Mathematics - theory flashcards for the partial exam.

Run:   python theory_flashcards.py
Keys:  Space = flip   Right / 2 = got it   Left / 1 = again   Backspace = previous
"""

import json
import random
import sys
from pathlib import Path
from textwrap import dedent

PROGRESS_FILE = Path(__file__).with_name("flashcards_progress.json")


# --------------------------------------------------------------------------- #
# Cards: (topic, question, answer)
# --------------------------------------------------------------------------- #
CARDS = []


def card(topic, question, answer, top=False):
    """top=True marks the cards most likely to be asked on the partial."""
    CARDS.append({
        "topic": topic,
        "q": dedent(question).strip(),
        "a": dedent(answer).strip(),
        "top": top,
    })


T1 = "1. Linear SDEs - basics"
T2 = "2. Homogeneous SDEs & Wronskian"
T3 = "3. Constant coefficients"
T4 = "4. Fundamental matrix"
T5 = "5. Stability - definitions & theorem"
T6 = "6. Routh-Hurwitz"
T7 = "7. Lyapunov equation"
T8 = "8. Seminar methods (for problems)"

# ---- 1. Basics ------------------------------------------------------------- #
card(T1, "What is the form of a linear SDE?", """
    y1'(x) = a11(x)y1(x) + a12(x)y2(x) + ... + a1n(x)yn(x) + b1(x)
    y2'(x) = a21(x)y1(x) + ... + a2n(x)yn(x) + b2(x)        (1)
    ...
    yn'(x) = an1(x)y1(x) + ... + ann(x)yn(x) + bn(x)

    aij, bi : I -> R are continuous functions on an interval I ⊂ R.
    (Under these conditions one can show the solution exists.)
""")
card(T1, "Matrix form of a linear SDE. Homogeneous vs nonhomogeneous?", """
    With A(x) = (aij(x)) n×n,  Y(x) = (y1(x),...,yn(x))ᵀ,  b(x) = (b1(x),...,bn(x))ᵀ
    the system (1) is equivalent to the vector equality:

        Y'(x) = A(x)·Y(x) + b(x)      (1)  nonhomogeneous SDE

    b1,...,bn are called PERTURBING FUNCTIONS.
    If b1 = b2 = ... = bn ≡ 0 the system is HOMOGENEOUS:

        Y'(x) = A(x)·Y(x)             (1')
""")
card(T1, "What is a solution? What is the general solution?", """
    A SOLUTION is a vector function Y(x) = (y1(x),...,yn(x))ᵀ which satisfies
    the SDE (1) or (1').

    The GENERAL SOLUTION is a vector function Y(x, C1, C2, ..., Cn), where
    C1,...,Cn ∈ R are arbitrary constants, such that ANY solution can be
    obtained from it by a suitable choice of the arbitrary constants.

    (The variable x represents the time.)
""")
card(T1, "Define an initial value problem (IVP).", """
    IVP:  { Y'(x) = A(x)Y(x) + b(x)     (1)  SDE
          { Y(x0) = Y0                  (IC) initial condition

    x0 ∈ R is the INITIAL MOMENT, Y0 ∈ Rⁿ is the INITIAL POSITION.
""")

# ---- 2. Homogeneous & Wronskian -------------------------------------------- #
card(T2, "Proposition 1 (homogeneous SDE): statement + proof.", """
    STATEMENT: Any linear combination of solutions of (1') Y' = A(x)Y
    is a solution of (1').

    PROOF: Let Y1(x), Y2(x) be two solutions:
        Y1' = A(x)Y1,  Y2' = A(x)Y2      (2)
    Let c1, c2 ∈ R and Y(x) = c1Y1(x) + c2Y2(x).
    Introduce Y in (1'):
        Y'(x) = c1Y1'(x) + c2Y2'(x) =(2)= c1A(x)Y1(x) + c2A(x)Y2(x)
    Take A(x) as a LEFT common factor:
        = A(x)(c1Y1(x) + c2Y2(x)) = A(x)Y(x)
    => Y' = A(x)Y, so the linear combination Y is a solution of (1'). ∎
""", top=True)
card(T2, "Corollary of Proposition 1?", """
    The set of solutions of a homogeneous SDE is a LINEAR SPACE.
""", top=True)
card(T2, "Define the Wronskian.", """
    Consider n solutions of the SDE:
        Y1 = (y11, y12, ..., y1n)ᵀ, ..., Yn = (yn1, ..., ynn)ᵀ
    The determinant formed with the columns Y1, Y2, ..., Yn is called the
    WRONSKIAN of the solutions:
        W(x) = det(Y1(x)  Y2(x)  ...  Yn(x))
""", top=True)
card(T2, "Proposition 2 (Wronskian): statement + proof.", """
    STATEMENT: If the solutions Y1,...,Yn are linearly DEPENDENT on an
    interval I ⊂ R, then W(x) = 0, ∀x ∈ I.

    PROOF (chain of equivalent statements):
    Y1,...,Yn linearly dependent on I
    => ∃ c1,...,cn NOT ALL equal to 0 such that
           c1Y1(x) + c2Y2(x) + ... + cnYn(x) = 0,  ∀x ∈ I
    => written on components:
           c1y11 + c2y21 + ... + cnyn1 = 0
           ...
           c1y1n + c2y2n + ... + cnynn = 0
    Consider these as an ALGEBRAIC linear system with unknowns (c1,...,cn).
    It is linear and homogeneous and has a NONZERO solution (c1,...,cn)
    => its determinant = 0
    => W(x) = 0. ∎
""", top=True)
card(T2, "Proposition 3 (Wronskian): statement + consequence.", """
    STATEMENT: The solutions Y1,...,Yn of the homogeneous SDE (1') are
    linearly INDEPENDENT on I  <=>  W(x) ≠ 0.
    (Proved by negation from Proposition 2.)

    CONSEQUENCE: If W(x) ≠ 0, the solutions Y1,...,Yn form a BASIS in the
    linear space of solutions <=> any solution is a linear combination of
    the basis:
        Y(x) = c1Y1(x) + c2Y2(x) + ... + cnYn(x)     (3)
    So if W(x) ≠ 0, then (3) is the GENERAL SOLUTION.
""", top=True)

# ---- 3. Constant coefficients ---------------------------------------------- #
card(T3, "What does 'constant coefficients' mean?", """
    All coefficients aij(x) = aij ∈ R are constants
    => A = (aij) is a constant n×n matrix, and the SDE is Y'(x) = A·Y(x).
""")
card(T3, "Case I: A diagonalizable. What are the solutions?", """
    A is diagonalizable <=> A has n linearly independent eigenvectors
    v1,...,vn corresponding to the eigenvalues λ1,...,λn:
        Av1 = λ1v1, ..., Avn = λnvn        (2)
    Linearly independent => det(v1 v2 ... vn) ≠ 0.

    Then the vector functions
        Y1 = v1·e^(λ1·x), ..., Yn = vn·e^(λn·x)
    are linearly independent solutions, and the general solution is
        Y(x) = C1·v1·e^(λ1·x) + C2·v2·e^(λ2·x) + ... + Cn·vn·e^(λn·x)
""")
card(T3, "Algorithm (course) for Y' = AY, A diagonalizable.", """
    Step I:   Solve the characteristic equation det(A - λIn) = 0;
              find the spectrum σ(A) = {λ1, λ2, ...}.
    Step II:  For each eigenvalue λi solve the algebraic linear homogeneous
              system (A - λiIn)v = 0 and find an eigenvector vi.
    Step III: Write the general solution
              Y(x) = C1v1e^(λ1x) + C2v2e^(λ2x) + ... + Cnvne^(λnx)
""")
card(T3, "Define algebraic multiplicity ma(λ) and geometric multiplicity mg(λ).", """
    ma(λ) = the multiplicity of λ as a ROOT of the characteristic equation
            det(A - λI) = 0.
    mg(λ) = the number of linearly independent EIGENVECTORS corresponding
            to λ (= dimension of the eigenspace, from (A - λI)v = 0).

    Always:  ma(λ) ≥ mg(λ).

    Example: A = [[-1,0,2],[0,-1,3],[0,0,5]],
             det(λI - A) = (λ+1)²(λ-5) => ma(-1) = 2, ma(5) = 1.
""")
card(T3, "Case II: A NOT diagonalizable. What do we do?", """
    ∃ λ ∈ σ(A) with ma(λ) > mg(λ)
    => not enough linearly independent eigenvectors
    => introduce CHAINS of GENERALISED eigenvectors (principal vectors):

        Av1 = λv1,  v1 ≠ 0   (v1 is an eigenvector)
        Av2 = λv2 + v1
        Av3 = λv3 + v2
        ...
        Avm = λvm + v(m-1)
""")
card(T3, "Case II: write the solutions given by a chain v1, v2, ..., vm.", """
    Y1 = v1·e^(λx)                                   -> degree 0 polynomial
    Y2 = [ (x/1!)·v1 + v2 ]·e^(λx)                    -> degree 1 polynomial
    Y3 = [ (x²/2!)·v1 + (x/1!)·v2 + v3 ]·e^(λx)        -> degree 2 polynomial
    ...
    Ym = [ x^(m-1)/(m-1)!·v1 + x^(m-2)/(m-2)!·v2 + ... + vm ]·e^(λx)

    These solutions are linearly independent.
""")
card(T3, "Prove that Yk = [x^(k-1)/(k-1)!·v1 + ... + vk]e^(λx) is a solution of Y' = AY.", """
    Calculate both members.

    LEFT:
    Yk' = [x^(k-2)/(k-2)!·v1 + ... + v(k-1)]e^(λx)
          + λ[x^(k-1)/(k-1)!·v1 + ... + vk]e^(λx)

    RIGHT:
    AYk = [x^(k-1)/(k-1)!·Av1 + ... + Avk]e^(λx)
    Replace Av1 = λv1 and Avj = λvj + v(j-1):
    AYk = λ[x^(k-1)/(k-1)!·v1 + ... + vk]e^(λx)
          + [x^(k-2)/(k-2)!·v1 + ... + v(k-1)]e^(λx)

    The two members are equal => Yk' = AYk. ∎
""")
card(T3, "Seminar algorithm for Y' = AY (all cases).", """
    1. Eigenvalues: det(A - λIn) = 0 -> σ(A), and ma(λ) for each.
    2. For each λ: eigenspace from (A - λIn)v = 0; mg(λ) = its dimension.
    3. For each λ:
       a. ma = mg = 1   -> take eigenvector v, solution e^(λx)·v
       b. ma = mg = k≥2 -> take k linearly independent eigenvectors,
                           solutions e^(λx)·v1, ..., e^(λx)·vk
       c. ma > mg = 1   -> eigenvector v + principal vectors:
                           (A - λIn)vp1 = v,  (A - λIn)vp2 = vp1, ...
                           v   -> e^(λx)·v
                           vp1 -> e^(λx)·(x/1!·v + vp1)
                           vp2 -> e^(λx)·(x²/2!·v + x/1!·vp1 + vp2)
    4. General solution Y = C1·(1st solution) + ... + Cn·(nth solution).
""")

# ---- 4. Fundamental matrix ------------------------------------------------- #
card(T4, "Define the fundamental matrix Φ(x, x0).", """
    Consider the IVP with a time-variable matrix A(x):
        Y'(x) = A(x)Y(x)  (1'),   Y(x0) = Y0  (IC)
    Determine the solutions Y1(x), ..., Yn(x) of the n IVPs
        Yk'(x) = A(x)Yk(x),   Yk(x0) = ek     (k = 1..n)
    where e1 = (1,0,...,0)ᵀ, ..., en = (0,...,0,1)ᵀ.

    The matrix formed with the columns Y1(x), ..., Yn(x) is called the
    FUNDAMENTAL MATRIX of the SDE (1') (of the matrix A(x)):
        Φ(x, x0) = ( Y1(x)  Y2(x)  ...  Yn(x) )

    Remark: the solutions depend on the initial moment x0.
""", top=True)
card(T4, "List the properties of the fundamental matrix.", """
    1. d/dx Φ(x, x0) = A(x)·Φ(x, x0)
    2. Φ(x0, x0) = In
    3. The solution of the IVP (1')+(IC) is Y(x) = Φ(x, x0)·Y0
    4. Φ(x, x1)·Φ(x1, x0) = Φ(x, x0)        (the subgroup property)
    5. Φ(x, x0)⁻¹ = Φ(x0, x)
    6. Peano-Baker formula
    7. A constant => Φ(x, x0) = e^(A(x - x0))
""", top=True)
card(T4, "Fundamental matrix - prove property 1: Φ' = A(x)Φ.", """
    One derives a matrix by deriving all its elements, hence by deriving
    all its columns:
    d/dx Φ(x, x0) = ( Y1'(x)  Y2'(x)  ...  Yn'(x) )
                  = ( A(x)Y1(x)  A(x)Y2(x)  ...  A(x)Yn(x) )
                  = A(x)·( Y1(x)  Y2(x)  ...  Yn(x) )
                  = A(x)·Φ(x, x0). ∎
""", top=True)
card(T4, "Fundamental matrix - prove property 2: Φ(x0, x0) = In.", """
    Replace x by x0:
    Φ(x0, x0) = ( Y1(x0)  Y2(x0)  ...  Yn(x0) ) = ( e1  e2  ...  en ) = In. ∎
""", top=True)
card(T4, "Fundamental matrix - prove property 3: Y(x) = Φ(x, x0)Y0 solves the IVP.", """
    Show that Ỹ(x) = Φ(x, x0)·Y0 verifies (1') and (IC).

    (1'): Ỹ'(x) = d/dx(Φ(x, x0)Y0) =(P1)= A(x)Φ(x, x0)Y0 = A(x)Ỹ(x)
    (IC): for x = x0,  Ỹ(x0) = Φ(x0, x0)Y0 =(P2)= In·Y0 = Y0

    The IVP has a unique solution => Ỹ is the solution of the IVP. ∎
""", top=True)
card(T4, "Fundamental matrix - the Remark (uniqueness of Φ).", """
    If an n×n matrix M(x, x0) has the properties 1 and 2, i.e.
        d/dx M(x, x0) = A(x)·M(x, x0)   and   M(x0, x0) = In,
    then Φ(x, x0) = M(x, x0)
    (similarly, Y(x) = M(x, x0)·Y0 solves the IVP).
""", top=True)
card(T4, "Fundamental matrix - prove property 4 (subgroup property).", """
    Apply property 3 on the intervals [x0, x1], [x1, x], [x0, x]:
        on [x0, x1]:  Y(x1) = Φ(x1, x0)·Y0
        on [x1, x]:   Y(x)  = Φ(x, x1)·Y(x1)   -> replace Y(x1):
                      Y(x)  = Φ(x, x1)·Φ(x1, x0)·Y0
        on [x0, x]:   Y(x)  = Φ(x, x0)·Y0
    We obtained two expressions for the solution of the IVP.
    But the IVP has a UNIQUE solution =>
        Φ(x, x1)Φ(x1, x0)Y0 = Φ(x, x0)Y0  for every Y0
    => the matrices are equal: Φ(x, x1)·Φ(x1, x0) = Φ(x, x0). ∎
""", top=True)
card(T4, "Fundamental matrix - prove property 5: Φ(x, x0)⁻¹ = Φ(x0, x).", """
    For two n×n matrices: B is the inverse of A (A⁻¹ = B) <=> B·A = In.
    Take A = Φ(x, x0) and B = Φ(x0, x). Then
        B·A = Φ(x0, x)·Φ(x, x0) =(P4)= Φ(x0, x0) =(P2)= In
    => A⁻¹ = B, i.e. Φ(x, x0)⁻¹ = Φ(x0, x). ∎
""", top=True)
card(T4, "State the Peano-Baker formula.", """
    Φ(x, x0) = In + ∫[x0,x] A(s1) ds1
                  + ∫[x0,x] A(s1) ∫[x0,s1] A(s2) ds2 ds1
                  + ...
                  + ∫[x0,x] A(s1) ∫[x0,s1] A(s2) ... ∫[x0,s(k-1)] A(sk) dsk ... ds1
                  + ...
""", top=True)
card(T4, "Prove the Peano-Baker formula.", """
    Denote by M(x, x0) the sum of the series. Prove that M has properties
    1 and 2; then by the Remark Φ(x, x0) = M(x, x0).

    Idea: derive the series term by term:
    d/dx M(x, x0) = 0n + A(x) + A(x)∫[x0,x]A(s2)ds2 + ...
                  = A(x)·[ In + ∫[x0,x]A(s2)ds2 + ... ]
                  = A(x)·M(x, x0)                        (property 1)
    Replace x by x0: every integral is 0 => M(x0, x0) = In (property 2)

    By the Remark, Φ(x, x0) = M(x, x0), hence (PB) is true. ∎
""", top=True)
card(T4, "A constant: show that Φ(x, x0) = e^(A(x - x0)).", """
    For A constant the (PB) formula becomes
    Φ(x, x0) = In + A∫[x0,x]ds1 + A²∫[x0,x](∫[x0,s1]ds2)ds1 + ...
                  + Aᵏ ∫[x0,x]∫[x0,s1]...∫[x0,s(k-1)] dsk...ds1 + ...

    Calculate the integrals (induction):
      ∫[x0,x] ds1 = x - x0 = (x - x0)/1!
      ∫[x0,x] (s1 - x0)/1! ds1 = (x - x0)²/2!
      Assume k-1 integrals = (difference of limits)^(k-1)/(k-1)!; then
      ∫[x0,x] (s1 - x0)^(k-1)/(k-1)! ds1 = (x - x0)ᵏ/(k·(k-1)!) = (x - x0)ᵏ/k!

    So Φ(x, x0) = In + A(x-x0)/1! + (A(x-x0))²/2! + ... + (A(x-x0))ᵏ/k! + ...
               = e^(A(x - x0))   (the exponential matrix)
    and property 3 becomes (for x0 = 0):  Y(x) = e^(Ax)·Y0.
""", top=True)
card(T4, "State the variation of parameters formula (VPF). Is the proof required?", """
    The solution of the IVP
        Y'(x) = A(x)Y(x) + b(x)  (1) nonhomogeneous,   Y(x0) = Y0  (IC)
    is given by the VARIATION OF PARAMETERS FORMULA:

        Y(x) = Φ(x, x0)·Y0 + ∫[x0,x] Φ(x, s)·b(s) ds        (VPF)

    For A constant, Φ(x, x0) = e^(A(x - x0)) and (VPF) becomes:
        Y(x) = e^(A(x - x0))·Y0 + ∫[x0,x] e^(A(x - s))·b(s) ds

    NOTE: WITHOUT PROOF at the exam (statement only).
""", top=True)

# ---- 5. Stability ---------------------------------------------------------- #
card(T5, "Stability setting: what is the equilibrium position?", """
    IVP: Y'(x) = A·Y(x) (1'),  Y(0) = Y0 (IC),  A a constant real n×n matrix.
    The solution is Y(x) = e^(Ax)·Y0.

    Remark: if the initial position is Y0 = 0n, then Y(x) = e^(Ax)·0 = 0
    => Y0 = 0 is an EQUILIBRIUM POSITION.

    Norm used: for Y = (y1,...,yn)ᵀ,  ||Y|| = sqrt(y1² + y2² + ... + yn²).
    (For n = 1: ||y|| = |y|, so ||y|| < ε <=> -ε < y < ε.)
""", top=True)
card(T5, "Define: stable system.", """
    The system (1') is STABLE if
        ∀ ε > 0, ∃ δ > 0 such that ∀ Y0 ∈ Rⁿ with ||Y0|| < δ,
        the solution Y(x) = e^(Ax)·Y0 verifies ||Y(x)|| < ε.

    (Graph: the solution stays inside the band between -ε and ε.)
""", top=True)
card(T5, "Define: unstable and asymptotically stable system.", """
    UNSTABLE: the system (1') is unstable if it is NOT stable.
    (Graph: the solution leaves the band and grows.)

    ASYMPTOTICALLY STABLE: the system (1') is asymptotically stable if
        - it is stable, and
        - lim (x->∞) Y(x) = 0.
    (Graph: oscillations that shrink to 0.)
""", top=True)
card(T5, "Proposition: what functions appear in e^(Ax) depending on ma and mg?", """
    Let λ ∈ σ(A) (an eigenvalue; σ(A) = spectrum of A).

    1. If ma(λ) = mg(λ), then for λ the solution Y(x) = e^(Ax)Y0 and e^(Ax)
       can contain ONLY simple functions of the form e^(λx)
       (A is diagonalizable on λ).

    2. If ma(λ) > mg(λ), there are not enough eigenvectors => we need chains
       of principal vectors (A is not diagonalizable) => Y(x) and e^(Ax) can
       contain functions of the form x^k·e^(λx).
""", top=True)
card(T5, "Stability theorem: the 4 cases.", """
    1. Y' = AY is ASYMPTOTICALLY STABLE  <=>  ∀ λ ∈ σ(A), Re(λ) < 0
       (all eigenvalues have negative real parts).

    2. If ∃ λ ∈ σ(A) with Re(λ) > 0  =>  UNSTABLE.

    3. If ∀ λ ∈ σ(A) Re(λ) ≤ 0, and for every λ with Re(λ) = 0 we have
       ma(λ) = mg(λ)  =>  STABLE, but NOT asymptotically stable.

    4. If ∃ λ ∈ σ(A) with Re(λ) = 0 and ma(λ) > mg(λ)  =>  UNSTABLE.
""", top=True)
card(T5, "Stability proof - the two preliminary facts (A and B).", """
    A. For z ∈ C, |e^z| = e^(Re z).
       z = x + iy  =>  e^z = e^(x+iy) = e^x·e^(iy) = e^x(cos y + i sin y),
       and |cos y + i sin y| = 1  =>  |e^z| = e^x = e^(Re z).
       Hence |x^k·e^(λx)| = x^k·e^(Re(λ)·x).

    B. If a > 0:  lim (x->∞) x^k·e^(ax) = ∞.
       If a < 0, a = -b (b > 0):  lim x^k·e^(-bx) = lim x^k / e^(bx) = 0
       (apply L'Hospital k times).
""", top=True)
card(T5, "Stability proof - case I (asymptotically stable <=> all Re λ < 0).", """
    Equivalent statements:
    The system is asymptotically stable
    <=> it is stable and lim (x->∞) Y(x) = 0
    <=> all the functions contained in the solution Y(x) = e^(Ax)Y0 tend to 0
    <=> ∀ function x^k·e^(λx) -> 0
    <=> (by A and B) Re(λ) < 0, ∀ λ ∈ σ(A). ∎
""", top=True)
card(T5, "Stability proof - case II (some Re λ > 0 => unstable).", """
    If ∃ λ ∈ σ(A) with Re(λ) > 0, then by A and B:
        lim (x->∞) |x^k·e^(λx)| = lim x^k·e^(Re(λ)x) = ∞
    => the solution is unbounded => the system is UNSTABLE. ∎
""", top=True)
card(T5, "Stability proof - case III (stable but not asymptotically stable).", """
    Re(λ) ≤ 0 ∀λ, and for λ with Re(λ) = 0: ma(λ) = mg(λ).

    - For λ with Re(λ) < 0:  lim x^k·e^(λx) = 0.
    - For λ with Re(λ) = 0: only simple functions e^(λx) appear (ma = mg),
      and |e^(λx)| = e^(Re(λ)x) = e^0 = 1  -> bounded, but NOT -> 0.

    Conclusion: all the functions in Y(x) = e^(Ax)Y0 are bounded, and the
    same holds in the matrix e^(Ax) => e^(Ax) is bounded:
        ∃ M > 0 (majorant) such that ||e^(Ax)|| ≤ M.

    For an arbitrary ε > 0 take δ = ε/M. Then for any Y0 with ||Y0|| < δ:
        ||Y(x)|| = ||e^(Ax)Y0|| ≤ M·||Y0|| < M·ε/M = ε
    => the system is STABLE.
    But |e^(λx)| = 1 does not tend to 0 => NOT asymptotically stable. ∎
""", top=True)
card(T5, "Stability proof - case IV (Re λ = 0 with ma > mg => unstable).", """
    If ∃ λ ∈ σ(A) with Re(λ) = 0 and ma(λ) > mg(λ), then the solution Y(x)
    can contain functions of the form x^k·e^(λx), k ≥ 1. Then
        |x^k·e^(λx)| = x^k·e^(Re(λ)x) = x^k·e^0 = x^k -> ∞
    => the solution is unbounded => UNSTABLE. ∎
""", top=True)

# ---- 6. Routh-Hurwitz ------------------------------------------------------ #
card(T6, "Routh-Hurwitz: characteristic polynomial and notations ℂ⁻, ℂ⁺, ℂ⁰, N⁻, N⁺, N⁰.", """
    Characteristic polynomial of A:
        P(s) = det(sI - A) = an·sⁿ + a(n-1)·s^(n-1) + ... + a1·s + a0,  an > 0
    Its roots are the eigenvalues: σ(A) = {λ1, ..., λn}.

    ℂ⁻ = {z ∈ ℂ | Re z = x < 0}  (left half-plane)
    ℂ⁺ = {z ∈ ℂ | Re z = x > 0}
    ℂ⁰ = {z ∈ ℂ | Re z = 0}
    N⁻ = number of eigenvalues of A with Re λ < 0
    N⁺ = number of eigenvalues of A with Re λ > 0
    N⁰ = number of eigenvalues of A with Re λ = 0

    By the Theorem: asymptotically stable <=> all eigenvalues ∈ ℂ⁻
                                          <=> N⁺ = 0 and N⁰ = 0.
""")
card(T6, "Write the Hurwitz matrix and its principal minors (course notation).", """
    For P(s) = an·sⁿ + a(n-1)·s^(n-1) + ... + a0:

          | a(n-1)  an      0       0       0  ...  0  |
    Hn =  | a(n-3)  a(n-2)  a(n-1)  an      0  ...  0  |
          | a(n-5)  a(n-4)  a(n-3)  a(n-2)  a(n-1) an ...|
          |  ...                                       |
          |  0      0       0       0       0  ...  a0 |

    Principal minors:
        Δ1 = a(n-1)
        Δ2 = | a(n-1)  an     |
             | a(n-3)  a(n-2) |
        ...
        Δn = det(Hn)
""")
card(T6, "Hurwitz matrix in SEMINAR notation (the one used in problems).", """
    P_A(λ) = det(λIn - A) = a0·λⁿ + a1·λ^(n-1) + ... + an
    (a0 = coefficient of the HIGHEST power!)

    1. Check aj > 0, j = 0..n  (necessary condition).
    2.        | a1    a0    0   ...  0  |
        Hn =  | a3    a2    a1  a0 ... 0 |      entry (i, j) = a(2i - j),
              | ...                      |      ak = 0 if k < 0 or k > n
              | a(2n-1) a(2n-2) ...   an |
    3. If Hn is positive definite (Sylvester: all leading minors > 0)
       => the system is asymptotically stable.

    n = 2:  H2 = [[a1, a0], [0, a2]]
    n = 3:  H3 = [[a1, a0, 0], [a3, a2, a1], [0, 0, a3]]
            Δ1 = a1, Δ2 = a1a2 - a0a3, Δ3 = a3·Δ2
""")
card(T6, "State the Routh-Hurwitz criterion.", """
    The SDE Y' = AY is asymptotically stable
        <=>  Δ1 > 0, Δ2 > 0, ..., Δn > 0      (2)
    (all principal minors of the Hurwitz matrix are positive).
""", top=True)
card(T6, "Routh-Hurwitz proof: the two propositions used (Gantmacher, Matrix Theory).", """
    Proposition 1: If Δi ≠ 0, ∀ i = 1..n, then N⁰ = 0.

    Proposition 2: N⁺ (the number of eigenvalues with Re λ > 0) is equal to
    the number of changes of sign (Ncs) in the sequence
        1,  Δ1,  Δ2/Δ1,  Δ3/Δ2,  ...,  Δn/Δ(n-1)        (3)
""")
card(T6, "Routh-Hurwitz proof: sufficiency and necessity.", """
    SUFFICIENCY: If (2) holds then Δ1 ≠ 0, ..., Δn ≠ 0 => (Prop. 1) N⁰ = 0.
    Δ1 > 0, ..., Δn > 0 => all ratios Δi/Δ(i-1) > 0 => no change of sign in (3)
    => (Prop. 2) N⁺ = Ncs = 0.
    N⁰ = 0 and N⁺ = 0 => all eigenvalues have negative real parts
    => asymptotically stable.

    NECESSITY: Assume asymptotically stable => N⁰ = 0, N⁺ = 0
    => Ncs = N⁺ = 0 => no change of sign in (3). Since 1 > 0:
    1 > 0 => Δ1 > 0;  Δ2/Δ1 > 0 and Δ1 > 0 => Δ2 > 0;  ...;
    Δn/Δ(n-1) > 0 and Δ(n-1) > 0 => Δn > 0. ∎
""")

# ---- 7. Lyapunov ----------------------------------------------------------- #
card(T7, "Define a positive definite matrix (complex case).", """
    Let P be an n×n matrix with complex entries. P is POSITIVE DEFINITE if
        1. P* = P        (P* = conjugate transpose, P* = P̄ᵀ)
        2. v*·P·v > 0,  ∀ v ∈ ℂⁿ, v ≠ 0
""")
card(T7, "Prove: a complex number z is real <=> z = z̄.", """
    =>: z real => z = x ∈ R => z = x + i·0 => z̄ = x - i·0 = x => z = z̄.
    <=: z = x + iy with z = z̄ => x + iy = x - iy => y = 0 => z = x ∈ R. ∎

    Consequence: if P is a real matrix, P̄ = P => P* = P̄ᵀ = Pᵀ.
""")
card(T7, "When is a REAL matrix P positive definite? How do you check it in practice?", """
    A real matrix P is positive definite <=>
        1. Pᵀ = P  (symmetric)
        2. vᵀ·P·v > 0, ∀ v ∈ Rⁿ, v ≠ 0

    In practice - SYLVESTER criterion: all leading principal minors > 0.
        P = [[a, b], [b, c]]:  Δ1 = a > 0,  Δ2 = ac - b² > 0
""")
card(T7, "State the Lyapunov theorem.", """
    The SDE Y' = AY (1') is asymptotically stable  <=>  the Lyapunov equation

        Aᵀ·P + P·A = -Q        (L)

    has a positive definite real matrix solution P, for a positive definite
    real matrix Q.

    (Seminar form: if for a symmetric positive definite Q we can find P,
    also symmetric and positive definite, with AᵀP + PA = -Q, then the system
    is asymptotically stable. Q is always given in problems.)
""", top=True)
card(T7, "Lyapunov theorem - prove sufficiency.", """
    Assume (L) has a solution P > 0 for Q > 0. We prove Re λ < 0, ∀ λ ∈ σ(A).

    Let λ ∈ ℂ be an eigenvalue of A and v ∈ ℂⁿ a corresponding eigenvector:
        Av = λv,  v ≠ 0   =>   v*Aᵀ = λ̄·v*   (A real)

    Idea: premultiply (L) by v* and postmultiply by v:
        v*AᵀPv + v*PAv = -v*Qv
        λ̄·v*Pv + λ·v*Pv = -v*Qv
        (λ + λ̄)·v*Pv = -v*Qv
        2·Re(λ)·v*Pv = -v*Qv

    v*Pv > 0 (P > 0) and v*Qv > 0 (Q > 0)  =>  Re(λ) < 0,
    for every eigenvalue λ of A => asymptotically stable. ∎
""", top=True)
card(T7, "Lyapunov theorem - necessity (idea).", """
    Assume the SDE is asymptotically stable => ∀ λ ∈ σ(A), Re λ < 0.
    Let Q > 0. The solution of (L) is

        P = ∫[0,∞) e^(Aᵀx)·Q·e^(Ax) dx

    Since Re λ < 0, the entries of P are (in modulus) of the form
    ∫[0,∞) x^k·e^(-ax) dx (Gamma-type integrals) => convergent integrals
    => P is well defined (and positive definite).
""")

# ---- 8. Seminar methods ---------------------------------------------------- #
card(T8, "Stability exercises: Method 1 (eigenvalues).", """
    1. Find the eigenvalues of A: det(A - λIn) = 0.
       (2×2 shortcut: λ² - tr(A)·λ + det(A) = 0)
    2. If Re(λ) < 0 for ALL eigenvalues => asymptotically stable.

    Complex roots: Δ < 0 => λ = -b/2a ± i·sqrt(-Δ)/2a, Re(λ) = -b/2a.
""")
card(T8, "Stability exercises: Method 3 (Lyapunov) - practical steps.", """
    1. P = [[a, b], [b, c]]  (3×3: [[a, d, e], [d, b, f], [e, f, c]])
    2. Compute P·A. Since P is symmetric, AᵀP = (PA)ᵀ, so
       AᵀP + PA = PA + (PA)ᵀ:
         diagonal entries   = 2 × diagonal of PA
         off-diagonal (i,j) = (PA)ij + (PA)ji
    3. Set it equal to -Q, solve for a, b, c.
       (2×2 trick: the corner equations give a and c in terms of b;
        plug into the middle equation.)
    4. Sylvester on P: Δ1 > 0, Δ2 > 0 (, Δ3 > 0) => asymptotically stable.
""")
card(T8, "Nonhomogeneous system Y' = AY + b(x), Y(0) = Y0: algorithm.", """
    1. Eigenvalues of A: det(A - λIn) = 0.
    2. Find e^(Ax):
       Case I (λ1 ≠ λ2): eigenvectors v1, v2; C = (v1 v2); C⁻¹;
           e^(Dx) = [[e^(λ1x), 0], [0, e^(λ2x)]],  e^(Ax) = C·e^(Dx)·C⁻¹
       Case II (λ, ma = 2): eigenvector v, principal vector vp1
           ((A - λI)vp1 = v); C = (v vp1); C⁻¹;
           e^(Jx) = e^(λx)·[[1, x], [0, 1]],  e^(Ax) = C·e^(Jx)·C⁻¹
           (careful: some notes write [[x,1],[0,1]] - that is WRONG,
            it does not give e^(A·0) = I)
           Shortcut for 2×2, ma = 2:  e^(Ax) = e^(λx)·[ I + x(A - λI) ]
    3. Yh = e^(Ax)·Y0
    4. Yp = ∫[0,x] e^(A(x-t))·b(t) dt
    5. Y = Yh + Yp
    Check: e^(A·0) must be I.
""")
card(T8, "Derivability of f at z0 = x0 + iy0: Cauchy-Riemann algorithm.", """
    1. Replace z = x + iy; find Re f = u(x, y) and Im f = v(x, y).
    2. Compute ∂u/∂x, ∂u/∂y, ∂v/∂x, ∂v/∂y.
    3. Check the Cauchy-Riemann conditions at (x0, y0):
         a. ∂u/∂x (x0,y0) =  ∂v/∂y (x0,y0)
         b. ∂u/∂y (x0,y0) = -∂v/∂x (x0,y0)
       Both true => f is derivable at z0, f'(z0) = ∂u/∂x + i·∂v/∂x.
       Otherwise f is not derivable at z0.
""")
card(T8, "Restoration of an analytic function from Re f = u or Im f = v.", """
    0. Check harmonic: Δu = ∂²u/∂x² + ∂²u/∂y² = 0 (or Δv = 0).
       If ≠ 0, stop: no analytic function exists.
    1. Known u:  f'(z) = ∂u/∂x - i·∂u/∂y
       Known v:  f'(z) = ∂v/∂y + i·∂v/∂x
    2. Put y = 0:  f'(x) = A(x)
    3. f(x) = ∫A(x)dx + C
    4. Replace x by z:  f(z) = ... + C
    5. Use the given condition (e.g. f(i) = i) to find C.
""")
card(T8, "Elementary complex functions (seminar list).", """
    e^z = e^(a+bi) = e^a(cos b + i sin b)
    sin z = (e^(iz) - e^(-iz)) / (2i)      cos z = (e^(iz) + e^(-iz)) / 2
    sh z  = (e^z - e^(-z)) / 2             ch z  = (e^z + e^(-z)) / 2
    Ln z  = ln|z| + i(θ + 2kπ),  z ≠ 0     (θ = argument of z)
    ⁿ√z   = ⁿ√|z| · ( cos((θ+2kπ)/n) + i sin((θ+2kπ)/n) ),  k = 0..n-1
    z^α   = e^(α·Ln z),  z ≠ 0
""")


# --------------------------------------------------------------------------- #
# Deck logic (no GUI dependency, so it can be tested on its own)
# --------------------------------------------------------------------------- #
ALL_TOPICS = "All topics"
TOP_ONLY = "★ Most likely (top)"


def topics():
    seen = []
    for c in CARDS:
        if c["topic"] not in seen:
            seen.append(c["topic"])
    return seen


def load_progress():
    try:
        data = json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))
        return set(data.get("known", [])), set(data.get("missed", []))
    except (OSError, ValueError):
        return set(), set()


def save_progress(known, missed):
    try:
        PROGRESS_FILE.write_text(
            json.dumps({"known": sorted(known), "missed": sorted(missed)}, indent=1),
            encoding="utf-8",
        )
    except OSError:
        pass


class Deck:
    def __init__(self):
        self.known, self.missed = load_progress()
        self.cards = []
        self.pos = 0

    def build(self, topic=ALL_TOPICS, hide_known=False, only_missed=False, shuffle=False):
        cards = list(CARDS)
        if topic == TOP_ONLY:
            cards = [c for c in cards if c["top"]]
        elif topic != ALL_TOPICS:
            cards = [c for c in cards if c["topic"] == topic]
        if only_missed:
            cards = [c for c in cards if c["q"] in self.missed]
        if hide_known:
            cards = [c for c in cards if c["q"] not in self.known]
        if shuffle:
            random.shuffle(cards)
        self.cards = cards
        self.pos = 0

    @property
    def current(self):
        return self.cards[self.pos] if self.pos < len(self.cards) else None

    def got_it(self):
        c = self.current
        if c is None:
            return
        self.known.add(c["q"])
        self.missed.discard(c["q"])
        save_progress(self.known, self.missed)
        self.pos += 1

    def again(self):
        """Mark as missed and requeue the card a few places later."""
        c = self.current
        if c is None:
            return
        self.missed.add(c["q"])
        self.known.discard(c["q"])
        save_progress(self.known, self.missed)
        self.cards.pop(self.pos)
        self.cards.insert(min(self.pos + 4, len(self.cards)), c)

    def back(self):
        if self.pos > 0:
            self.pos -= 1

    def reset(self):
        self.known.clear()
        self.missed.clear()
        save_progress(self.known, self.missed)


# --------------------------------------------------------------------------- #
# GUI
# --------------------------------------------------------------------------- #
def run_gui():
    import tkinter as tk
    from tkinter import ttk, messagebox

    BG, CARD_BG, ACCENT = "#f4f1ea", "#ffffff", "#2f5d8a"
    GOOD, BAD, MUTED = "#2e7d4f", "#b3412f", "#6b6b6b"

    deck = Deck()
    root = tk.Tk()
    root.title("Special Mathematics - Theory Flashcards")
    root.geometry("980x720")
    root.minsize(700, 520)
    root.configure(bg=BG)

    topic_var = tk.StringVar(value=ALL_TOPICS)
    hide_known_var = tk.BooleanVar(value=False)
    only_missed_var = tk.BooleanVar(value=False)
    shuffle_var = tk.BooleanVar(value=True)
    revealed = {"on": False}

    # --- top bar
    bar = tk.Frame(root, bg=BG)
    bar.pack(fill="x", padx=16, pady=(14, 6))
    tk.Label(bar, text="Topic:", bg=BG, font=("Segoe UI", 10)).pack(side="left")
    combo = ttk.Combobox(bar, textvariable=topic_var, state="readonly", width=38,
                         values=[ALL_TOPICS, TOP_ONLY] + topics())
    combo.pack(side="left", padx=(6, 12))
    for text, var in (("Shuffle", shuffle_var), ("Hide known", hide_known_var),
                      ("Only missed", only_missed_var)):
        tk.Checkbutton(bar, text=text, variable=var, bg=BG, activebackground=BG,
                       command=lambda: restart()).pack(side="left", padx=4)

    # --- header line (topic + counter)
    head = tk.Frame(root, bg=BG)
    head.pack(fill="x", padx=16)
    topic_lbl = tk.Label(head, bg=BG, fg=ACCENT, font=("Segoe UI", 10, "bold"))
    topic_lbl.pack(side="left")
    count_lbl = tk.Label(head, bg=BG, fg=MUTED, font=("Segoe UI", 10))
    count_lbl.pack(side="right")

    # --- card
    card_frame = tk.Frame(root, bg=CARD_BG, highlightbackground="#d8d2c4",
                          highlightthickness=1)
    card_frame.pack(fill="both", expand=True, padx=16, pady=8)

    q_lbl = tk.Label(card_frame, bg=CARD_BG, fg="#1d1d1d", justify="left",
                     anchor="w", font=("Segoe UI", 15, "bold"), wraplength=900)
    q_lbl.pack(fill="x", padx=20, pady=(18, 10))

    a_text = tk.Text(card_frame, bg=CARD_BG, fg="#1d1d1d", wrap="word",
                     relief="flat", font=("Consolas", 12), padx=20, pady=8,
                     spacing1=1, spacing3=1)
    a_scroll = ttk.Scrollbar(card_frame, command=a_text.yview)
    a_text.configure(yscrollcommand=a_scroll.set)
    a_scroll.pack(side="right", fill="y")
    a_text.pack(fill="both", expand=True)

    def on_resize(event):
        q_lbl.configure(wraplength=max(300, event.width - 60))
    card_frame.bind("<Configure>", on_resize)

    # --- buttons
    btns = tk.Frame(root, bg=BG)
    btns.pack(fill="x", padx=16, pady=(0, 6))

    def mk(text, cmd, color):
        return tk.Button(btns, text=text, command=cmd, bg=color, fg="white",
                         activebackground=color, activeforeground="white",
                         relief="flat", font=("Segoe UI", 11, "bold"),
                         padx=14, pady=8, cursor="hand2")

    mk("◀ Back", lambda: (deck.back(), show()), MUTED).pack(side="left")
    mk("✗ Again  (←)", lambda: answer(False), BAD).pack(side="left", padx=8)
    flip_btn = mk("Show answer  (Space)", lambda: flip(), ACCENT)
    flip_btn.pack(side="left", expand=True, fill="x", padx=8)
    mk("✓ Got it  (→)", lambda: answer(True), GOOD).pack(side="left", padx=8)

    status = tk.Label(root, bg=BG, fg=MUTED, font=("Segoe UI", 9), anchor="w")
    status.pack(fill="x", padx=16, pady=(0, 10))

    def reset_progress():
        if messagebox.askyesno("Reset progress", "Forget all known / missed marks?"):
            deck.reset()
            restart()
    tk.Button(bar, text="Reset progress", command=reset_progress,
              relief="flat", bg="#e3ddd0").pack(side="right")

    # --- behaviour
    def set_answer(text):
        a_text.configure(state="normal")
        a_text.delete("1.0", "end")
        a_text.insert("1.0", text)
        a_text.configure(state="disabled")

    def show():
        revealed["on"] = False
        c = deck.current
        total = len(deck.cards)
        known_all = sum(1 for x in CARDS if x["q"] in deck.known)
        status.configure(text=f"Known: {known_all}/{len(CARDS)}   ·   "
                              f"Missed: {len(deck.missed)}   ·   "
                              f"Space flip · → got it · ← again · Backspace back")
        if c is None:
            topic_lbl.configure(text="")
            count_lbl.configure(text=f"{total}/{total}")
            q_lbl.configure(text="Deck finished 🎉" if total else "No cards match these filters.")
            set_answer("Change the topic or filters above, or tick 'Only missed' "
                       "to drill the cards you got wrong.")
            flip_btn.configure(text="Restart deck", command=restart)
            return
        star = "★ " if c["top"] else ""
        topic_lbl.configure(text=star + c["topic"])
        count_lbl.configure(text=f"Card {deck.pos + 1}/{total}")
        q_lbl.configure(text=c["q"])
        set_answer("")
        flip_btn.configure(text="Show answer  (Space)", command=flip)

    def flip():
        c = deck.current
        if c is None:
            restart()
            return
        revealed["on"] = not revealed["on"]
        set_answer(c["a"] if revealed["on"] else "")
        flip_btn.configure(text="Hide answer  (Space)" if revealed["on"]
                           else "Show answer  (Space)")

    def answer(ok):
        if deck.current is None:
            return
        deck.got_it() if ok else deck.again()
        show()

    def restart(*_):
        deck.build(topic_var.get(), hide_known_var.get(),
                   only_missed_var.get(), shuffle_var.get())
        show()

    combo.bind("<<ComboboxSelected>>", restart)
    root.bind("<space>", lambda e: flip())
    root.bind("<Right>", lambda e: answer(True))
    root.bind("2", lambda e: answer(True))
    root.bind("<Left>", lambda e: answer(False))
    root.bind("1", lambda e: answer(False))
    root.bind("<BackSpace>", lambda e: (deck.back(), show()))

    restart()
    root.mainloop()


def self_test():
    """Exercise the deck logic without a display."""
    global PROGRESS_FILE
    PROGRESS_FILE = Path(__file__).with_name("_selftest_progress.json")
    try:
        assert len({c["q"] for c in CARDS}) == len(CARDS), "duplicate questions"
        d = Deck()
        d.reset()
        d.build()
        assert len(d.cards) == len(CARDS)
        first = d.current
        d.again()
        assert d.current is not first and first in d.cards
        d.got_it()
        assert len(d.known) == 1 and len(d.missed) == 1
        d.build(only_missed=True)
        assert [c["q"] for c in d.cards] == [first["q"]]
        d.build(hide_known=True)
        assert len(d.cards) == len(CARDS) - 1
        d.build(topic=TOP_ONLY)
        n_top = len(d.cards)
        for t in topics():
            d.build(topic=t)
            assert d.cards, t
        print(f"OK: {len(CARDS)} cards, {n_top} marked most likely, {len(topics())} topics")
        for t in topics():
            print(f"  {t}: {sum(c['topic'] == t for c in CARDS)}")
    finally:
        PROGRESS_FILE.unlink(missing_ok=True)


if __name__ == "__main__":
    if "--test" in sys.argv:
        self_test()
    else:
        run_gui()
