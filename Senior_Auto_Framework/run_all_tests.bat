@echo off
echo =======================================================
echo     FPT SENIOR AUTOMATION SHOWCASE - TEST RUNNER
echo =======================================================

echo 1. Checking Virtual Environment...
IF NOT EXIST "C:\Users\Admin\Desktop\Python\FirstProject1\venv\Scripts" (
    echo [INFO] Virtual Environment not found. Creating a new one...
    python -m venv venv
    call venv\Scripts\activate.bat
) ELSE (
    call C:\Users\Admin\Desktop\Python\FirstProject1\venv\Scripts\activate.bat
)

echo.
echo 2. Installing Requirements...
pip install -r requirements.txt

echo.
echo 3. Running Pytest Suite (UI, API, Unit)...
pytest -v -s --html=reports/report.html --alluredir=reports/allure-results

echo.
echo =======================================================
echo TEST EXECUTION COMPLETED! 
echo =======================================================
echo Test Report has been successfully generated!
echo 1. Please open folder: Auto_Framework\reports
echo 2. Double click "report.html" to view the HTML Report.
echo (If you have Java installed, you can also view the Allure Report by running: allure serve reports/allure-results)
pause
