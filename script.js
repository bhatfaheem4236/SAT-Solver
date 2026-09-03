document.getElementById("solveBtn").addEventListener("click", async () => {
    const input = document.getElementById("formulaInput").value;
    const resultDiv = document.getElementById("result");

    const lines = input.trim().split("\n");
    const formula = lines.map(line =>
        line.trim().split(/\s+/).map(Number)
    );

    try {
        const response = await fetch("http://127.0.0.1:8000/solve", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ formula: formula })
        });

        const data = await response.json();

        if (data.satisfiable) {
            resultDiv.textContent = "SATISFIABLE\n" + JSON.stringify(data.assignment, null, 2);
            resultDiv.className = "satisfiable";
        } else {
            resultDiv.textContent = "UNSATISFIABLE";
            resultDiv.className = "unsatisfiable";
        }
    } catch (error) {
        resultDiv.textContent = "Error: " + error.message;
        resultDiv.className = "unsatisfiable";
    }
});