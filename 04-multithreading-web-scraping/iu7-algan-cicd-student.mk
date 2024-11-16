all: ready/report.pdf ready/stud-unit-test-report-prev.json ready/stud-unit-test-report.json

ready/report.pdf:
	mkdir -p ./ready
	cp report/report.pdf ready/report.pdf

ready/stud-unit-test-report-prev.json: 
	mkdir -p ./ready
	cp stud-unit-test-report-prev.json ./ready/stud-unit-test-report-prev.json

ready/stud-unit-test-report.json: 
	mkdir -p ./ready
	cp stud-unit-test-report.json ./ready/stud-unit-test-report.json

ready/main-cli-debug.py:
	mkdir -p ./ready
	cp -r ./code/* ./ready/

ready/app-cli-debug:
