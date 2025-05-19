# Gem Hunter

_Gem Hunter is a logic-based puzzle game where players explore a grid to uncover hidden gems and avoid deadly traps. The game uses logical constraints and SAT solving techniques to determine the location of traps and gems._

## Features

- Represent the game grid using logical variables and constraints in **Conjunctive Normal Form (CNF)**.
- Automatically generate CNF constraints based on tile clues.
- Solve the puzzle using:
  - **PySAT** library with modern SAT solvers
  - **Brute-force** algorithm
  - **Backtracking** algorithm
- Compare performance and accuracy of all solving approaches.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/huynhtranty/gem-hunter.git
    cd gem-hunter
    ```
2. (Optional) Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To solve a sample puzzle using CNF and compare solvers:

```bash
python main.py
```

The program will:

- Parse a predefined game grid.
- Encode constraints in CNF.
- Use the PySAT solver to find a satisfying assignment (traps and gems).
- Optionally solve using brute-force and backtracking algorithms.
- Compare and display the running times and solution performance.

### Example Grid Format

A game grid might look like:

```
_ 1 _
_ _ _
2 _ _
```

Where:
- `.` means unknown cell
- `1`, `2`, etc. indicate the number of adjacent traps

You can modify the input grid in `data/board.txt` or a similar file depending on implementation.


## Dependencies

- `python-sat` (PySAT)
- `numpy`
- Others listed in `requirements.txt`