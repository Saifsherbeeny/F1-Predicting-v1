import telemetry_test, predictor_brain, dashboard

def run_analysis(race):
    speeds = telemetry_test.get_top_speeds(race)
    drivers, scores = predictor_brain.calculate_scores(race, speeds)
    print(f"\n[ORACLE RESULT] {drivers[0]} is the favorite to win {race}!")
    dashboard.draw_chart(race, drivers, scores)
    dashboard.save_prediction(race, drivers, scores)

def main():
    while True:
        print("\n--- 🏁 2026 F1 ORACLE ---")
        print("1. Miami GP (Next)")
        print("2. Monaco GP")
        print("3. Japan GP (Re-run)")
        print("4. Exit")
        c = input("Choice: ")
        if c == '1': run_analysis('Miami')
        elif c == '2': run_analysis('Monaco')
        elif c == '3': run_analysis('Japan')
        elif c == '4': break

if __name__ == "__main__":
    main()