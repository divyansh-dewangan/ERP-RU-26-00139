# Sports Performance Analyzer

## Overview
Sports Performance Analyzer is a menu-driven Python project that analyses player scores stored in a CSV file. It helps compare player performance and view basic statistics in the terminal.

## Features
- Reads player, match and score details from a CSV file.
- Validates records and skips invalid rows.
- Calculates each player's total, best and average score.
- Ranks players by average score.
- Calculates overall mean, median, minimum, maximum and population standard deviation.
- Optionally saves a bar chart of player averages.

## CSV Format
```csv
Player,Match,Score
Aman,1,40
Aman,2,60
Riya,1,30
Riya,2,50
```

## How to Run
```bash
python "Sports Performance Analyzer.py" sports_data.csv
```

To save a chart:
```bash
python "Sports Performance Analyzer.py" sports_data.csv --chart player_average_chart.png
```

## Technologies
Python 3.8+, CSV handling, and built-in modules including `csv`, `argparse`, `pathlib` and `statistics`. NumPy and Matplotlib are optional.

## Limitations and Future Scope
The current version does not perform match-wise trend analysis, machine-learning predictions, GUI operations or database connectivity. Future versions could add these features and exportable reports.
