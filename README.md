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
First observation for conftest.py: If there are severatl subfolders of test - e.g. unit - then the conftest.py is serach first in the current folder (e.g. .test/unit/) and then in the higher level test folder.