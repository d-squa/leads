name: Daily Lead Discovery Run

# Runs once a day on GitHub's infrastructure - no local machine, no
# admin rights, no always-on server needed. Also runnable manually
# from the Actions tab (workflow_dispatch) to test without waiting
# for the schedule.
on:
  schedule:
    # 06:00 UTC daily. GitHub Actions cron is always UTC - adjust the
    # hour to whatever local time works for you.
    - cron: "0 6 * * *"
  workflow_dispatch: {}

permissions:
  contents: write  # required to commit the updated database back to the repo

jobs:
  run-lead-discovery:
    runs-on: ubuntu-latest
    steps:
      - name: Check out repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Write Google service account credentials
        run: |
          mkdir -p credentials
          printf '%s' "$GOOGLE_SERVICE_ACCOUNT_JSON" > credentials/service_account.json
        env:
          GOOGLE_SERVICE_ACCOUNT_JSON: ${{ secrets.GOOGLE_SERVICE_ACCOUNT_JSON }}

      - name: Write .env
        run: |
          cat > .env << EOF
          JOOBLE_API_KEY=${{ secrets.JOOBLE_API_KEY }}
          ADZUNA_APP_ID=${{ secrets.ADZUNA_APP_ID }}
          ADZUNA_APP_KEY=${{ secrets.ADZUNA_APP_KEY }}
          REED_API_KEY=${{ secrets.REED_API_KEY }}
          SEARCH_TERMS=paid media,performance marketing,media buyer,paid social,PPC,media planner
          SEARCH_COUNTRIES=gb,us,de,fr,nl,ae
          TITLE_SCORES_FILE=./config/title_scores.json
          FUZZY_MATCH_THRESHOLD=82
          ATS_WATCHLIST_FILE=./config/ats_watchlist.json
          MIN_SCORE=50
          DATABASE_PATH=./data/lead_discovery.db
          GOOGLE_SHEET_ID=${{ secrets.GOOGLE_SHEET_ID }}
          GOOGLE_SERVICE_ACCOUNT_FILE=./credentials/service_account.json
          LOG_LEVEL=INFO
          LOG_FILE=./logs/lead_discovery.log
          EOF

      - name: Run lead discovery
        run: python main.py

      - name: Commit updated database
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/lead_discovery.db
          git diff --staged --quiet || git commit -m "Update lead database [automated]"
          git push
