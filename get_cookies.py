import undetected_chromedriver as uc

if __name__ == '__main__':
    options = uc.ChromeOptions()
    options.add_argument(f'--user-data-dir=/Users/mac/Library/Application Support/Google/Chrome/Default') # chrome profile location
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
    options.add_argument('--load-extension=C:\\temp\\plugin-folder')
    driver = uc.Chrome(options=options)
    driver.get('https://www.google.com')
    driver.quit()
