import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def load_and_clean_data(filepath: str) -> pd.DataFrame:
    """Loads match scores from a CSV file using Pandas and cleans invalid or missing rows."""
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' not found.")
        return pd.DataFrame(columns=["Player", "Match", "Score"])

    try:
        raw_df = pd.read_csv(filepath)
    except pd.errors.EmptyDataError:
        return pd.DataFrame(columns=["Player", "Match", "Score"])

    required_cols = {"Player", "Match", "Score"}
    if not required_cols.issubset(raw_df.columns):
        print("Error: CSV must contain columns: Player, Match, Score")
        return pd.DataFrame(columns=["Player", "Match", "Score"])

    valid_rows = []
    for idx, row in raw_df.iterrows():
        row_num = idx + 1
        player = str(row["Player"]).strip() if pd.notna(row["Player"]) else ""
        match_val = row["Match"]
        score_val = row["Score"]

        if not player:
            print(f"Row {row_num} skipped: missing Player name.")
            continue

        # Validate Match number
        try:
            match_num = int(float(match_val))
            if match_num <= 0:
                print(f"Row {row_num} skipped: Match must be positive.")
                continue
        except (ValueError, TypeError):
            print(f"Row {row_num} skipped: invalid Match '{match_val}'.")
            continue

        # Validate Score (check missing, non-numeric, or negative)
        if pd.isna(score_val) or str(score_val).strip() == "":
            print(f"Row {row_num} skipped: missing Score.")
            continue

        try:
            score_num = float(score_val)
        except (ValueError, TypeError):
            print(f"Row {row_num} skipped: invalid Score '{score_val}'.")
            continue

        if score_num < 0:
            print(f"Row {row_num} skipped: Score cannot be negative.")
            continue

        valid_rows.append({
            "Player": player,
            "Match": match_num,
            "Score": score_num
        })

    return pd.DataFrame(valid_rows, columns=["Player", "Match", "Score"])


def fmt_num(val: float) -> str:
    """Formats integer-valued floats cleanly without decimal points."""
    return str(int(val)) if val == int(val) else f"{val:.2f}"


def player_stats_menu(df: pd.DataFrame) -> None:
    """Menu Option 1: Uses groupby() to find each player's average, best score, and top performer."""
    grouped = df.groupby("Player", sort=False)["Score"]
    stats_df = grouped.agg(
        Avg="mean",
        Best="max",
        Total="sum",
        StdDev=lambda s: np.std(s.to_numpy(), ddof=0)  # Population standard deviation (np.std default)
    ).reset_index()

    is_single_row = len(df) == 1

    for _, row in stats_df.iterrows():
        player = row["Player"]
        avg_str = f"{row['Avg']:.2f}"
        best_str = fmt_num(row["Best"])
        total_str = fmt_num(row["Total"])
        std_str = f"{row['StdDev']:.2f}"

        if is_single_row:
            print(f"{player}: Avg {avg_str} | Best {best_str} | Std Dev: {std_str}")
        else:
            print(f"{player}: Avg {avg_str} | Best {best_str} | Total {total_str}")

    top_idx = stats_df["Avg"].idxmax()
    top_player = stats_df.loc[top_idx, "Player"]
    top_avg = stats_df.loc[top_idx, "Avg"]

    if is_single_row:
        print(f"Top performer: {top_player}")
    else:
        print(f"Top performer: {top_player} (Avg {top_avg:.2f})")


def statistics_and_trend_menu(df: pd.DataFrame) -> None:
    """Menu Option 2: Calculates NumPy statistics, match-wise trends, and displays Matplotlib charts."""
    scores = df["Score"].to_numpy()

    mean_val = np.mean(scores)
    median_val = np.median(scores)
    std_val = np.std(scores, ddof=0)  # Population standard deviation (np.std default)
    max_val = np.max(scores)
    min_val = np.min(scores)

    max_row = df.loc[df["Score"].idxmax()]
    max_player = max_row["Player"]
    max_match = int(max_row["Match"])

    print(
        f"Mean: {mean_val:.2f} | Median: {median_val:.2f} | "
        f"Std Dev: {std_val:.2f} | Max: {fmt_num(max_val)} "
        f"({max_player}, Match {max_match}) | Min: {fmt_num(min_val)}"
    )

    match_avg = df.groupby("Match")["Score"].mean().sort_index()
    match_str = " | ".join(f"Match {m}: {avg:.2f}" for m, avg in match_avg.items())
    print(f"Match-wise average: {match_str}")

    # Chart 1: Line Chart - Score Trend
    plt.figure(figsize=(8, 5))
    for player, p_data in df.groupby("Player", sort=False):
        p_sorted = p_data.sort_values("Match")
        plt.plot(p_sorted["Match"], p_sorted["Score"], marker="o", label=player)
    plt.plot(match_avg.index, match_avg.values, linestyle="--", color="black", marker="s", label="Match Average")
    plt.title("Score Trend")
    plt.xlabel("Match")
    plt.ylabel("Score")
    plt.xticks(match_avg.index)
    plt.legend()
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.tight_layout()
    print("Line chart 'Score Trend' displayed")
    plt.show()

    # Chart 2: Bar Chart - Player Average vs Best Score
    player_summary = df.groupby("Player", sort=False)["Score"].agg(["mean", "max"])
    x = np.arange(len(player_summary.index))
    width = 0.35

    plt.figure(figsize=(8, 5))
    plt.bar(x - width / 2, player_summary["mean"], width, label="Average Score", color="#2b5c8f")
    plt.bar(x + width / 2, player_summary["max"], width, label="Best Score", color="#e07a3f")
    plt.title("Player Performance Comparison")
    plt.xlabel("Player")
    plt.ylabel("Score")
    plt.xticks(x, player_summary.index)
    plt.legend()
    plt.grid(axis="y", linestyle=":", alpha=0.6)
    plt.tight_layout()
    print("Bar chart 'Player Performance Comparison' displayed")
    plt.show()


def main() -> None:
    filepath = input("Enter CSV filename (press Enter for 'scores.csv'): ").strip() or "scores.csv"
    df = load_and_clean_data(filepath)

    if df.empty:
        print("No valid data to analyse.")
        return

    while True:
        print("\n=== Sports Performance Analyzer ===")
        print("1. Player stats")
        print("2. Statistics and trend")
        print("3. Exit")
        option = input("Enter menu option (1-3): ").strip()

        if option == "1":
            player_stats_menu(df)
        elif option == "2":
            statistics_and_trend_menu(df)
        elif option == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()