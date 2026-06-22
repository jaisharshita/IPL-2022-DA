import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.title("IPL 2022 Data Analytics Dashboard")
st.markdown("""
This interactive dashboard performs an Exploratory Data Analysis (EDA) on the IPL 2022 dataset using **Streamlit** and **Plotly**.
The source dataset contains 74 match rows and 20 distinct columns with no missing records, allowing for a structured deep dive into toss behaviors, venue biases, team dominance, and tournament scoring structures.
""")
df = pd.read_csv("IPL.csv")


st.header("Dataset Overview")
st.write("Rows:", df.shape[0])
st.write("Columns:", df.shape[1])
st.write("Some of the details from data is shown below:")
st.dataframe(df.head())



st.subheader("Total matches won by each team")
match_wins = df['match_winner'].value_counts()
fig = px.bar(x=match_wins.index,y=match_wins.values, color=match_wins.values,
             color_discrete_sequence=px.colors.qualitative.Pastel)
fig.update_layout(xaxis_title="Teams",yaxis_title="Wins")
st.plotly_chart(fig,use_container_width=True)



st.subheader("Toss decision analysis")
st.markdown("""whether the team who won the toss opted for batting or bowling""")
toss = df['toss_decision'].value_counts()
fig = px.bar(x=toss.index,y=toss.values,text=toss.values,
    title='Toss Decision Distribution', color=toss.index )
fig.update_layout(
    xaxis_title='Decision',yaxis_title='Frequency') 
st.plotly_chart(fig, use_container_width=True)



st.subheader("Won by wickets or runs")
st.markdown(""" analysis over throughout the season weather the winning teams won by taking more wickets or by chasing runs, and by seeing chart it can be said that each scenario happened equal times """)
win_type = df['won_by'].value_counts()
fig = px.pie(
    values=win_type.values, names=win_type.index, title='Wins by Runs vs Wickets' )
st.plotly_chart(fig)



st.subheader("Ultimate clutch player of the season")
st.markdown("Who won the most 'man of the match' awards")
pom = df['player_of_the_match'].value_counts().head(10)
fig = px.bar( x=pom.values,y=pom.index,orientation='h', title='Top Player of the Match Winners' , 
              text=pom.values, color=pom.values, color_continuous_scale='Blues')
fig.update_layout( xaxis_title='Awards Won', yaxis_title='Player', title_x=0.5)
fig.show()
st.plotly_chart(fig)
motm_counts = df['player_of_the_match'].value_counts()



st.subheader("Top Scorers of the season")
top_scorers = (
    df.groupby('top_scorer')['highscore'].max().sort_values(ascending=False).head(10))
fig = px.bar(
    x=top_scorers.values,
    y=top_scorers.index,
    orientation='h',
    color=top_scorers.values,
    color_continuous_scale='YlGnBu'
)
st.plotly_chart(fig,use_container_width=True)



st.subheader("Top Bowlers of the season")
df['highest_wickets'] = df['best_bowling_figure'].apply(lambda x : x.split('--')[0])
df['highest_wickets'] = df['highest_wickets'].astype(int)
top_bowlers = (
    df.groupby('best_bowling')['highest_wickets'].sum().sort_values(ascending=False).head(10))
fig = px.bar( x=top_bowlers.index, y=top_bowlers.values, text=top_bowlers.values,
    title='Top Bowlers by Total Wickets', color=top_bowlers.values,
    color_continuous_scale='Mint')
fig.update_layout(
    xaxis_title='Bowler',
    yaxis_title='Total Wickets'
)
fig.update_traces(textposition='outside')
st.plotly_chart(fig)



st.subheader("Top Venues for the matches")
top_venues = df['venue'].value_counts().head(15)
fig = px.bar(x=top_venues.values,y=top_venues.index,orientation='h',title='Top IPL Venues',
            color=top_venues.values, color_continuous_scale='Teal')

fig.update_layout(
    xaxis_title='Matches Hosted',
    yaxis_title='Venue'
)
st.plotly_chart(fig)



st.subheader("Team Dominance")
st.markdown(""" Maximum vs Average Win Margin (Runs)\n This grouped bar chart displays how aggressively teams dominated their opponents when defending a target (winning by runs).""")
run_wins = df[df['won_by'] == 'Runs']
max_margins = run_wins.groupby('match_winner')['margin'].max().sort_values(ascending=False)
avg_margins = run_wins.groupby('match_winner')['margin'].mean()
dominance = pd.DataFrame({
    'Team': max_margins.index,'Max Margin': max_margins.values,
    'Average Margin': avg_margins.loc[max_margins.index].values
})
fig = px.bar(dominance,x='Team',y=['Max Margin', 'Average Margin'],barmode='group',title='Team Dominance Analysis')
fig.update_layout(xaxis_title='Team',yaxis_title='Runs')
st.plotly_chart(fig)



st.subheader("Correlation Heatmap")
st.markdown("""By examining this matrix, we can see if massive individual batting `highscore` or aggressive bowling breakthroughs `highest_wickets` have a stronger mathematical tie to a team's overall safety margin (`margin`) during matches. It helps us understand whether explosive batting or consistent bowling collapses drive larger victory margins in the IPL""")
num_cols = [
    'margin',
    'highscore',
    'highest_wickets'
]
corr = df[num_cols].corr()
fig, ax = plt.subplots(figsize=(4,3))
sns.heatmap(
    corr,
    annot=True,
    cmap='YlGnBu',
    ax=ax,
    cbar_kws={'shrink': 0.7}
)
plt.xticks(fontsize=6)
plt.yticks(fontsize=6)
plt.tight_layout()
st.pyplot(fig)



