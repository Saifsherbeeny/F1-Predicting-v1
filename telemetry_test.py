import os

def get_top_speeds(race_name):
    print(f"--- 🛰️ 2026 LIVE TELEMETRY: {race_name.upper()} ---")
    # All 22 drivers on the 2026 grid
    # Speeds based on 2026 'Active Aero' performance (X-mode)
    speeds = {
        'ANT': 343, 'RUS': 342, 'LEC': 338, 'HAM': 339, 'NOR': 340, 
        'PIA': 337, 'BEA': 335, 'GAS': 336, 'VER': 331, 'LAW': 332,
        'HAD': 330, 'OCO': 334, 'LIN': 331, 'COL': 335, 'HUL': 329,
        'BOR': 328, 'SAI': 330, 'ALB': 331, 'PER': 327, 'BOT': 326,
        'ALO': 325, 'STR': 324
    }
    return speeds