# Week 3: Grade Reporter & Bug Hunt

- `grade_reporter.py` assigns grades, counts passes and fails, and calculates the average for the provided scores.
- `bug_hunt.py` fixes the loop syntax, includes 5 in the sum, and prints the numeric total as text.

The hardest bug to find was the loop stopping before it reached 5. The program still ran, so it did not raise an error; checking the printed total against the expected answer of 15 showed that the loop's condition needed to include 5.

