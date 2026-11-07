# CLAUDE.md — Passing Special Mathematics

This repository is a study kit for the **Special Mathematics** course (first-year engineering,
taught in English). It condenses two source documents written by the student:

- **`study-materials/PARTIAL-SPECIAL-MATHEMATICS.pdf`** (11 pages): a typed summary of the
  exercise types, with algorithms and worked examples.
- **`study-materials/CAIET-MS.pdf`** (66 pages, ~48 MB, photographed handwriting): the course +
  seminar notebook. Course pages hold the theory (definitions, propositions, proofs); seminar
  pages hold the worked exercises.

Everything needed to study is reproduced below and in `theory_flashcards.py`, so you rarely
need to open the PDFs. When you do, read them with the Read tool's `pages` parameter (at most
20 pages per call). The notebook in particular is too large to read in one go. Rough page map
of `CAIET-MS.pdf`:
- p.1–7: course, linear SDEs, Prop. 1, Wronskian, constant coefficients (Case I)
- p.8–14: seminar, homogeneous Y' = AY
- p.14–19: course, algorithm, Case II chains, proof for Yₖ, fundamental matrix with properties 1–3
- p.21–28: seminar, nonhomogeneous systems
- p.29–35: course, fundamental matrix properties 4–5, Peano–Baker, constant case, VPF (p.33–34 duplicate p.31–32)
- p.36: course, start of Chapter II (stability)
- p.37–43: seminar, stability with 3 methods (2×2 and 3×3)
- p.44–49: course, stability definitions, proposition, theorem with proof
- p.50–54: seminar, complex functions, values, equations
- p.55–60: course, Routh–Hurwitz and Lyapunov with proofs
- p.61–66: seminar, Re/Im and Cauchy–Riemann

When you (Claude) work in this repo, you are a **tutor helping the student cram for the
partial exam**. Read the "How to tutor" section before answering anything.

---

## 1. Exam facts

| Item | Value |
|---|---|
| Partial exam | **30 points**: Theory 1 + Theory 2 (min. 5) and Problem 1 + Problem 2 (min. 5) |
| Date | The partial was held on **7 November 2026**. (The notebook had noted "Test 9 November (BN104)".) |
| Past questions | [`past-exams/questions.md`](past-exams/questions.md). **Check it first**; real questions outrank the guesses below |
| Rest of grade | Course 10p (presence + answers), Seminar 10p (presence + activity), Final exam 50p |

So the partial is **2 theory questions + 2 problems**.

### What is most likely to be asked

**Theory (ranked):**

1. 🔥🔥🔥 **Fundamental matrix: definition + properties (with proofs).** The professor wrote
   *"Ex: Fundamental matrix. Definition. Properties"* in the notebook. That reads as a sample subject.
2. 🔥🔥🔥 **Stability: definitions (stable / unstable / asymptotically stable) + the 4-case
   theorem with proof.** The seminar notes say *"for theory we have to learn all the cases"*.
3. 🔥🔥 **Proposition 1 (linear combination of solutions) + corollary + Wronskian
   (Propositions 2 and 3).** These have short proofs.
4. 🔥🔥 **Lyapunov theorem + the sufficiency proof** (5 lines).
5. 🔥 **Routh–Hurwitz criterion** (statement, Hurwitz matrix, the Gantmacher-based proof).
6. Medium: Peano–Baker formula and the constant case Φ = e^{A(x−x₀)}; Case I / Case II for
   constant coefficients; the proof that Y_k from a chain is a solution.
7. **Variation of parameters formula: STATEMENT ONLY.** The notebook says *"without proof at the exam"*.

**The 7 November 2026 partial actually asked (theory):**
(1) *Linear and homogeneous SDEs, Case I: the matrix A is diagonalizable*, and
(2) *Differentiability of the complex functions*. So complex-variable topics **can** be theory
questions, even though the notebook has no course pages on them yet. Keep this list updated
from `past-exams/questions.md`.

**Problems (ranked):**

1. 🔥🔥🔥 **Stability of Y' = AY using ALL THREE methods** (eigenvalues, Routh–Hurwitz,
   Lyapunov with a given Q). The summary says *"for the partial exam we have to use all of
   them"* and *"the matrix Q will be always given"*. The seminar did **2×2 and 3×3** cases.
