import pandas as pd

# 1. THE DATASET (Based on 2026 Season so far)
drivers = {
    'Russell':  {'team_rank': 1, 'avg_grid': 1.5, 'reliability': 100},
    'Antonelli':{'team_rank': 1, 'avg_grid': 2.0, 'reliability': 85},
    'Leclerc':  {'team_rank': 2, 'avg_grid': 3.5, 'reliability': 95},
    'Verstappen':{'team_rank': 3, 'avg_grid': 8.0, 'reliability': 60}, # Had tech issues
}

def predict_winner(driver_name, grid_pos, track_temp):
    stats = drivers[driver_name]
    score = 100 # Start with a perfect score
    
    # Pillar 1: Grid Penalty (Harder to win from the back)
    score -= (grid_pos * 5)
    
    # Pillar 2: 2026 Engine Strength
    if stats['team_rank'] == 1: score += 15 # Mercedes/McLaren (Low Clipping)
    if stats['team_rank'] == 3: score += 5  # Red Bull (High Speed but High Clipping)
    
    # Pillar 3: Temperature/Tire Management
    # In 2026, 35°C+ makes the cars "snappy"
    if track_temp > 35:
        if driver_name == 'Verstappen': score += 10 # Rain/Heat Master
        else: score -= 5
        
    return score

# --- TEST IT ---
temp = 38 # Miami is going to be hot!
print(f"--- Miami GP Prediction (Temp: {temp}°C) ---")

for d in drivers:
    grid = 3 if d == 'Verstappen' else 1 # Let's pretend Max qualifies P3
    final_score = predict_winner(d, grid, temp)
    print(f"{d}: Predictor Score = {final_score}")