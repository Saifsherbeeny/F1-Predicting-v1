import pandas as pd

# Data from the first 2 races of 2026
drivers_2026 = {
    'ANT': {'team_rank': 1, 'reliability': 98, 'form': 10}, # Won China
    'RUS': {'team_rank': 1, 'reliability': 100, 'form': 8}, # Won Australia
    'LEC': {'team_rank': 2, 'reliability': 95, 'form': 7},
    'PIA': {'team_rank': 2, 'reliability': 90, 'form': 9}, # Fastest in sector 1
    'VER': {'team_rank': 3, 'reliability': 65, 'form': 6}, # Engine DNF risk
}

def run_test_prediction(driver, grid_pos, track_temp):
    stats = drivers_2026[driver]
    score = 100
    
    # Logic 1: Grid Position
    score -= (grid_pos * 4) 
    
    # Logic 2: 2026 Mercedes Engine Advantage (Low Clipping)
    if stats['team_rank'] == 1: score += 12
    
    # Logic 3: Reliability Risk (The "Piastri/Verstappen" factor)
    if stats['reliability'] < 70: score -= 20 
    
    # Logic 4: Form (Recent Wins)
    score += stats['form']
    
    return score

# --- THE TEST: JAPANESE GP 2026 ---
# Actual Qualifying: 1. VER, 2. ANT, 3. PIA, 4. LEC
print("--- PREDICTING JAPANESE GP (Ground Truth Test) ---")
test_results = []
qualifying_grid = {'VER': 1, 'ANT': 2, 'PIA': 3, 'LEC': 4}

for driver, grid in qualifying_grid.items():
    pred_score = run_test_prediction(driver, grid, 22)
    test_results.append((driver, pred_score))

# Sort by highest score
test_results.sort(key=lambda x: x[1], reverse=True)

for rank, (d, s) in enumerate(test_results, 1):
    print(f"{rank}. {d} (Score: {s})")