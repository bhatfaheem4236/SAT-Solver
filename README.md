SAT Solver (DPLL Algorithm)
A Boolean Satisfiability (SAT) solver built from scratch in Python, implementing the classic DPLL algorithm (Davis–Putnam–Logemann–Loveland). Includes support for reading standard DIMACS CNF files, and a web interface (FastAPI + HTML/CSS/JS) for interactively solving formulas in the browser.
What is SAT?
The Boolean Satisfiability Problem asks: given a logical formula made of variables connected by AND/OR/NOT, is there an assignment of True/False to each variable that makes the whole formula True? If such an assignment exists, the formula is satisfiable (SAT); otherwise it is unsatisfiable (UNSAT).
SAT is one of the most studied problems in computer science, with applications in scheduling, circuit design, formal verification, and AI planning.
Features
	1	DPLL algorithm — recursive backtracking search with unit propagation
	2	DIMACS CNF file support — read standard .cnf benchmark files
	3	Correctly handles both SAT and UNSAT cases
	4	Web interface — FastAPI backend + HTML/CSS/JS frontend to solve formulas interactively
How it works
	1.	CNF representation — a formula is a list of clauses; each clause is a list of integer literals (positive = variable, negative = its negation)
	2.	Unit propagation — automatically assigns variables forced by clauses with only one unassigned literal left
	3.	DPLL search — picks an unassigned variable, tries True then False, recursing and backtracking on conflicts
	4.	Result — either a satisfying assignment, or UNSATISFIABLE
Project structure
formula.py        Core solver: is_satisfied, unit_propagate, dpll, solve, read_dimacs
app.py            FastAPI backend exposing a /solve endpoint
index.html        Web UI
style.css         Web UI styling
script.js         Web UI logic (calls the API, displays result)
test1.cnf         Example satisfiable formula
test2.cnf           Example unsatisfiable formula
Running it
Command line
python formula.py
Reads test1.cnf by default and prints the result — either a satisfying assignment (e.g. {1: True, 3: True}) or UNSATISFIABLE.
Web interface
Install dependencies:
pip install fastapi uvicorn
Start the backend:
uvicorn app:app --reload
Open index.html in your browser. Enter a formula (one clause per line, space-separated literals), click Solve, and see the result.
Example input:
1 -2
2 3
-1 3
Example: DIMACS form
c Comment line
p cnf 3 3
1 -2 0
2 3 0
-1 3 0
Lines starting with c are comments
	->	The p cnf <vars> <clauses> line is the header
	->	Each remaining line is a clause, ending in 0
Author
Faheem Ul Haq — BS CSDA, IIT Patna
