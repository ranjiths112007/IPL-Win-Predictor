import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load everything
model      = pickle.load(open('model.pkl', 'rb'))
le_team    = pickle.load(open('le_team.pkl', 'rb'))
le_venue   = pickle.load(open('le_venue.pkl', 'rb'))
le_toss    = pickle.load(open('le_toss.pkl', 'rb'))
team_wins  = pickle.load(open('team_wins.pkl', 'rb'))
h2h        = pickle.load(open('h2h.pkl', 'rb'))
venue_wins = pickle.load(open('venue_wins.pkl', 'rb'))
teams      = pickle.load(open('teams.pkl', 'rb'))
venues     = pickle.load(open('venues.pkl', 'rb'))

# Team colors
team_colors = {
    'Chennai Super Kings'        : '#F9CD05',
    'Delhi Capitals'             : '#0078BC',
    'Gujarat Titans'             : '#1C3A6E',
    'Kolkata Knight Riders'      : '#3A225D',
    'Lucknow Super Giants'       : '#A0E0FF',
    'Mumbai Indians'             : '#005DA0',
    'Punjab Kings'               : '#ED1F27',
    'Rajasthan Royals'           : '#EA1A85',
    'Royal Challengers Bengaluru': '#EC1C24',
    'Sunrisers Hyderabad'        : '#F7A721',
}

