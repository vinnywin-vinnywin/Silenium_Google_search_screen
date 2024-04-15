"""
#ссылка на стр с драйвером: https://chromedriver.chromium.org/downloads
#адрес скрита и драйвера: D:\SF_Start29\03_AutoPy\Example_test_text\distr
pip install selenium==4.9.0
pip install pytest-selenium==4.0.0
pip install pytest==6.2.5
#каждый раз для запуска тестов необходимо указать, какой именно браузер мы хотим использовать:
pytest -v --driver Chrome --driver-path
#для запуска в терминале PyCharme:
python -m pytest -v --driver Chrome --driver-path D:/SF_Start29/03_AutoPy/Example_test_text/distr/chromedriver.exe tests/selen.py
"""

import time

def test_search_example(selenium):
    """ Search some phrase in google and make a screenshot of the page. """
    # Open google search page:
    selenium.get('https://google.com')
    time.sleep(5)

    # Find the field for search text input:
    #search_input = selenium.find_element("name", "q") - work done
    search_input = selenium.find_element('xpath', '//*[@id="APjFqb"]') # find_element_by_xpath - AttributeError

    # Enter the text for search:
    search_input.clear()
    search_input.send_keys('first test \n') #input text with enter
    time.sleep(7)

    # Click Search:
    #search_button = selenium.find_element("name", "btnK")
    #search_button.click()
    #time.sleep(7)

    # Make the screenshot of browser window:
    selenium.save_screenshot('result.png')

