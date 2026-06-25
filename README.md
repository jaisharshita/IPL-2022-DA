# IPL-2022-DA

### Project Overview
This data analytics project performs a full Exploratory Data Analysis (EDA) on the Indian Premier League (IPL) 2022 season dataset. It provides structured insights into match dynamics, team performances, venue behaviors, and scoring trends throughout the tournament. The repository features an interactive web interface that converts complex cricket statistics into real-time visual insights.<br>
### To see the dashboard, kindly refer to the video attached in files section or run the file app.py in anaconda powershell prompt.<br>

### Tech Stack
* **Language:** Python<br>
* **Data Manipulation:** Pandas, NumPy<br>
* **Data Visualization:** Plotly Express, Matplotlib, Seaborn<br>
* **Web Framework:** Streamlit<br>
* **Development Environment:** Jupyter Notebook<br>

### Data Characteristics and Preprocessing
The core dataset consists of 74 match records tracking 20 distinct attributes with high structural integrity.<br>
* **Data Cleanliness:** The raw dataset contains zero missing values, allowing immediate analytical computation without synthetic row imputation.<br>
* **Feature Parsing:** String-to-datetime object casting applied to match dates to map temporal progression across the tournament timeline.<br>
* **Statistical Grouping:** Uses categorical indexing to isolate critical situational factors including toss decisions, player-of-the-match frequencies, and stadium metrics.<br>

### Key Insights and Metrics Showcased
The notebook and interactive dashboard visually illustrate several strategic variables from the 2022 season:<br>
* **Team Dominance Profiling:** Evaluates the distribution of match wins to highlight the most successful franchises across the tournament framework.<br>
* **Toss Decision Optimization:** Breaks down team preferences between choosing to bat or bowl first after winning the toss.<br>
* **Match Outcomes by Strategy:** Correlates the toss-winning choices directly with final match victories to detect strategic advantages.<br>
* **High-Impact Player Rankings:** Flags individual player consistency by identifying and sorting the athletes with the most Player of the Match awards.<br>
* **Venue Bias Analysis:** Highlights specific match venues to expose whether a given stadium favors defending a total or chasing down a score.<br>
* **Chronological Pitch Degradation:** Leverages linear regression slopes alongside 7-match rolling averages to evaluate if first-innings scores slow down as pitches wear out over time.<br>

### Repository Components
* **ipl.ipynb:** The developmental Jupyter Notebook built for data exploration, initial mathematical profiling, statistical trends, and static charting.<br>
* **app.py:** The dynamic production script utilizing Streamlit and interactive Plotly visualization layers to construct the user-facing web dashboard.<br>
