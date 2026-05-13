import fastf1
import os

# 1. Create the folder automatically if it doesn't exist
cache_dir = 'f1_cache'
if not os.path.exists(cache_dir):
    os.makedirs(cache_dir)

# 2. Now enable the cache using that folder
fastf1.Cache.enable_cache(cache_dir) 

# Change 'Bahrain' to 'Australia'
session = fastf1.get_session(2026, 'Australia', 'R')
session.load()

# Print the Final Standings
print("--- 2026 AUSTRALIAN GP RESULTS ---")
# We use .head(10) to just see the top 10 finishers
print(session.results[['Abbreviation', 'TeamName', 'ClassifiedPosition', 'Status']].head(10))