# Test Case Report: Sports Performance Analyzer

## Testing Summary
The project report documents 12 test cases: **11 passed and 1 failed**.

| Test | Input / Condition | Expected Result | Status |
|---|---|---|---|
| TC1 | Valid CSV, player statistics | Player rankings and summaries displayed | Pass |
| TC2 | Valid CSV, overall statistics | Overall statistics displayed | Pass |
| TC3 | Chart option enabled | PNG chart saved | Pass |
| TC4 | CSV with invalid rows | Invalid rows skipped; valid records analysed | Pass |
| TC5 | Missing CSV file | Error message and exit code 1 | Pass |
| TC6 | Empty CSV file | Error message and exit code 1 | Pass |
| TC7 | Header-only CSV | No valid data message | Pass |
| TC8 | CSV without header | Rows treated as data | Pass |
| TC9 | Invalid menu choice | Invalid choice handled | Pass |
| TC10 | All records invalid | No valid data message | Pass |
| TC11 | Optional libraries unavailable | Statistics work; chart is skipped | Pass |
| TC12 | Decimal score values | Decimal best and total displayed correctly | Fail |

## Failed Test Explanation
TC12 failed because the display logic converts score values to integers, removing the decimal portion. For example, `88.25` may display as `88`.

## Suggested Correction
Keep values as decimals and format them to two decimal places where appropriate:

```python
print(f"Average: {average:.2f} | Best: {best:.2f} | Total: {total:.2f}")
```

## Conclusion
The main features worked in the documented test conditions. The decimal display issue should be corrected and TC12 should be tested again.
