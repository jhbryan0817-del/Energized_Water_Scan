# Verification scripts

`check_stl.py` uses Python 3 standard-library code. Run `python scripts/check_stl.py` from the repository root; it checks the 12 binary STL files and overwrites `verification/RevA1_STL_Check.json`.

`fusion_audit.py` runs **inside Autodesk Fusion**, with the scanner design active. Register/run it as a Fusion Python script, keeping it in this repository's `scripts` directory so `__file__` resolves the adjacent verification folder. It inspects geometry without changing the design and writes `verification/RevA1_Assembly_Audit.json`. The solid Boolean and 71-position steering checks can take several minutes. Recompute the model first. The script is specific to this revision's component names and ideal linkage dimensions; update it if these change.

Read the audit's exclusions before interpreting results. Passing geometry/mesh checks does not qualify sealing, printability, loads or sensing performance.
