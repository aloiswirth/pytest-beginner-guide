# Pytest tutorial

Learning pytest with Eric de Andrade

https://github.com/Pytest-with-Eric/pytest-beginner-guide.git

Video referenced: https://www.youtube.com/watch?v=qPfQM4w4I04

Important Links
https://pytest-with-eric.com/
https://docs.pytest.org/en/stable/
https://github.com/Pytest-with-Eric/pytest-beginner-guide

Pytest with eric.com links to a the page https://pytest-with-eric.com/introduction/how-to-run-pytest-in-vscode/. 
Despite possible little errors it is really enlightening about the usage of testing in VSCode. 
Another good source is https://code.visualstudio.com/docs/python/testing

The error/doubt I found is in "python.testing.cwd": "${workspaceFolder}/tests". For me it only works nicely if I leave this line out of the settings.json.

Settings.json:
{
    "files.autoSave": "onFocusChange",
    "[python]": {
        "editor.defaultFormatter": "ms-python.black-formatter"
    },
    "python.testing.pytestArgs": [],
    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": true,
    "python.testing.cwd": "${workspaceFolder}/tests",
    "python.testing.autoTestDiscoverOnSaveEnabled": true,
}



## Observations
First observation for conftest.py: If there are several subfolders of test - e.g. unit - then the conftest.py is serach first in the current folder (e.g. .test/unit/) and then in the higher level test folder.


Welcome to Pytest with Eric!

Learn to write simple but effective tests with Pytest.

From basics to advanced topics with simple, but detailed explanations and example code. Explore the topics below or on the sidebar to get started.
Getting Started

- [x] How To Run Pytest (python -m pytest vs pytest)
- [x] How To Run Pytest In VS Code (Easy To Follow Step-By-Step Tutorial)
- [x] How To Set Up Pytest With PyCharm (Step-By-Step Guide)
- [x] How To Run Pytest With Poetry (A Step-by-Step Guide)

Basic Concepts

- [x] Maximizing Quality - A Comprehensive Look at Testing in Software Development
- [x] How To Test Python Exception Handling Using Pytest Assert (A Simple Guide)

Testing Best Practices

- [ ] 5 Best Practices For Organizing Tests (Simple And Scalable)
- [ ] Python Testing 101 (How To Decide What To Test)
- [ ] 13 Proven Ways To Improve Test Runtime With Pytest
- [ ] Python Unit Testing Best Practices For Building Reliable Applications

Running Tests

- [ ] How To Run A Single Test In Pytest (Using CLI And Markers)
- [ ] How To Filter Tests Effortlessly With Pytest -K Options

Fixtures

- [ ] How Pytest Fixtures Can Help You Write More Readable And Efficient Tests
- [ ] What Are Pytest Fixture Scopes? (How To Choose The Best Scope For Your Test)
- [ ] A Step-by-Step Guide To Using Pytest Fixtures With Arguments
- [ ] How to Auto-Request Pytest Fixtures Using “Autouse”
- [ ] How To Access Test Details With Pytest Request Fixture
- [ ] What is Setup and Teardown in Pytest? (Importance of a Clean Test Environment)
- [ ] What Is Pytest Caplog? (Everything You Need To Know)
- [ ] How To Manage Temporary Files with Pytest tmp_path

Parametrization

- [ ] How to Effortlessly Generate Unit Test Cases with Pytest Parameterized Tests
- [ ] A Beginner’s Guide To pytest_generate_tests (Explained With 2 Examples)

Mocking

- [ ] Common Mocking Problems And How To Avoid Them (+ Best Practices)
- [ ] How To Mock In Pytest? (A Comprehensive Guide)
- [ ] Mocking Vs. Patching (A Quick Guide For Beginners)
- [ ] What Are Pytest Mock Assert Called Methods and How To Leverage Them
- [ ] The Ultimate Guide To Using Pytest Monkeypatch with 2 Code Examples
- [ ] How To Test Raised Exceptions with Pytest MagicMock? (Advanced Guide)
- [ ] How To Return Multiple Values From Pytest Mock (Practical Guide)
- [ ] How To Easily Resolve The “Fixture ‘Mocker’ Not Found” Error in Pytest
- [ ] How To Mock Celery Tasks With Pytest (Step-by-Step Guide with Examples)

Configuration & Environment Variables

