import matplotlib.pyplot as plt

def draw_chart(race_name, drivers, scores):
    colors_2026 = {
        'ANT': '#00D2BE', 'RUS': '#00D2BE', # Merc
        'HAM': '#E60000', 'LEC': '#E60000', # Ferrari
        'NOR': '#FF8700', 'PIA': '#FF8700', # McLaren
        'BEA': '#FFFFFF', 'OCO': '#FFFFFF', # Haas
        'VER': '#0600EF', 'HAD': '#0600EF', # Red Bull
        'HUL': '#F5F5F5', 'BOR': '#F5F5F5', # Audi
        'PER': '#FFD700', 'BOT': '#FFD700'  # Cadillac
    }
    
    # Slice for Top 12 to ensure scannability
    top_d, top_s = drivers[:12], scores[:12]
    chart_colors = [colors_2026.get(d, '#808080') for d in top_d]

    plt.figure(figsize=(12, 6))
    bars = plt.bar(top_d, top_s, color=chart_colors, edgecolor='black')
    
    plt.title(f"2026 {race_name.upper()} GP: WINNER CONFIDENCE (FULL GRID)", fontsize=14)
    plt.ylabel("Probability Score (%)")
    plt.ylim(0, 130)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def save_prediction(race_name, drivers, scores):
    import pandas as pd
    pd.DataFrame({'Driver': drivers, 'Score': scores}).to_csv(f'{race_name}_FullGrid.csv')