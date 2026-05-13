import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Training data based on 2026 season start (Merc/McLaren/Ferrari dominance)
data = {
    'grid_pos': [1, 2, 3, 5, 1, 2, 10, 4, 6],
    'team_rank': [1, 1, 2, 3, 1, 3, 6, 2, 3], # 1:Merc, 2:Ferrari, 3:McLaren, 6:RBR-Ford
    'track_temp': [35, 38, 30, 32, 40, 35, 28, 33, 30],
    'final_pos': [1, 2, 3, 2, 1, 5, 8, 4, 1]
}
model = RandomForestRegressor(n_estimators=100)
model.fit(pd.DataFrame(data)[['grid_pos', 'team_rank', 'track_temp']], pd.DataFrame(data)['final_pos'])

def calculate_scores(race_name, top_speeds=None):
    # FULL 2026 GRID: [GridPosition, TeamRank, TrackTemp]
    grid_2026 = {
        'ANT': [1, 1, 35], 'RUS': [2, 1, 35], # Mercedes
        'NOR': [5, 3, 35], 'PIA': [3, 3, 35], # McLaren (Reigning Champs)
        'LEC': [4, 2, 35], 'HAM': [6, 2, 35], # Ferrari
        'BEA': [10, 4, 35], 'OCO': [12, 4, 35],# Haas
        'VER': [11, 6, 35], 'HAD': [8, 6, 35], # Red Bull-Ford
        'GAS': [7, 5, 35], 'COL': [14, 5, 35], # Alpine
        'LAW': [9, 7, 35], 'LIN': [13, 7, 35], # Racing Bulls
        'HUL': [15, 8, 35], 'BOR': [16, 8, 35],# Audi
        'SAI': [17, 9, 35], 'ALB': [18, 9, 35],# Williams
        'PER': [19, 10, 35], 'BOT': [20, 10, 35],# Cadillac
        'ALO': [21, 11, 35], 'STR': [22, 11, 35] # Aston-Honda
    }

    raw_results = {}
    for driver, stats in grid_2026.items():
        prediction = model.predict([stats])
        score = max(0, 115 - (prediction[0] * 10))
        
        # STREET CIRCUIT & CHAMPION BONUSES
        if race_name in ['Miami', 'Monaco']:
            if driver in ['HAM', 'NOR', 'LEC', 'VER']: score += 8 # Experience boost
        
        # 2026 ENGINE CLIPPING PENALTY
        if top_speeds and driver in top_speeds and top_speeds[driver] < 330:
            score -= 12
            
        raw_results[driver] = round(score)

    sorted_res = sorted(raw_results.items(), key=lambda x: x[1], reverse=True)
    return [x[0] for x in sorted_res], [x[1] for x in sorted_res]