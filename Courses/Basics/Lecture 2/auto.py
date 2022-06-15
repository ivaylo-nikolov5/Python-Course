import webbrowser as wb

def web_automation():
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    URLS = ("https://softuni.bg/trainings/3609/programming-fundamentals-with-python-january-2022#lesson-36319", "youtube.com", "https://translate.google.com/")

    for url in URLS:
        print(f"Opening: {url}")
        wb.get(chrome_path).open(url)

web_automation()