st.set_page_config(
    page_title="IPL Win Predictor",
    page_icon="🏏",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    body { background-color: #0f0f1a; }
    .main { background-color: #0f0f1a; }
    
    .hero {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        padding: 40px;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 30px;
        border: 1px solid #ffffff15;
    }
    .hero h1 {
        font-size: 3em;
        font-weight: 900;
        color: #ffffff;
        margin: 0;
        letter-spacing: 2px;
    }
    .hero p {
        color: #aaaacc;
        font-size: 1.1em;
        margin-top: 10px;
    }
    .hero .badge {
        display: inline-block;
        background: #f7a72120;
        border: 1px solid #f7a721;
        color: #f7a721;
        padding: 4px 16px;
        border-radius: 20px;
        font-size: 0.85em;
        margin-top: 10px;
    }

    .card {
        background: #1a1a2e;
        border: 1px solid #ffffff15;
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 16px;
    }

    .card h3 {
        color: #aaaacc;
        font-size: 0.8em;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 12px;
    }

    .predict-btn button {
        background: linear-gradient(90deg, #f7a721, #f7541a) !important;
        color: white !important;
        font-size: 1.2em !important;
        font-weight: 700 !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 16px !important;
        width: 100% !important;
        cursor: pointer !important;
        letter-spacing: 1px !important;
    }

    .result-box {
        background: linear-gradient(135deg, #1a1a2e, #0f3460);
        border: 2px solid #f7a721;
        border-radius: 20px;
        padding: 40px;
        text-align: center;
        margin-top: 20px;
    }
    .result-box .winner {
        font-size: 2.5em;
        font-weight: 900;
        color: #f7a721;
    }
    .result-box .trophy {
        font-size: 4em;
    }

    .prob-bar-container {
        background: #ffffff15;
        border-radius: 10px;
        height: 14px;
        margin: 8px 0;
        overflow: hidden;
    }
    .prob-bar-fill {
        height: 100%;
        border-radius: 10px;
        transition: width 0.5s ease;
    }

    .stat-card {
        background: #ffffff08;
        border: 1px solid #ffffff15;
        border-radius: 12px;
        padding: 16px;
        text-align: center;
    }
    .stat-card .val {
        font-size: 2em;
        font-weight: 800;
        color: #f7a721;
    }
    .stat-card .lbl {
        color: #aaaacc;
        font-size: 0.85em;
        margin-top: 4px;
    }

    .stSelectbox label { color: #aaaacc !important; }
    .stSlider label { color: #aaaacc !important; }
    div[data-testid="stSelectbox"] > div {
        background: #ffffff08 !important;
        border: 1px solid #ffffff20 !important;
        border-radius: 10px !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# Hero section
st.markdown("""
<div class="hero">
    <div class="badge">🏆 IPL 2008 – 2025 · 1169 Matches · 63.7% Accuracy</div>
    <h1>🏏 IPL WIN PREDICTOR</h1>
    <p>Powered by Machine Learning · Gradient Boosting · Real IPL Data</p>
</div>
""", unsafe_allow_html=True)

# Stats row
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown('<div class="stat-card"><div class="val">1,169</div><div class="lbl">Matches Trained</div></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="stat-card"><div class="val">63.7%</div><div class="lbl">Model Accuracy</div></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="stat-card"><div class="val">18</div><div class="lbl">IPL Seasons</div></div>', unsafe_allow_html=True)
with c4:
    st.markdown('<div class="stat-card"><div class="val">37</div><div class="lbl">Venues</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Input section
col_left, col_right = st.columns([2, 1])

with col_left:
    st.markdown('<div class="card"><h3>⚔️ Select Teams</h3>', unsafe_allow_html=True)
    t1, t2 = st.columns(2)
    with t1:
        team1 = st.selectbox("🟦 Batting Team", teams, key="t1")
    with t2:
        team2 = st.selectbox("🟥 Bowling Team", teams, key="t2",
                   index=1 if len(teams) > 1 else 0)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card"><h3>🏟️ Venue & Season</h3>', unsafe_allow_html=True)
    venue = st.selectbox("Stadium", venues)
    year  = st.slider("Season Year", 2008, 2025, 2024)
    st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    st.markdown('<div class="card"><h3>🪙 Toss Details</h3>', unsafe_allow_html=True)
    toss_winner   = st.selectbox("Toss Winner", [team1, team2])
    toss_decision = st.selectbox("Decision", ["bat", "field"])
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="predict-btn">', unsafe_allow_html=True)
    predict = st.button("🔮 PREDICT WINNER", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Prediction
if predict:
    if team1 == team2:
        st.error("Please select two different teams!")
    else:
        team1_enc    = le_team.transform([team1])[0]
        team2_enc    = le_team.transform([team2])[0]
        toss_enc     = le_team.transform([toss_winner])[0]
        venue_enc    = le_venue.transform([venue])[0]
        toss_dec_enc = le_toss.transform([toss_decision])[0]

        team1_winrate = team_wins.get(team1, 0.5)
        team2_winrate = 1 - team_wins.get(team2, 0.5)

        h2h_row      = h2h[(h2h['batting_team']==team1) & (h2h['bowling_team']==team2)]
        h2h_winrate  = h2h_row['h2h_winrate'].values[0] if len(h2h_row) > 0 else 0.5

        venue_row    = venue_wins[(venue_wins['batting_team']==team1) & (venue_wins['venue']==venue)]
        venue_winrate= venue_row['venue_winrate'].values[0] if len(venue_row) > 0 else 0.5

        toss_field       = 1 if toss_decision == 'field' else 0
        batting_won_toss = 1 if toss_winner == team1 else 0
        recent_form      = team_wins.get(team1, 0.5)

        input_data = pd.DataFrame([[
            team1_enc, team2_enc, toss_enc, toss_dec_enc,
            venue_enc, year, team1_winrate, team2_winrate,
            toss_field, batting_won_toss, h2h_winrate,
            venue_winrate, recent_form
        ]], columns=[
            'team1_enc','team2_enc','toss_winner_enc','toss_decision_enc',
            'venue_enc','year','team1_winrate','team2_winrate',
            'toss_field','batting_won_toss','h2h_winrate',
            'venue_winrate','team1_recent_form'
        ])

        prob       = model.predict_proba(input_data)[0]
        prediction = model.predict(input_data)[0]

        winner   = team1 if prediction == 1 else team2
        loser    = team2 if prediction == 1 else team1
        win_prob = prob[1]*100 if prediction == 1 else prob[0]*100
        lose_prob= 100 - win_prob

        w_color = team_colors.get(winner, '#f7a721')
        l_color = team_colors.get(loser,  '#aaaacc')

        st.markdown(f"""
        <div class="result-box">
            <div class="trophy">🏆</div>
            <div style="color:#aaaacc; font-size:1em; letter-spacing:3px; margin:10px 0 4px;">PREDICTED WINNER</div>
            <div class="winner" style="color:{w_color};">{winner}</div>
            <div style="color:#aaaacc; margin-top:6px;">wins with {win_prob:.1f}% probability</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # Win probability bars
        r1, r2 = st.columns(2)
        with r1:
            st.markdown(f"""
            <div style="padding:16px; background:#ffffff08; border-radius:12px;">
                <div style="color:{w_color}; font-weight:700; font-size:1.1em;">{team1}</div>
                <div class="prob-bar-container">
                    <div class="prob-bar-fill" style="width:{prob[1]*100:.0f}%; background:{team_colors.get(team1,'#f7a721')};"></div>
                </div>
                <div style="color:white; font-size:1.8em; font-weight:800;">{prob[1]*100:.1f}%</div>
            </div>
            """, unsafe_allow_html=True)

        with r2:
            st.markdown(f"""
            <div style="padding:16px; background:#ffffff08; border-radius:12px;">
                <div style="color:{team_colors.get(team2,'#aaaacc')}; font-weight:700; font-size:1.1em;">{team2}</div>
                <div class="prob-bar-container">
                    <div class="prob-bar-fill" style="width:{prob[0]*100:.0f}%; background:{team_colors.get(team2,'#aaaacc')};"></div>
                </div>
                <div style="color:white; font-size:1.8em; font-weight:800;">{prob[0]*100:.1f}%</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f"""
        <div style="text-align:center; color:#aaaacc; font-size:0.85em;">
            Based on head-to-head records · venue history · recent form · 17 seasons of IPL data
        </div>
        """, unsafe_allow_html=True)