st.subheader("Toss advantage ")
st.markdown("""analyzes how matches were won based on game strategy (Batting First vs. Batting Second).""")
same = (df['toss_winner']==df['match_winner']).sum()
different = len(df)-same
fig, ax = plt.subplots(figsize=(2,2), facecolor="black") 
patches, texts, autotexts = ax.pie( 
    [same, different], labels=['Won Toss & Won Match', 'Won Toss But Lost Match'], 
    autopct='%1.1f%%', colors=sns.color_palette("pastel"), 
    startangle=90
) 
for text in texts: 
    text.set_color("white") 
    text.set_fontsize(12) 
st.pyplot(fig)




st.subheader("Chasing vs Defending Grounds")
st.markdown(""" shows whether on each ground the winning team chased or defended """)
fig = px.bar(df, y='venue', color='won_by', barmode='group', 
    color_continuous_scale='Teal', 
    title='Chasing vs Defending'
)
fig.update_layout(
    xaxis_title='Number of Matches',
    yaxis_title='Stadium Venue'
)
st.plotly_chart(fig, use_container_width=True)



st.subheader("Average 'Safe' Score to Defend per Venue")
defending_wins = df[df['won_by'] == 'Runs']
avg_defended_score = defending_wins.groupby('venue')['first_ings_score'].mean()
avg_defended_score = avg_defended_score.sort_values()
fig = px.bar(
    x=avg_defended_score.values, y=avg_defended_score.index,
    orientation='h', color=avg_defended_score.values,  
    color_continuous_scale="Teal" , title='Average Score Needed to Successfully Defend and Win'
)
fig.update_layout(
    xaxis_title='Average 1st Innings Score',
    yaxis_title='Stadium Venue',
    showlegend=False 
)
st.plotly_chart(fig)


st.subheader("Does a Massive Individual Score Guarantee Victory?")
st.markdown(""" meaning that whether the player who won man of the match individually took the team towards winning """)
match_results_for_top_scorer = []
for index, row in df.iterrows():
    if row['player_of_the_match'] == row['top_scorer']:
        match_results_for_top_scorer.append('Won Match (MOTM)')
    else:
        match_results_for_top_scorer.append('Did Not Get MOTM')
df['top_scorer_outcome'] = match_results_for_top_scorer
outcome_counts = df['top_scorer_outcome'].value_counts()
fig = px.pie(
    names=outcome_counts.index,
    values=outcome_counts.values,
    title='Top Scorer Performance Relationship to Match Outcomes',
    color_discrete_sequence=px.colors.qualitative.Pastel1,
)

fig.update_traces(
    textinfo='percent+label',
    textfont_size=12,
    marker=dict(line=dict(color='#FFFFFF', width=2))
)
st.plotly_chart(fig)



st.subheader("Group Stages vs Playoff Matches Scoring Trend")
st.markdown( """ (using first innings score) whether there is a difference in the runs scored during the Group Stages of the tournament compared to the high-pressure Playoff Matches (like Semifinals and Finals).column called 'stage' marks whether a match is regular (Group) or sudden-death knockout stage (Playoff). """)
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='stage', y='first_ings_score', palette='Set3')
plt.title('Comparison of Scores: Group Stages vs Playoff Matches')
plt.xlabel('Tournament Stage')
plt.ylabel('1st Innings Scores')
st.pyplot(plt)



st.subheader("Tournament Scoring Patterns: Tracking if Pitches Slow Down Over Time")
st.markdown(""" This visualization tracks the scoring health of tournament tracks over time to evaluate if pitches become slow, tired, and low-scoring as consecutive matches are played on them.""")

df['datetime_clean'] = pd.to_datetime(df['date'].str.replace(' ', ''), format='%B%d,%Y', errors='coerce')
df_chronological = df.sort_values(by='datetime_clean').dropna(subset=['datetime_clean'])

x_numbers = np.arange(len(df_chronological))
slope, intercept = np.polyfit(x_numbers, df_chronological['first_ings_score'], 1)
trend_line_values = (slope * x_numbers) + intercept

df_chronological['rolling_avg_score'] = df_chronological['first_ings_score'].rolling(window=7, min_periods=1).mean()

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df_chronological['datetime_clean'], df_chronological['first_ings_score'], 
        marker='o', alpha=0.3, color='purple', linestyle='-', label='Match Score')
ax.plot(df_chronological['datetime_clean'], df_chronological['rolling_avg_score'], 
        color='black', linewidth=2.5, label='7-Match Rolling Trend')
ax.plot(df_chronological['datetime_clean'], trend_line_values, 
        color='red', linestyle='--', linewidth=2, label='Overall Slope Direction')
ax.set_title('Tournament Scoring Patterns: Tracking if Pitches Slow Down Over Time', fontsize=12, pad=15)
ax.set_xlabel('Match Date', fontsize=10)
ax.set_ylabel('1st Innings Score', fontsize=10)
ax.tick_params(axis='x', rotation=45)
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='upper right')

plt.tight_layout()
st.pyplot(fig)



st.header("Key Insights")
st.success(f"Team with most wins: {match_wins.idxmax()}")
st.success(
    f"Most Player of the Match Awards: {motm_counts.index[0]}"
)
st.success(
    f"Most common toss decision: {toss.idxmax()}"
)
st.success(
    f"Highest winning margin: {df['margin'].max()}"
)