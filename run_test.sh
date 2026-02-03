#!/bin/bash
pytest --alluredir test-reports/25-01-29-1st-info-001
npx allure generate ./test-reports/25-01-29-1st-info-001
cd allure-report
echo check out your http://127.0.0.1:8000 in a sec
python -m http.server