- [ ] How To Overwrite Dynaconf Variables For Testing In Python
- [ ] Pytest Conftest With Best Practices And Real Examples
- [ ] What Is pytest.ini And How To Save Time Using Pytest Config
- [ ] Pytest Config Files - A Practical Guide To Good Config Management
- [ ] How To Ignore Warnings In Pytest (With Examples)
- [ ] 3 Simple Ways To Ignore Test Directories in Pytest
- [ ] The Ultimate Guide To Capturing Stdout/Stderr Output In Pytest
- [ ] How To Use Pytest With Command Line Options (Easy To Follow Guide)
- [ ] 4 Proven Ways To Define Pytest PythonPath and Avoid Module Import Errors
- [ ] 3 Simple Ways To Define Environment Variables In Pytest

Markers

- [ ] Ultimate Guide To Pytest Markers And Good Test Management

Property Based Testing

- [ ] How to Use Hypothesis and Pytest for Robust Property-Based Testing in Python

Async Testing

- [ ] A Practical Guide To Async Testing With Pytest-Asyncio

Flask Testing

- [ ] 3 Proven Ways To Test Your Flask Applications With Pytest

FastAPI Testing

- [ ] Pytest API Testing with FastAPI, SQLAlchemy, Postgres - 1/2
- [ ] Pytest API Testing with FastAPI, SQLAlchemy, Postgres - 2/2
- [ ] Building And Testing FastAPI CRUD APIs With Pytest (Hands-On Tutorial)

Django Testing

- [ ] Comprehensive Step-by-Step Guide to Testing Django REST APIs with Pytest

External/3rd Party API Testing

- [ ] How To Write Tests For External (3rd Party) API Calls With Pytest
- [ ] Python REST API Unit Testing for External APIs

Database Testing

- [ ] How To Test Database Transactions With Pytest And SQLModel

Web Automation Testing

- [ ] How To Use Pytest With Selenium For Web Automation Testing
- [ ] Test Automation Made Easy with Pytest and Playwright
- [ ] How To Create Interactive Test Reports with Pytest and Allure

Pytest Errors and Debugging

- [ ] A Simple Guide to Fixing The ‘Pytest Collected 0 Items’” Error
- [ ] 7 Simple Ways To Fix The “Pytest Command Not Found” Error
- [ ] 5 Simple Techniques To Resolve The Pytest Fixture Not Found Error
- [ ] How To Debug Failing Tests Like A Pro (Use Pytest Verbosity Options)

CI/CD Pipelines

- [ ] Automated Python Unit Testing Made Easy with Pytest and GitHub Actions
- [ ] How To Test And Build Python Packages With Pytest, Tox And Poetry

Plugins and Integrations

- [ ] 8 Useful Pytest Plugins To Make Your Python Unit Tests Easier, Faster and Prettier
- [ ] How To Create Custom HTML Test Reports With pytest-html
- [ ] Parallel Testing Made Easy With pytest-xdist
- [ ] A Simple Guide To Controlling Time in Pytest Using Freezegun
- [ ] How To Measure And Improve Code Efficiency with Pytest Benchmark (The Ultimate Guide)
- [ ] How To Avoid Hanging Tests Using Pytest Timeout (And Save Compute Resource)
- [ ] An Ultimate Guide To Using Pytest Skip Test And XFail - With Examples
- [ ] Save Money On You CI/CD Pipelines Using Pytest Parallel (with Example)
- [ ] A Comprehensive Guide to Pytest Approx for Accurate Numeric Testing

Coverage

- [ ] 3 Simple Ways To Omit Subfolders From Python Coverage Reports
- [ ] How To Measure And Improve Test Coverage With Poetry And Pytest
- [ ] How To Generate Beautiful & Comprehensive Pytest Code Coverage Reports (With Example)

BDD (Behavior-Driven Development)

- [ ] A Complete Guide To Behavior-Driven Testing With Pytest BDD

TDD (Test-Driven Development)

- [ ] How To Practice Test-Driven Development In Python? (Deep Dive)

Hooks

- [ ] Introduction To Pytest Hooks (A Practical Guide For Beginners)
- [ ] What Is The pytest_configure Hook? (A Simple Guide)
- [ ] pytest_sessionstart and pytest_sessionfinish (A Complete Guide)

Testing CLI Applications

- [ ] How To Test CLI Applications With Pytest, Argparse And Typer

Testing AWS Services

- [ ] Easy And Quick Python Local Lambda Unit Testing for AWS Lambda Functions

Misc

- [ ] How To Use Pytest Logging And Print To Console And File (A Practical Guide)
- [ ] 5 Easy Ways To Read JSON Input Data In Pytest

Comparisons

- [ ] Pytest vs Unittest (Honest Review Of The 2 Most Popular Python Testing Frameworks)
- [ ] Practical Overview Of The Top 5 Python Testing Frameworks