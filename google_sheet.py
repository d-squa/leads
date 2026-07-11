# Secrets & config
.env
credentials/
credentials/*.json

# Database
# The Actions workflow commits data/lead_discovery.db back to the repo
# after every run - it's the persistence layer for the dedup ledger
# across ephemeral runners, so it must NOT be gitignored. Everything
# else under data/ (e.g. local test databases) still is.
data/*
!data/lead_discovery.db
*.sqlite3

# Logs
logs/
*.log

# Python
__pycache__/
*.py[cod]
*.egg-info/
.pytest_cache/
.venv/
venv/
env/
*.egg

# OS / editor
.DS_Store
.idea/
.vscode/