2. 🔥🔥 **Linear homogeneous SDE Y' = AY** (usually 3×3, possibly with principal vectors).
3. 🔥🔥 **Restoration of an analytic function** from Re f or Im f.
4. 🔥 **Nonhomogeneous system Y' = AY + b(x), Y(0) = Y₀** via e^{Ax} (usually 2×2; long).
5. 🔥 **Derivability at a point (Cauchy–Riemann).** Often a short sub-question.
6. Seminar-only extras: Re/Im of complex expressions, values of elementary complex functions,
   solving complex equations (Ln, roots, sh z = 2, …).

---

## 2. How to tutor (instructions for Claude)

- **Order:** start with what is *most likely and easiest*, then go purely from easiest to
  hardest. The order used so far:
  Stability (M1 → M2 → M3) → Cauchy–Riemann → Restoration → Homogeneous Y' = AY → Nonhomogeneous.
- **Step by step.** One topic at a time: algorithm → fully worked example (prefer the
  examples from the student's own PDFs, listed below) → "what to write on the exam" block →
  common mistakes → **one practice problem**. Then stop and wait for the student's answer.
- **Check answers line by line.** Say exactly which step is wrong and why.
- **Explain prerequisites when asked, without condescension.** The student has asked how
  the characteristic equation is formed, what Re(λ) means, and where i comes from (√ of a
  negative number). Answer these with concrete numbers.
- **Show the exam-ready version.** For theory, give clean text the student can copy
  (definition → statement → numbered proof steps → ∎).
- **Flag errors in the source notes** (see §7) every time the topic comes up.
- Use LaTeX or Unicode math, tables for row × column work, and keep each reply focused.
- The exam is in **English**; use the course's notation: σ(A) spectrum, mₐ / m_g
  multiplicities, Φ(x, x₀), Δₖ minors, SDE = system of differential equations.

---

## 3. Theory, written as it should appear on the exam

### 3.1 Linear SDEs: basics

- **Linear SDE:** y_i'(x) = Σⱼ a_ij(x)·y_j(x) + b_i(x), with a_ij, b_i : I → ℝ continuous on an interval I ⊂ ℝ.
- **Matrix form:** **Y'(x) = A(x)Y(x) + b(x)** (1), nonhomogeneous. b₁, …, bₙ are the **perturbing functions**.
- If b ≡ 0, the system is **homogeneous**: **Y'(x) = A(x)Y(x)** (1').
- **Solution:** a vector function Y(x) = (y₁, …, yₙ)ᵀ that satisfies the SDE.
- **General solution:** Y(x, C₁, …, Cₙ) with arbitrary constants Cᵢ ∈ ℝ such that *any* solution is obtained by a suitable choice of the constants. (x represents time.)
- **IVP:** { Y' = A(x)Y + b(x), Y(x₀) = Y₀ }, where x₀ is the initial moment and Y₀ ∈ ℝⁿ the initial position.

### 3.2 Homogeneous SDEs and the Wronskian

**Proposition 1.** Any linear combination of solutions of (1') is a solution of (1').

*Proof.*
1. Let Y₁' = A(x)Y₁ and Y₂' = A(x)Y₂ (2), and let c₁, c₂ ∈ ℝ, Y = c₁Y₁ + c₂Y₂.
2. Then Y' = c₁Y₁' + c₂Y₂' =⁽²⁾ c₁AY₁ + c₂AY₂.
3. Take A(x) as a left common factor: Y' = A(c₁Y₁ + c₂Y₂) = AY. ∎

**Corollary.** The set of solutions of a homogeneous SDE is a linear space.

**Wronskian.** For n solutions Y₁, …, Yₙ: W(x) = det(Y₁(x) … Yₙ(x)), with the solutions as columns.

**Proposition 2.** If Y₁, …, Yₙ are linearly dependent on I, then W(x) = 0 ∀x ∈ I.

*Proof.*
1. Dependence means there are c₁, …, cₙ, **not all 0**, with Σ cₖYₖ(x) = 0 ∀x.
2. Written on components, this is a linear, homogeneous algebraic system in (c₁, …, cₙ).
3. That system has a nonzero solution, so its determinant is 0, i.e. W(x) = 0. ∎

**Proposition 3.** Y₁, …, Yₙ are linearly independent ⇔ W(x) ≠ 0 (by negation of Prop. 2).
Then they form a **basis** of the solution space, and Y = c₁Y₁ + … + cₙYₙ is the **general solution**.

### 3.3 Constant coefficients, Y' = AY

**Case I (A diagonalizable).** A has n linearly independent eigenvectors v₁, …, vₙ with
Avₖ = λₖvₖ, so det(v₁ … vₙ) ≠ 0. Then Yₖ = vₖ·e^{λₖx} are independent solutions, and
**Y = C₁v₁e^{λ₁x} + … + Cₙvₙe^{λₙx}**.

**Multiplicities.**
- mₐ(λ) is the multiplicity of λ as a root of det(A − λI) = 0.
- m_g(λ) is the number of linearly independent eigenvectors of λ, which is the dimension of the eigenspace.
- Always mₐ ≥ m_g.

**Case II (not diagonalizable: some λ has mₐ > m_g).** Use chains of generalised
(principal) vectors:
Av₁ = λv₁ (v₁ ≠ 0), Av₂ = λv₂ + v₁, …, Avₘ = λvₘ + vₘ₋₁. The solutions are:

- Y₁ = v₁e^{λx}
- Y₂ = [ (x/1!)v₁ + v₂ ] e^{λx}
- Y₃ = [ (x²/2!)v₁ + (x/1!)v₂ + v₃ ] e^{λx}
- Yₖ = [ x^{k−1}/(k−1)!·v₁ + … + vₖ ] e^{λx}

*Proof that Yₖ is a solution.*
1. Yₖ' = [x^{k−2}/(k−2)!·v₁ + … + vₖ₋₁]e^{λx} + λ[x^{k−1}/(k−1)!·v₁ + … + vₖ]e^{λx}.
2. AYₖ = [x^{k−1}/(k−1)!·Av₁ + … + Avₖ]e^{λx}.
3. Substitute Av₁ = λv₁ and Avⱼ = λvⱼ + vⱼ₋₁ into step 2. The result equals step 1. ∎

### 3.4 Fundamental matrix ⭐

**Definition.** For the IVP Y' = A(x)Y, Y(x₀) = Y₀, let Yₖ solve Yₖ' = A(x)Yₖ,
Yₖ(x₀) = eₖ (the canonical basis vector). Then
**Φ(x, x₀) = (Y₁(x) Y₂(x) … Yₙ(x))** is the fundamental matrix. (The solutions depend on x₀.)

| # | Property | Proof |
|---|---|---|
| 1 | Φ' = A(x)Φ | Differentiate column by column: (Y₁' … Yₙ') = (AY₁ … AYₙ) = A(Y₁ … Yₙ) |
| 2 | Φ(x₀, x₀) = Iₙ | The columns at x₀ are e₁ … eₙ |
| 3 | Y(x) = Φ(x, x₀)Y₀ solves the IVP | Ỹ' = AΦY₀ = AỸ, and Ỹ(x₀) = IₙY₀ = Y₀; the solution is unique |
| 4 | Φ(x, x₁)Φ(x₁, x₀) = Φ(x, x₀) | On [x₀, x₁], Y(x₁) = Φ(x₁, x₀)Y₀; on [x₁, x], Y(x) = Φ(x, x₁)Y(x₁); on [x₀, x], Y(x) = Φ(x, x₀)Y₀. The solution is unique, so the matrices are equal |
| 5 | Φ(x, x₀)⁻¹ = Φ(x₀, x) | B·A = Iₙ ⇒ A⁻¹ = B. Take A = Φ(x, x₀) and B = Φ(x₀, x): BA = Φ(x₀, x₀) = Iₙ, by properties 4 and 2 |

**Remark.** If M satisfies M' = A(x)M and M(x₀, x₀) = Iₙ, then M = Φ.

**Peano–Baker formula.**
Φ(x, x₀) = Iₙ + ∫ₓ₀ˣ A(s₁)ds₁ + ∫ₓ₀ˣ A(s₁)∫ₓ₀^{s₁} A(s₂)ds₂ds₁ + …

*Proof.* Call the sum M.
1. Differentiate term by term: M' = A(x)[Iₙ + ∫A(s₂)ds₂ + …] = A(x)M.
2. At x = x₀ every integral vanishes, so M(x₀, x₀) = Iₙ.
3. By the Remark, Φ = M. ∎

**Constant A.** The k nested integrals equal (x − x₀)ᵏ/k! (by induction:
∫ₓ₀ˣ (s₁ − x₀)^{k−1}/(k−1)! ds₁ = (x − x₀)ᵏ/k!). So
Φ = Iₙ + A(x−x₀)/1! + (A(x−x₀))²/2! + … = **e^{A(x−x₀)}**, and Y(x) = e^{Ax}Y₀ for x₀ = 0.

**Variation of parameters (VPF), statement only:**
Y(x) = Φ(x, x₀)Y₀ + ∫ₓ₀ˣ Φ(x, s)b(s)ds. For constant A:
**Y(x) = e^{A(x−x₀)}Y₀ + ∫ₓ₀ˣ e^{A(x−s)}b(s)ds.**

### 3.5 Stability ⭐

**Setting.** Y' = AY, Y(0) = Y₀, A constant real n×n, Y(x) = e^{Ax}Y₀.
Y₀ = 0 gives Y ≡ 0, so 0 is the **equilibrium position**. The norm is ‖Y‖ = √(y₁² + … + yₙ²).

**Definitions.**
- **Stable:** ∀ε > 0 ∃δ > 0 such that ∀Y₀ with ‖Y₀‖ < δ, the solution satisfies ‖Y(x)‖ < ε.
- **Unstable:** not stable.
- **Asymptotically stable:** stable, and lim_{x→∞} Y(x) = 0.
- On the exam, draw 3 small graphs: stays inside the ±ε band / leaves the band / oscillations shrinking to 0.

**Proposition.**
- If mₐ(λ) = m_g(λ), then e^{Ax} contains only e^{λx}-type functions for λ.
- If mₐ > m_g, it contains x^k·e^{λx}-type functions.

**Theorem.**
1. Asymptotically stable ⇔ Re λ < 0 ∀λ ∈ σ(A).
2. ∃λ with Re λ > 0 ⇒ unstable.
3. Re λ ≤ 0 ∀λ, and every λ with Re λ = 0 has mₐ = m_g ⇒ stable but **not** asymptotically stable.
4. ∃λ with Re λ = 0 and mₐ > m_g ⇒ unstable.

*Proof.*
- **A.** |e^z| = e^{Re z}, since e^{x+iy} = eˣ(cos y + i sin y). Hence |x^k e^{λx}| = x^k e^{(Re λ)x}.
- **B.** For a > 0, x^k e^{ax} → ∞. For a = −b < 0, x^k/e^{bx} → 0 (L'Hôpital k times).
- **I.** Asymptotically stable ⇔ all functions x^k e^{λx} in e^{Ax} → 0 ⇔ Re λ < 0 ∀λ.
- **II.** Re λ > 0 ⇒ |x^k e^{λx}| → ∞ ⇒ unbounded ⇒ unstable.
- **III.** For Re λ < 0 the terms → 0. For Re λ = 0 only e^{λx} appears, with |e^{λx}| = 1: bounded, but not → 0. So ∃M with ‖e^{Ax}‖ ≤ M. Take δ = ε/M: ‖Y(x)‖ ≤ M‖Y₀‖ < ε, so the system is stable. It is not asymptotically stable because |e^{λx}| = 1 ↛ 0.
- **IV.** Re λ = 0 with mₐ > m_g ⇒ terms x^k e^{λx}, k ≥ 1, with |x^k e^{λx}| = x^k → ∞ ⇒ unstable. ∎

### 3.6 Routh–Hurwitz

**Course notation.**
- P(s) = det(sI − A) = aₙsⁿ + … + a₁s + a₀, with aₙ > 0.
- N⁻, N⁺, N⁰ count the eigenvalues with Re < 0, Re > 0, Re = 0.
- Asymptotically stable ⇔ N⁺ = N⁰ = 0.
- The Hurwitz matrix has rows (aₙ₋₁, aₙ, 0, …), (aₙ₋₃, aₙ₋₂, aₙ₋₁, aₙ, …), …, ending in a₀.
- Minors: Δ₁ = aₙ₋₁, …, Δₙ = det Hₙ.

**Theorem.** Asymptotically stable ⇔ Δ₁ > 0, …, Δₙ > 0.

*Proof (Gantmacher).*
- **Prop. 1:** if all Δᵢ ≠ 0, then N⁰ = 0.
- **Prop. 2:** N⁺ equals the number of sign changes in 1, Δ₁, Δ₂/Δ₁, …, Δₙ/Δₙ₋₁.
- **Sufficiency:** all Δᵢ > 0 ⇒ N⁰ = 0, and there are no sign changes ⇒ N⁺ = 0.
- **Necessity:** N⁺ = 0 ⇒ no sign changes. Starting from 1 > 0, each ratio being positive forces Δ₁ > 0, Δ₂ > 0, … in turn. ∎

### 3.7 Lyapunov equation

- **Positive definite (complex):** P* = P and v*Pv > 0 ∀v ≠ 0.
- **z is real ⇔ z = z̄.** So for a real P, P* = Pᵀ.
- **Positive definite (real):** Pᵀ = P and vᵀPv > 0 ∀v ≠ 0. In practice, use **Sylvester**: all leading minors > 0.

**Theorem.** Y' = AY is asymptotically stable ⇔ **AᵀP + PA = −Q** has a positive definite
solution P for a positive definite Q.

*Sufficiency proof.*
1. Take Av = λv, v ≠ 0, so v*Aᵀ = λ̄v*.
2. Multiply by v* on the left and by v on the right: λ̄v*Pv + λv*Pv = −v*Qv, i.e. 2 Re λ·v*Pv = −v*Qv.
3. v*Pv > 0 and v*Qv > 0, so Re λ < 0. ∎

*Necessity.* P = ∫₀^∞ e^{Aᵀx}Qe^{Ax}dx converges (Gamma-type integrals, since Re λ < 0).

---

## 4. Problem algorithms + worked examples (from the student's PDFs)

### 4.1 Stability with all three methods

**Example (partial PDF):** A = [[−2, 1], [0, −2]], Q = [[16, 0], [0, 2]].

**Method 1 (eigenvalues).**
- det(A − λI) = (−2 − λ)² = 0, so **λ = −2** (double).
- Re λ = −2 < 0 ⇒ asymptotically stable.
- 2×2 shortcut: λ² − tr(A)λ + det A = 0.
- If Δ < 0: λ = −b/2a ± i√(−Δ)/2a, so Re λ = −b/2a.

**Method 2 (Routh–Hurwitz, seminar notation).**
1. P(λ) = det(**λI − A**) = λ² + 4λ + 4.
2. Coefficients from the **highest power down**: **a₀ = 1, a₁ = 4, a₂ = 4**, all > 0.
3. The entry (i, j) of Hₙ is a₂ᵢ₋ⱼ; aₖ = 0 if k < 0 or k > n. So H₂ = [[a₁, a₀], [a₃, a₂]] = [[4, 1], [0, 4]].
4. Δ₁ = 4 > 0, Δ₂ = 16 > 0 ⇒ asymptotically stable.

For 3×3: H₃ = [[a₁, a₀, 0], [a₃, a₂, a₁], [0, 0, a₃]], with Δ₂ = a₁a₂ − a₀a₃ and Δ₃ = a₃Δ₂.

**Method 3 (Lyapunov).**
1. Let P = [[a, b], [b, c]] (3 unknowns, symmetric).
2. Compute **PA**. Since **AᵀP = (PA)ᵀ**, the sum AᵀP + PA has:
   - corners = 2 × the corners of PA
   - off-diagonal = (PA)₁₂ + (PA)₂₁
3. Here PA = [[−2a, a − 2b], [−2b, b − 2c]], so AᵀP + PA = [[−4a, a − 4b], [a − 4b, 2b − 4c]].
4. Set it equal to −Q = [[−16, 0], [0, −2]]: **a = 4, b = 1, c = 1**.
5. P = [[4, 1], [1, 1]], Δ₁ = 4 > 0, Δ₂ = 3 > 0 ⇒ asymptotically stable.

2×2 solving trick: the corner equations give a and c in terms of b; plug those into the
middle equation.

**More examples from the notebook (seminar):**
- A = [[−1, 1], [−1, −1]], Q = [[8, 6], [6, 4]]:
  - λ = −1 ± i
  - P(λ) = λ² + 2λ + 2, H₂ = [[2, 1], [0, 2]]
  - P = [[2, 2], [2, 4]] (Δ₁ = 2, Δ₂ = 4)
- A = [[0, 0, −2], [−1, −1, 1], [1, 0, −3]], Q = [[4, 1, 4], [1, 2, 3], [4, 3, 24]]:
  - λ = −1, −2, −1
  - P(λ) = λ³ + 4λ² + 5λ + 2
  - H₃ = [[4, 1, 0], [2, 5, 4], [0, 0, 2]], with Δ = 4, 18, 36
- A = [[−3, 1, 0], [−1, −3, 0], [0, 0, −1]], Q = [[8, 7, 0], [7, 10, 0], [0, 0, 2]]:
  - λ = −1, −3 ± i
  - P(λ) = λ³ + 7λ² + 16λ + 10
  - H₃ = [[7, 1, 0], [10, 16, 7], [0, 0, 10]], with Δ = 7, 102, 1020
- Practice problems used in tutoring:
  - A = [[−4, 2], [1, −3]], Q = 14I: λ = −2, −5; H₂ = [[7, 1], [0, 10]]; P = [[2, 1], [1, 3]].
  - A = [[−1, 0], [1, −1]], Q = [[2, 0], [0, 4]]: P = [[2, 1], [1, 2]].

### 4.2 Homogeneous system Y' = AY (seminar algorithm)

1. Solve det(A − λI) = 0 for σ(A) and mₐ(λ).
2. For each λ, solve (A − λI)v = 0 to get the eigenspace; m_g(λ) is its dimension.
3. For each λ:
   - **mₐ = m_g = 1:** e^{λx}v.
   - **mₐ = m_g = k ≥ 2:** k independent eigenvectors, each giving e^{λx}vᵢ.
   - **mₐ > m_g = 1:** principal vectors with (A − λI)v_{p1} = v and (A − λI)v_{p2} = v_{p1}. They give e^{λx}(x·v + v_{p1}) and e^{λx}(x²/2!·v + x·v_{p1} + v_{p2}).
4. The general solution is Y = Σ Cᵢ·(solution i).

**Example (partial PDF):** A = [[2, 1, 1], [2, 3, 2], [3, 3, 4]].
1. Add all rows to row 1, which factors out (7 − λ). The result is (7 − λ)(1 − λ)², so λ₁ = 7 (mₐ = 1) and λ₂ = 1 (mₐ = 2).
2. λ = 7 gives v = (1, 2, 3).
3. λ = 1 gives x + y + z = 0, so two vectors: (1, 0, −1) and (0, 1, −1), with m_g = 2 = mₐ.
4. **Y = C₁e^{7x}(1, 2, 3) + C₂eˣ(1, 0, −1) + C₃eˣ(0, 1, −1).**

**Example (notebook, principal vector):** A = [[1, 2, 0], [0, 1, 0], [1, 2, 0]].
1. Eigenvalues: λ = 0 (v = (0, 0, 1)) and λ = 1 with mₐ = 2, m_g = 1 (v = (1, 0, 1)).
2. Principal vector: v_{p1} = (0, 1/2, 0).
3. Y = C₁(0, 0, 1) + C₂eˣ(1, 0, 1) + C₃eˣ[x(1, 0, 1) + (0, 1/2, 0)].

Tip for 3×3 determinants: look for equal row sums or column sums to factor out (c − λ).
For cubics, guess a root (often ±1, ±2) and use Horner's scheme.

### 4.3 Nonhomogeneous system Y' = AY + b(x), Y(0) = Y₀

1. Find the eigenvalues of A.
2. Find **e^{Ax}**:
   - **λ₁ ≠ λ₂:** C = (v₁ v₂), e^{Dx} = diag(e^{λ₁x}, e^{λ₂x}), and **e^{Ax} = Ce^{Dx}C⁻¹**.
   - **λ double (mₐ = 2):** C = (v v_{p1}), **e^{Jx} = e^{λx}[[1, x], [0, 1]]**, and e^{Ax} = Ce^{Jx}C⁻¹.
     Shortcut: **e^{Ax} = e^{λx}[I + x(A − λI)]**.
   - Always check that e^{A·0} = I.
3. Y_h = e^{Ax}Y₀.
4. Y_p = ∫₀ˣ e^{A(x−t)}b(t)dt.
5. Y = Y_h + Y_p.

**Example (partial PDF):** y₁' = −2y₁ + 2y₂, y₂' = y₁ − y₂ + e^{−3x}, Y₀ = (2, 1).
1. λ = 0 and −3, with v₁ = (1, 1) and v₂ = (−2, 1). C = [[1, −2], [1, 1]] and C⁻¹ = ⅓[[1, 2], [−1, 1]].
2. e^{Ax} = ⅓[[1 + 2e^{−3x}, 2 − 2e^{−3x}], [1 − e^{−3x}, 2 + e^{−3x}]].
3. Y_h = ⅓(4 + 2e^{−3x}, 4 − e^{−3x}).
4. Y_p = ⅓(2/3 − (2/3)e^{−3x} − 2xe^{−3x}, 2/3 − (2/3)e^{−3x} + xe^{−3x}).
5. **Y = ⅓(14/3 + (4/3)e^{−3x} − 2xe^{−3x}, 14/3 − (5/3)e^{−3x} + xe^{−3x}).**

**2×2 inverse:** C = [[p, q], [r, s]] gives C⁻¹ = (1/(ps − qr))·[[s, −q], [−r, p]].

### 4.4 Derivability at a point (Cauchy–Riemann)

1. Substitute z = x + iy and get u = Re f, v = Im f.
2. Compute u_x, u_y, v_x, v_y.
3. Check **CR1: u_x = v_y** and **CR2: u_y = −v_x** at (x₀, y₀).
4. If both hold, f is derivable there and f'(z₀) = u_x + i·v_x.

Substitutions:
- z̄ = x − iy
- |z|² = x² + y²
- 1/z = (x − iy)/(x² + y²)
- e^{z̄} = eˣ(cos y − i sin y)

Sanity check: functions of z only (polynomials, e^z, sin, ch, 1/z) are derivable on their
whole domain. Anything with z̄, |z| or Re z is usually derivable only at some points or along a line.

**Examples.**
- f = z·Re z = x² + ixy: derivable **only at 0**.
- f = x² + iy²: derivable on the line **y = x**, with f' = 2x.
- f = (z̄ + 1)e^{z̄} at 0:
  - u = eˣ[(x + 1)cos y − y sin y], v = −eˣ[(x + 1)sin y + y cos y]
  - u_x(0, 0) = 2 ≠ −2 = v_y(0, 0), so it is not derivable.
- f = (z̄ − i)e^{z̄} at z₀ = −i:
  - u_x(0, −1) = cos 1 ≠ −cos 1 = v_y(0, −1), so it is not derivable.

### 4.5 Restoration of an analytic function

0. Check that the given part is **harmonic**: Δu = u_xx + u_yy = 0. If not, stop.
1. If u is known: **f'(z) = u_x − i·u_y**. If v is known: **f'(z) = v_y + i·v_x**.
2. Set y = 0 to get f'(x).
3. Integrate: f(x) = ∫f'(x)dx + C.
4. Replace x by z.
5. Use the given condition to find C.

**Example (partial PDF):** Im f = y + arctan(y/x), f(i) = i.
1. v_x = −y/(x² + y²) and v_y = 1 + x/(x² + y²). Then v_xx = 2xy/(x² + y²)² and v_yy = −2xy/(x² + y²)², so Δv = 0 ✓.
2. f'(z) = 1 + x/(x² + y²) − i·y/(x² + y²).
3. Setting y = 0 gives f'(x) = 1 + 1/x, so f(x) = x + ln x + C.
4. Replacing x by z: f(z) = z + Ln z + C.
5. f(i) = i gives C = −Ln i, so **f(z) = z + Ln z − Ln i, z ≠ 0**.

### 4.6 Elementary complex functions (seminar)

- e^{a+bi} = e^a(cos b + i sin b)
- sin z = (e^{iz} − e^{−iz})/(2i), cos z = (e^{iz} + e^{−iz})/2
- sh z = (e^z − e^{−z})/2, ch z = (e^z + e^{−z})/2
- Ln z = ln|z| + i(θ + 2kπ)
- ⁿ√z = ⁿ√|z|·(cos((θ + 2kπ)/n) + i sin((θ + 2kπ)/n)), k = 0..n−1
- z^α = e^{α·Ln z}

To solve sh z = 2, set t = e^z. This gives t² − 4t − 1 = 0, so t = 2 ± √5, and z = Ln t.

---

## 5. Repository contents

| File | Purpose |
|---|---|
| `CLAUDE.md` | This file: the complete study guide and tutoring instructions |
| `theory_flashcards.py` | Tkinter flashcard app: 57 theory cards in 8 topics, 30 starred as most likely |
| `README.md` | Public overview: what's covered, how to run the app, how to study with Claude Code |
| `study-materials/` | The original PDFs (typed summary + handwritten notebook); they contain the errors listed in §7 |
| `past-exams/` | Past exam papers (empty for now). When papers are added, read them and update the "most likely" rankings in §1 |
| `.gitignore` | Ignores the per-user progress file and Python caches |

### Flashcard app

```bash
python theory_flashcards.py          # open the app (needs Python 3 with tkinter)
python theory_flashcards.py --test   # headless self-test of the deck logic
```

- **Keys:** Space flips the card, → / 2 means "got it", ← / 1 means "again" (the card returns 4 cards later), Backspace goes back.
- **Topic menu:** "★ Most likely (top)" drills only the starred cards. The filters are Shuffle / Hide known / Only missed.
- **Progress** is saved to `flashcards_progress.json` next to the script (gitignored).
- **Code layout:** `card(topic, question, answer, top=False)` appends to `CARDS`. `Deck` holds the
  filtering and requeue logic and has no GUI dependency. `run_gui()` builds the window. `self_test()` checks the deck.
- **Adding a card:** call `card(T?, "question", """answer""", top=True/False)` in the right
  section. Questions must be unique; the self-test asserts this.

---

## 6. Common student mistakes to watch for

1. Using **A − λI** in Method 2. It must be **λI − A**. For 3×3 every sign flips, and a₀ becomes −1.
2. **Reversing the coefficients**: a₀ is the coefficient of the highest power.
3. Using **4 unknowns** in P (it is symmetric), or forgetting the **minus** in −Q.
4. Stopping Lyapunov after solving, without the **Sylvester check on P**.
5. Writing √(−16) = −4. It is **4i**.
6. In C-R, not multiplying out fully before separating u and v. Also forgetting the product rule on eˣ·g.
7. In e^{Ax}, not checking e^{A·0} = I.
8. In Restoration, skipping the harmonic check, or using the wrong f' formula for u vs v.

---

## 7. Known errors in the source notes (always flag these)

| Where | Wrong | Correct |
|---|---|---|
| Partial PDF p.4, homogeneous example | y₁ = eˣ(1, 2, 3) | **y₁ = e^{7x}(1, 2, 3)** (λ₁ = 7) |
| Partial PDF p.8, Method 1 | (−2 − λ)² = 0 ⇒ λ = 2 | **λ = −2** |
| Partial PDF p.8, Method 2 | a₂ = 1, a₁ = 4, a₀ = 4; H₂ = [[4, 4], [0, 1]] | **a₀ = 1, a₁ = 4, a₂ = 4; H₂ = [[4, 1], [0, 4]]**, Δ₂ = 16 (same conclusion) |
| Partial PDF p.9, C-R algorithm step 2 | lists ∂u/∂y twice | the 4th derivative is **∂v/∂y** |
| Partial PDF p.4–5 and notebook, Case II | e^{Jx} = e^{λx}[[x, 1], [0, 1]] | **e^{Jx} = e^{λx}[[1, x], [0, 1]]**. The wrong form gives e^{A·0} ≠ I. This makes the notebook's e^{Ax} for A = [[0, 2], [−2, 4]] wrong; the correct one is e^{2x}[[1 − 2x, 2x], [−2x, 1 + 2x]] |
| Notebook, C-R exercise 3 | u_x(0, −1) = 2 cos 1 | **cos 1** (conclusion unchanged: not derivable) |
| Notebook, Lyapunov theory | "vᵀPv = 0" | **vᵀPv > 0** |
