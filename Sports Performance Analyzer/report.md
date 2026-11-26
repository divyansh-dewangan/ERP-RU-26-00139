# Project Report: Sports Performance Analyzer

## 1. Introduction
Sports Performance Analyzer is a Python project that analyses sports scores stored in a CSV file. It provides player-wise summaries and overall statistical information through a simple terminal menu.

## 2. Objectives
- Read sports records from a CSV file.
- Validate input and handle incorrect records.
- Calculate total, best and average scores for each player.
- Display overall statistical values.
- Show player rankings and optionally generate a chart.

## 3. Tools and Technologies
The project uses Python 3.8 or later and built-in modules such as `csv`, `argparse`, `pathlib` and `statistics`. NumPy and Matplotlib are optional libraries.

## 4. Working
The program accepts a CSV file path, reads the records and validates the player name, match number and score. Invalid rows are skipped with a message. Valid scores are grouped by player.

It calculates each player's total, best and average score. It also calculates the overall mean, median, minimum, maximum and population standard deviation. Users can choose player statistics or overall statistics from the terminal menu. A chart can be saved when requested and when Matplotlib is available.

## 5. Main Functions
- `parse_arguments()` – reads command-line arguments.
- `to_float()` – helper for numeric conversion.
- `safe_mean()` – calculates mean safely.
- `safe_std()` – calculates population standard deviation.
- `load_scores()` – reads and validates CSV records.
- `player_summary()` – calculates player summaries and rankings.
- `overall_summary()` – calculates overall statistics.
- `display_player_stats()` – displays player performance.
- `display_overall_stats()` – displays overall statistics.
- `save_player_chart()` – creates a bar chart.
- `run_menu()` – handles menu choices.
- `main()` – controls program execution.

## 6. Sample Results
According to the project sample dataset, Diya is the top performer with an average score of 89.00. Overall mean is 76.12, median is 76.00, minimum is 55, maximum is 95 and population standard deviation is 11.51.

## 7. Limitations
The current version does not calculate match-wise trends, predict future scores, use machine learning, or provide a GUI or database connection. The documented decimal-score display test also identifies an issue where integer conversion truncates decimal values.

## 8. Conclusion
The project demonstrates Python functions, CSV handling, input validation, data structures and statistical calculations. It provides a simple way to summarize and compare player scores. Future improvements may include trend analysis, report export and a graphical interface.
