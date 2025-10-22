import os
import json
import subprocess
import requests
from openai import OpenAI


def load_lessons(path="lessons.json"):
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def generate_patch(lessons, test_output):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    prompt = (
        "Je bent een AI-code agent. Fix de volgende testfouten automatisch.\n"
        f"Lessons: {json.dumps(lessons)}\nTestoutput: {test_output}\n"
        "Geef alleen een geldige patch in unified diff formaat."
    )
    response = client.chat.completions.create(
        model=os.getenv("MODEL_NAME", "gpt-4"),
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=1200,
    )
    return response.choices[0].message.content


def apply_patch(patch):
    with open("patch.diff", "w", encoding="utf-8") as f:
        f.write(patch)
    subprocess.run(["git", "apply", "patch.diff"], check=True)


def create_branch(branch_name):
    subprocess.run(["git", "checkout", "-b", branch_name], check=True)


def commit_and_push(branch_name):
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(
        ["git", "commit", "-m", "🤖 Self-heal: auto patch by agent"], check=True
    )
    subprocess.run(["git", "push", "origin", branch_name], check=True)


def create_pr(branch_name, github_token, repo, title, body):
    url = f"https://api.github.com/repos/{repo}/pulls"
    headers = {"Authorization": f"token {github_token}"}
    data = {
        "title": title,
        "head": branch_name,
        "base": "main",
        "body": body,
    }
    r = requests.post(url, headers=headers, json=data)
    r.raise_for_status()
    return r.json()


def main():
    lessons = load_lessons()
    with open("test_output.txt", "r", encoding="utf-8") as f:
        test_output = f.read()
    patch = generate_patch(lessons, test_output)
    branch_name = "selfheal/auto-fix"
    create_branch(branch_name)
    apply_patch(patch)
    commit_and_push(branch_name)
    github_token = os.getenv("GITHUB_TOKEN")
    github_repo = os.getenv("GITHUB_REPOSITORY")
    pr = create_pr(
        branch_name,
        github_token,
        github_repo,
        "🤖 Self-heal: auto patch by agent",
        "Automatisch gegenereerde fix voor testfouten.",
    )
    print(f"PR aangemaakt: {pr['html_url']}")


if __name__ == "__main__":
    main()
