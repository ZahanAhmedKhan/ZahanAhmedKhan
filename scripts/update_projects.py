"""Rebuild the projects part of my profile README from my public GitHub repos.

Runs every day through GitHub Actions. How each repo is shown:

- Repos with the topic "featured" go under "Featured Projects". Each one gets
  its title, description, tech table and links, in the same style as before.
- Every other public repo goes in the "Other Projects" table automatically.
- Forks, archived repos, this profile repo and repos with the topic
  "hide-from-profile" are left out.

Where the details come from (fill these in once per repo, under "About" on GitHub):
- Title: the first "# Heading" in the repo's own README (falls back to the repo name)
- Emoji: put one at the start of the repo description, e.g. "🚆 Loads the GO schedule..."
- Description: the repo description
- Tech: the repo topics (python, postgresql, streamlit...)
- Tech table for featured repos: copied from the repo's README, from the first table
  under a heading that contains "Stack" or "Tech" (falls back to the topics)
- Live demo link: the "Website" field
"""
import base64
import json
import os
import re
import urllib.request

USER = "ZahanAhmedKhan"
FEATURED_TOPIC = "featured"
HIDE_TOPIC = "hide-from-profile"
START = "<!-- PROJECTS:START -->"
END = "<!-- PROJECTS:END -->"

# Nicer names for common topics. Any topic not listed is shown title-cased.
TOPIC_NAMES = {
    "python": "Python", "sql": "SQL", "postgresql": "PostgreSQL", "postgres": "PostgreSQL",
    "pandas": "pandas", "duckdb": "DuckDB", "sqlite": "SQLite", "supabase": "Supabase",
    "streamlit": "Streamlit", "pydeck": "pydeck", "grafana": "Grafana", "docker": "Docker",
    "docker-compose": "Docker Compose", "airflow": "Airflow", "dagster": "Dagster", "dbt": "dbt",
    "kafka": "Kafka", "spark": "Spark", "aws": "AWS", "terraform": "Terraform",
    "snowflake": "Snowflake", "iceberg": "Apache Iceberg", "fastapi": "FastAPI", "flask": "Flask",
    "scikit-learn": "scikit-learn", "machine-learning": "Machine Learning", "ocr": "OCR",
    "excel": "Excel", "typescript": "TypeScript", "javascript": "JavaScript", "react": "React",
    "react-native": "React Native", "github-actions": "GitHub Actions", "gtfs": "GTFS",
    "etl": "ETL", "groq": "Groq", "gemini": "Gemini", "openwakeword": "OpenWakeWord",
    "spotify-api": "Spotify API", "ibm-granite": "IBM Granite", "ollama": "Ollama",
    "mediapipe": "MediaPipe", "html": "HTML", "css": "CSS",
}
SKIP_TOPICS = {FEATURED_TOPIC, HIDE_TOPIC}


def github_get(url, raw=False):
    """Call the GitHub API and return the JSON response."""
    request = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        request.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(request) as response:
        return json.load(response)


def get_repos():
    """My public repos, most recently updated first."""
    return github_get(f"https://api.github.com/users/{USER}/repos?per_page=100&sort=pushed")


def get_repo_readme(repo_name):
    """The text of a repo's own README, or an empty string if it has none."""
    try:
        data = github_get(f"https://api.github.com/repos/{USER}/{repo_name}/readme")
        return base64.b64decode(data["content"]).decode("utf-8", errors="ignore")
    except Exception:
        return ""


def should_show(repo):
    if repo["fork"] or repo["archived"]:
        return False
    if repo["name"].lower() == USER.lower():
        return False
    return HIDE_TOPIC not in repo.get("topics", [])


def title_from(repo, readme):
    """Use the README's first '# Heading' as the title, else tidy up the repo name."""
    match = re.search(r"^#\s+(.+)$", readme, flags=re.M)
    if match:
        return match.group(1).strip()
    return repo["name"].replace("-", " ").replace("_", " ").title()


def split_emoji(description):
    """'🚆 Loads the schedule' -> ('🚆 ', 'Loads the schedule'). No emoji -> ('', text)."""
    if description and not description[0].isascii():
        first, _, rest = description.partition(" ")
        return first + " ", rest
    return "", description


def tech_names(repo):
    topics = [t for t in repo.get("topics", []) if t not in SKIP_TOPICS]
    if not topics and repo["language"]:
        topics = [repo["language"].lower()]
    return [TOPIC_NAMES.get(t, t.replace("-", " ").title()) for t in topics]


def stack_table_from(readme):
    """Copy the first markdown table under a heading that mentions 'Stack' or 'Tech'."""
    lines = readme.splitlines()
    in_stack_section = False
    table = []
    for line in lines:
        if line.startswith("#"):
            if table:
                break
            in_stack_section = bool(re.search(r"stack|tech", line, flags=re.I))
            continue
        if in_stack_section and line.strip().startswith("|"):
            table.append(line.strip())
        elif table:
            break
    return "\n".join(table) if len(table) >= 3 else ""


def links_line(repo):
    links = [f"[Code]({repo['html_url']})"]
    if repo.get("homepage"):
        links.append(f"[Live demo]({repo['homepage']})")
    return "🔗 " + " · ".join(links)


def featured_block(repo, readme):
    emoji, description = split_emoji(repo["description"] or "Description coming soon.")
    table = stack_table_from(readme)
    if not table:
        rows = ["| Layer | Technology |", "|-------|------------|"]
        rows.append(f"| Stack | {', '.join(tech_names(repo)) or '-'} |")
        table = "\n".join(rows)
    return "\n".join([f"### {emoji}{title_from(repo, readme)}", description, "", table, "", links_line(repo)])


def other_row(repo, readme):
    emoji, description = split_emoji(repo["description"] or "Description coming soon.")
    description = description.replace("|", "\\|")
    name = f"{emoji}[{title_from(repo, readme)}]({repo['html_url']})"
    return f"| {name} | {description} | {', '.join(tech_names(repo)) or '-'} |"


def build_section(repos):
    featured, others = [], []
    for repo in repos:
        readme = get_repo_readme(repo["name"])
        if FEATURED_TOPIC in repo.get("topics", []):
            featured.append(featured_block(repo, readme))
        else:
            others.append(other_row(repo, readme))

    parts = []
    if featured:
        parts.append("## 🚀 Featured Projects\n\n" + "\n\n".join(featured))
    if others:
        header = "| Project | What it is | Tech |\n|---------|------------|------|"
        parts.append("## 🧩 Other Projects\n\n" + header + "\n" + "\n".join(others))
    return "\n\n---\n\n".join(parts)


def main():
    repos = [repo for repo in get_repos() if should_show(repo)]
    section = build_section(repos)

    with open("README.md", encoding="utf-8") as f:
        readme = f.read()
    if START not in readme or END not in readme:
        raise SystemExit("README.md needs the PROJECTS:START and PROJECTS:END markers.")

    pattern = re.escape(START) + r".*?" + re.escape(END)
    new_readme = re.sub(pattern, lambda _: f"{START}\n{section}\n{END}", readme, flags=re.S)
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_readme)
    print(f"Projects updated: {len(repos)} repos.")


if __name__ == "__main__":
    main()
