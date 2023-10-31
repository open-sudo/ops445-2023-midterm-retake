# ops445-2023-midterms

# Setup

This will download midterm retake locally, allowing you to work on your scripts and upload (push) them back up to GitHub.

1. Use the green **Code** button to copy the HTTPS or SSH link into your clipboard.
1. Clone your assignment repository into your ~/ops445/midterms directory.

```bash
git clone <link> ~/ops445/midterms/
```

# Submission

1. Run your script against the provide students.csv file.  
Please note that this test run script does not check your script docstring or your function docstring.  

```bash
cd ~/ops445/midterms/
pwd #confirm that you are in the right directory
python3 ./midterms.py student_grades.csv stats.csv
```
