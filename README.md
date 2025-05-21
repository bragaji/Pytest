Pytest implementation for API testing

#steps to generate allure report
# Run tests and collect results
pytest --alluredir=allure-results

# Generate and view new report
allure generate allure-results --clean -o allure-report
allure open allure-report