# Passing Special Mathematics

A cram kit for the **Special Mathematics** partial exam: systems of differential equations,
stability, and functions of a complex variable.

It has three parts:

- **[`CLAUDE.md`](CLAUDE.md)** is the full study guide. It covers every theory item written the
  way it should appear on the exam (definitions, statements, numbered proofs), every problem
  type with its algorithm and a worked example, common mistakes, and a list of errors found in
  the original course notes. It also tells [Claude Code](https://claude.com/claude-code) how to
  tutor from this material, so you can open the repo in Claude Code and say *"quiz me"*.
- **[`theory_flashcards.py`](theory_flashcards.py)** is a desktop flashcard app with 57 theory
  cards in 8 topics. The 30 most likely exam questions are starred.
- **[`study-materials/`](study-materials)** holds the original PDFs: the typed exercise summary
  and the handwritten course notebook.
- **[`past-exams/`](past-exams)** holds past exam questions. See
  [`questions.md`](past-exams/questions.md); it starts with the 7 November 2026 partial.

## What's covered

| # | Topic | Theory | Problems |
|---|---|---|---|
| 1 | Linear SDEs: basics | definitions, IVP | |
| 2 | Homogeneous SDEs & Wronskian | Prop. 1–3 with proofs | |
| 3 | Constant coefficients Y' = AY | Case I / II, principal vectors | general solution (3×3) |
| 4 | Fundamental matrix ⭐ | definition, 5 properties, Peano–Baker, e^{A(x−x₀)}, VPF | nonhomogeneous systems via e^{Ax} |
| 5 | Stability ⭐ | definitions, 4-case theorem with proof | |
| 6 | Routh–Hurwitz | Hurwitz matrix, criterion, proof | stability, Method 2 |
| 7 | Lyapunov equation | positive definiteness, theorem, proof | stability, Method 3 |
| 8 | Complex variable | | Cauchy–Riemann, restoring an analytic function, elementary functions |

⭐ marks the topics most likely to be asked on the exam.

## Exam format

The partial is worth **30 points**: **2 theory questions + 2 problems**, with a minimum score
on each part. The stability problem is expected to use **all three methods**: eigenvalues,
Routh–Hurwitz, and Lyapunov with a given Q.

## Running the flashcards

You need **Python 3** with tkinter. The standard installer from
[python.org](https://www.python.org/downloads/) includes it. On Windows you can also run
`winget install Python.Python.3.12`.

```bash
git clone https://github.com/MateiSebastian9/passing-special-mathematics.git
cd passing-special-mathematics
python theory_flashcards.py
```

| Key | Action |
|---|---|
| `Space` | flip the card |
| `→` or `2` | got it |
| `←` or `1` | again (the card comes back a few cards later) |
| `Backspace` | previous card |

- Pick **"★ Most likely (top)"** in the topic menu for a quick final review.
- Tick **"Only missed"** to go back over the cards you got wrong.
- Your progress is saved locally in `flashcards_progress.json`. Git ignores this file.

To check the deck logic without opening a window:

```bash
python theory_flashcards.py --test
```

## Studying with Claude Code

Open the folder in Claude Code and ask for what you need, for example:

- *"Quiz me on the fundamental matrix properties."*
- *"Walk me through stability with all three methods, then give me a practice matrix."*
- *"Check my answer:"* followed by your work.

Claude reads `CLAUDE.md` and tutors you in the right order (most likely and easiest first),
in the exam's notation.

## Study materials

The original notes are in [`study-materials/`](study-materials):

| File | What it is |
|---|---|
| [`PARTIAL-SPECIAL-MATHEMATICS.pdf`](study-materials/PARTIAL-SPECIAL-MATHEMATICS.pdf) | 11-page typed summary: an algorithm and a worked example for each exercise type |
| [`CAIET-MS.pdf`](study-materials/CAIET-MS.pdf) | 66-page handwritten course + seminar notebook (theory with proofs, solved seminar exercises; ~48 MB) |

⚠️ Both PDFs contain a few mistakes. For example, Case II writes e^{Jx} = e^{λx}[[x, 1], [0, 1]]
where it should be [[1, x], [0, 1]]. Every error found is corrected and listed in
[`CLAUDE.md` §7](CLAUDE.md#7-known-errors-in-the-source-notes-always-flag-these).
Trust the guide where the two disagree.
