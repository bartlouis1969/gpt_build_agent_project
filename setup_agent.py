import os
import subprocess
import sys
import webbrowser


def print_header():
    print("\n=== GPT Build Agent Setup ===\n")


REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
ENV_PATH = os.path.join(REPO_ROOT, ".env")
README_PATH = os.path.join(REPO_ROOT, "README.md")
DRAAIBOEK_PATH = os.path.join(REPO_ROOT, "EA_test_checklist.md")
REQUIREMENTS_PATH = os.path.join(REPO_ROOT, "requirements.txt")


DEFAULT_ENV = (
    "OPENAI_API_KEY=your-key-here\n"
    "MODEL_NAME=gpt-4\n"
    "DEFAULT_TEMPERATURE=0.7\n"
    "MAX_TOKENS=2048\n"
    "GPT_TIMEOUT=60\n"
)


def check_tool(tool, version_arg="--version"):
    try:
        result = subprocess.run([tool, version_arg], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"[OK] {tool} gevonden: {result.stdout.splitlines()[0]}")
            return True
        else:
            print(f"[FOUT] {tool} niet gevonden of geen toegang.")
            return False
    except Exception:
        print(f"[FOUT] {tool} niet gevonden.")
        return False


def create_env():
    if not os.path.exists(ENV_PATH):
        with open(ENV_PATH, "w") as f:
            f.write(DEFAULT_ENV)
        print("[OK] .env aangemaakt met standaardwaarden.")
    else:
        print("[OK] .env bestaat al.")


def install_requirements():
    if os.path.exists(REQUIREMENTS_PATH):
        print("[INFO] Installeer requirements...")
        result = subprocess.run([sys.executable, "-m", "pip", "install", "-r", REQUIREMENTS_PATH])
        if result.returncode == 0:
            print("[OK] Dependencies ge nstalleerd.")
        else:
            print("[FOUT] Installatie dependencies mislukt.")
            sys.exit(1)
    else:
        print("[FOUT] requirements.txt niet gevonden.")
        sys.exit(1)


def run_tests():
    print("[INFO] Draai test suite...")
    result = subprocess.run([sys.executable, "-m", "pytest", "--maxfail=1", "--disable-warnings"])

    if result.returncode == 0:
        print("[OK] Alle tests geslaagd.")
    else:
        print("[FOUT] Test(s) gefaald. Check output.")
        sys.exit(1)


def open_docs():
    print("[INFO] Open README en draaiboek in browser/editor...")
    if os.path.exists(README_PATH):
        webbrowser.open(f"file://{README_PATH}")
    if os.path.exists(DRAAIBOEK_PATH):
        webbrowser.open(f"file://{DRAAIBOEK_PATH}")


def main():
    print_header()
    # Check tools
    all_ok = True
    for tool in ["git", "python", "pip"]:
        if not check_tool(tool):
            all_ok = False
    # Poetry is optioneel
    check_tool("poetry")
    if not all_ok:
        print("[FOUT] Vereiste tools ontbreken. Installeer git, python en pip.")
        sys.exit(1)
    # .env
    create_env()
    # Install requirements
    install_requirements()
    # Run tests
    run_tests()
    # Open docs
    open_docs()
    print("\n[SETUP COMPLEET] Je agent is klaar voor gebruik!\n")


if __name__ == "__main__":
    main()
