# 🏏 IPL Match Win Predictor

A machine learning web app that predicts IPL match winners
based on 17 years of real IPL data (2008–2025).

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ipl-win-predictor-111.streamlit.app)

---

## 🔗 Live Demo

👉 [https://ipl-win-predictor-111.streamlit.app](https://ipl-win-predictor-111.streamlit.app)

---

## 📌 What It Does

User inputs:
- Batting team
- Bowling team
- Venue / Stadium
- Toss winner
- Toss decision (bat or field)
- Season year

Model outputs:
- Predicted winner
- Win probability for both teams

---

## 📊 Dataset

- Source: Kaggle — IPL Complete Dataset 2008–2025
- 278,205 rows of ball by ball data
- 1,169 matches across 18 seasons
- 64 columns of match information

---

## 🧠 How The Model Works

### Features Used
| Feature | Description |
|---|---|
| team1_winrate | Batting team overall win rate |
| team2_winrate | Bowling team overall win rate |
| h2h_winrate | Head to head win rate between teams |
| venue_winrate | Batting team win rate at this venue |
| team1_recent_form | Last 5 match win rate |
| toss_decision | Bat or field |
| year | Season year |

### Model
- Algorithm: Gradient Boosting Classifier
- Estimators: 300
- Learning rate: 0.05
- Max depth: 4
- Train/Test split: 80/20
- Final accuracy: 63.7%

---

## 🔍 Key Findings

| Factor | Importance |
|---|---|
| Venue win rate | 51% |
| Head to head history | 16% |
| Season year | 8.7% |
| Recent form | 6.3% |
| Toss decision | Less than 1% |

> The toss that everyone obsesses over
> barely affects the result.
> Where you play matters the most.

---

## ✅ Real World Validation

RCB vs SRH — March 28th 2025
at M Chinnaswamy Stadium, Bengaluru

| Source | RCB | SRH |
|---|---|---|
| Google | 55% | 45% |
| Our Model | 55% | 45% |

Exact same prediction. ✅

---

## 🛠️ Tech Stack

- Python 3.11
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
- Streamlit
- Jupyter Notebook
- GitHub + Streamlit Cloud

---

## 📁 Project Structure
```
cricket-predictor/
├── app.py               ← Streamlit web app
├── analysis.ipynb       ← Full ML notebook
├── requirements.txt     ← Dependencies
├── model.pkl            ← Trained ML model
├── le_team.pkl          ← Team label encoder
├── le_venue.pkl         ← Venue label encoder
├── le_toss.pkl          ← Toss label encoder
├── team_wins.pkl        ← Team win rates
├── h2h.pkl              ← Head to head records
├── venue_wins.pkl       ← Venue win rates
├── teams.pkl            ← Active IPL teams list
└── venues.pkl           ← Clean venues list
```

---

## 🚀 Run Locally
```bash
# Clone the repo
git clone https://github.com/yourusername/ipl-win-predictor

# Go into the folder
cd ipl-win-predictor

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## 👨‍💻 Built By

A college student who learned Python from YouTube tutorials
and built this from absolute zero in one week.

---

## ⭐ If you found this useful

Give it a star on GitHub! 🌟
