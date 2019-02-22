# hudl-test

Automated test case for the following workflow:

1. Log into hudl.com with your credentials.
2. Upload video
3. Share it with the Team Members

## Dependencies

* [Selenium](https://selenium-python.readthedocs.io/installation.html#downloading-python-bindings-for-selenium)
* [Chrome Webdriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
* [Python 3.6](https://www.python.org/downloads/release/python-365/)


## Usage

* Clone the repository
* Place a test video file in the root of the repo
* Update the config.py file with the following parameters:
  
      DRIVER_PATH - path to the downloaded web driver
      USER_NAME - hudl coach user name
      PASSWORD - password for the account
      VIDEO_FILE - name of test video file
      UPLOAD_TIMEOUT - adjustable parameter for the file upload timeout (default 420s)

* Run the test.py as follows:

      python test.py

