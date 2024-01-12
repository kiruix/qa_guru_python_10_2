from selene import browser, be, have

def test_google_have_text(browser_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_google_not_have_test(browser_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('wqewqjkdsamn jsakdsan jklasdjasbnms akldsjakld').press_enter()
    browser.element('.card-section [role="heading"]').should(have.exact_text('По запросу wqewqjkdsamn jsakdsan jklasdjasbnms akldsjakld ничего не найдено. '))