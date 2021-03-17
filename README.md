# sorting_testing_challenge

Complete Solution Details are provided in the attached confluence link.
https://pradeepsheokand.atlassian.net/wiki/spaces/DEVQA/pages/196632/Test+Engineer+Take+Home+Assessment+Solution


Instructions to Run the Python Testing Framework:\
	1) Clone the GitHub Repo:  https://github.com/sheokapr/sorting_testing_challenge  to your local directory\
	2) If not already installed, Install Python version > 3.5\
	3) Create a virtual env using this python command: python -m venv c:\path\to\myenv\
	4) Activate above virtual env: \path\to\myenv\Scripts\activate
	5) Install dependencies using this command (requirements.txt file below has complete dependencies for this project): pip install -r /path/to/requirements.txt\
	[requirements.txt](https://github.com/sheokapr/sorting_testing_challenge/files/6156492/requirements.txt)\
	6) Run this command to execute - Whitebox testing suite: pytest -v test_whitebox_quicksort.py  --html=Reports/Report.html  --durations=0\
	7) Run this command to generate coverage report (html output): pytest  --cov   src   test_whitebox_quicksort.py    --cov-report html\
	8) Run this command to execute - Blackbox testing suite: pytest -v test_blackbox_sorting.py  --html=Reports/Report.html  --durations=0\
        9) Run this command to only execute Performance test suite:  pytest -v -m performance  --html=Reports/Report.html   --durations=0\


