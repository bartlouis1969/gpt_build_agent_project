# tools.ps1 — snelle dev-taken voor Windows/PowerShell

# Resolve python/pip uit .venv als die bestaat, anders globale
function Get-Py { if (Test-Path .\.venv\Scripts\python.exe) { return ".\.venv\Scripts\python.exe" } "python" }
function Get-Pip { if (Test-Path .\.venv\Scripts\pip.exe) { return ".\.venv\Scripts\pip.exe" } "pip" }

# ============ Taken (zelfde als Makefile) ============
function t { & (Get-Py) -m pytest -q }                                  # test
function l { ruff check . --fix --config ruff.toml }                     # lint
function ty { mypy . --config-file mypy.ini }                             # type
function r { uvicorn app.main:app --reload }                             # run

function f {
    # format
    ruff format . --config ruff.toml
    if (Get-Command black -ErrorAction SilentlyContinue) { black . }
    if (Get-Command isort -ErrorAction SilentlyContinue) { isort . }
}

function fr { & (Get-Pip) freeze > requirements.txt }                     # freeze

function c {
    # clean
    Write-Host "Cleaning caches..." -ForegroundColor Yellow
    Remove-Item -Recurse -Force -ErrorAction SilentlyContinue `
        .pytest_cache, .mypy_cache, dist, build
    Get-ChildItem -Recurse -Filter "__pycache__" | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
}

function all { l; ty; t }                                                 # lint+type+tests

# Helpje
function help-tools {
    @"
tools.ps1 geladen. Beschikbare commando's:
  t    -> tests (pytest -q)
  l    -> lint (ruff --fix)
  ty   -> typecheck (mypy)
  r    -> run devserver (uvicorn --reload)
  f    -> format (ruff format [+ black/isort als aanwezig])
  fr   -> freeze (pip freeze > requirements.txt)
  c    -> clean caches
  all  -> lint + type + tests
"@ | Write-Host
}
