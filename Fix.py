import nbformat

# Load the notebook
with open("CNNbasics.ipynb", "r", encoding="utf-8") as f:
    notebook = nbformat.read(f, as_version=4)

# Add missing 'execution_count' values
for cell in notebook.cells:
    if cell.cell_type == "code" and "execution_count" not in cell:
        cell["execution_count"] = None  # Add a placeholder

# Save the fixed notebook
with open("CNNbasics_fixed.ipynb", "w", encoding="utf-8") as f:
    nbformat.write(notebook, f)

print("Notebook repaired and saved as 'CNNbasics_fixed.ipynb'")
