## **Information**

This is a tool used to search for links from website to website. For now, this has the function of searching for useful websites without knowing certain keywords, even if it takes a long time.

## **Way to run this program**

```batch
>> python main.py --urls "https://playwright.dev" --chromium "chrome-win/chrome.exe" --output "output.txt" --headless "False"

--urls     : This is select first URL that the program will process. This URL is enclosed in double quotes because it contains special characters (dots and slashes).
--chromium : this is mainly path to chromium app
--output   : This is the path or location where the results from sending the URL will be saved. This path is also enclosed in double quotes.
--headless : This is a boolean value that indicates whether the program should perform a headless mode or not.
```

## **Negative Impact**
Sometimes because this software clicks on random links, and the destination is unknown, it's better to be careful because it could go to a dark website or a website that has bad intentions