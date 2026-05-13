import fastf1

# 1. Load the 2026 Season Standings
# We'll pull data from the last completed round (Japan)
session = fastf1.get_session(2026, 'Japan', 'R')
session.load(laps=False, telemetry=False, weather=False)

print("--- OFFICIAL 2026 CHAMPIONSHIP STANDINGS ---")
# This pulls the actual points table from the API
standings = session.results[['Abbreviation', 'TeamName', 'Points', 'ClassifiedPosition']]
print(standings.head(10))

# 2. Integration Logic
# Your predictor can now use 'Points' as a 'Form' variable!
# Higher Points = Better Driver Form.