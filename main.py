import pandas as pd
import streamlit as st

# Load datasets with caching
@st.cache_data
def load_data():
    matches = pd.read_csv("matches.csv")
    deliveries = pd.read_csv("deliveries.csv")
    return matches, deliveries

matches, deliveries = load_data()

# Data Cleaning
def clean_data(matches):
    matches["winner"].fillna("No Result", inplace=True)
    matches.dropna(subset=["city"], inplace=True)
    matches.fillna({"umpire1": "Unknown", "umpire2": "Unknown", "umpire3": "Unknown"}, inplace=True)
    matches["date"] = pd.to_datetime(matches["date"])
    
    team_name_corrections = {"Delhi Daredevils": "Delhi Capitals", "Deccan Chargers": "Sunrisers Hyderabad", "Rising Pune Supergiant": "Rising Pune Supergiants"}
    matches.replace({"team1": team_name_corrections, "team2": team_name_corrections, "winner": team_name_corrections}, inplace=True)
    
    return matches

matches = clean_data(matches)

# Streamlit App
st.title("\U0001F3CF IPL Analytics Dashboard")

# Sidebar for Navigation
st.sidebar.title("Navigation")
options = [
    "Total Matches Per Season", "Most Successful Teams", "Player of the Match Awards",
    "Venue Analysis", "Top Scorers & Wicket Takers", "Death Over Specialists",
    "Best Finishers", "Most Impactful Players"
]
selected_option = st.sidebar.radio("Select an Analysis", options)

if selected_option == "Total Matches Per Season":
    st.header("Total Matches Played Per Season")
    matches_per_season = matches["season"].value_counts().sort_index()
    st.bar_chart(matches_per_season)

elif selected_option == "Most Successful Teams":
    st.header("Most Successful Teams")
    st.subheader("Win Percentage of Teams: Total Wins/Total Matches Played")
    team_wins = matches["winner"].value_counts()
    matches_played = pd.concat([matches["team1"], matches["team2"]], axis=0).value_counts()
    win_percentage = (team_wins / matches_played) * 100
    win_percentage = win_percentage.sort_values(ascending=False)
    st.bar_chart(win_percentage)

elif selected_option == "Player of the Match Awards":
    st.header("Most Player-of-the-Match Awards")
    player_awards = matches["player_of_match"].value_counts().head(10)
    st.bar_chart(player_awards)

elif selected_option == "Venue Analysis":
    st.header("Best Chasing & Batting Grounds")
    venue_matches = matches["venue"].value_counts().head(10)
    st.subheader("Top 10 Venues by Matches Hosted")
    st.bar_chart(venue_matches)

elif selected_option == "Top Scorers & Wicket Takers":
    st.header("Top Scorers & Wicket Takers")
    top_scorers = deliveries.groupby("batter")["batsman_runs"].sum().sort_values(ascending=False).head(10)
    top_wicket_takers = deliveries[deliveries["is_wicket"] == 1].groupby("bowler")["is_wicket"].count().sort_values(ascending=False).head(10)
    st.bar_chart(top_scorers)
    st.bar_chart(top_wicket_takers)

elif selected_option == "Death Over Specialists":
    st.header("Best Death-Over Bowlers")
    st.subheader("Death-over Bowlers: A cricketer who bowls in the final overs of a match.")
    death_overs = deliveries[(deliveries["over"] >= 16) & (deliveries["over"] <= 20)]
    death_economy = (death_overs.groupby("bowler")["total_runs"].sum() / (death_overs.groupby("bowler")["ball"].count() / 6)).sort_values().head(10)
    st.bar_chart(death_economy)

elif selected_option == "Best Finishers":
    st.header("Best Finishers")
    st.subheader("Finishers: A cricketer who bats in the final overs of a match.")
    last_5 = deliveries[(deliveries["over"] >= 16) & (deliveries["over"] <= 20)]
    finisher_sr = (last_5.groupby("batter")["batsman_runs"].sum() / last_5.groupby("batter")["ball"].count() * 100).sort_values(ascending=False).head(10)
    st.bar_chart(finisher_sr)

elif selected_option == "Most Impactful Players":
    st.header("Most Impactful Players (Runs + Wickets)")
    batsmen_scores = deliveries.groupby("batter")["batsman_runs"].sum()
    bowlers_wickets = deliveries[deliveries["is_wicket"] == 1].groupby("bowler")["is_wicket"].count()
    
    impact_players = pd.DataFrame({"Runs": batsmen_scores, "Wickets": bowlers_wickets}).fillna(0)
    impact_players["Impact Score"] = impact_players["Runs"] + (impact_players["Wickets"] * 20)
    impact_players = impact_players.sort_values("Impact Score", ascending=False).head(10)
    st.bar_chart(impact_players["Impact Score"])

st.sidebar.write("\U0001F680 *Srishti Tayal*")
