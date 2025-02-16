# Amazon Search Results Scraper 🛒

## 📌 Overview
This script scrapes data from Amazon search results, extracting:
- **Sponsored Brand Video Ads**
- **Banner Ads**
- **Sponsored Ads (SP Ad1, SP AD2, SP AD3, SP AD4)**
- **Product Prices**

After scraping, the extracted data is uploaded to **Google Sheets** for easy access and analysis.

## 🔧 Technologies Used
- **Selenium** - For browser automation
- **BeautifulSoup** - For parsing and extracting data from HTML
- **Pandas** - For data processing and structuring
- **gspread** - For uploading data to Google Sheets

## 🚀 How to Use
### 1️⃣ Install Dependencies
Ensure you have Python installed, then install the required libraries:
```bash
pip install -r requirements.txt
```

### 2️⃣ Setup Google Sheets API
1. [Enable API Access for a Project](https://docs.gspread.org/en/latest/oauth2.html#enable-api-access) if you haven’t done it.

2. Go to “APIs & Services > Credentials” and choose “Create credentials > Service account key”.

3. Fill out the form

4. Click “Create” and “Done”.

5. Press “Manage service accounts” above Service Accounts.

6. Press on ⋮ near recently created service account and select “Manage keys” and then click on “ADD KEY > Create new key”.

7. Select JSON key type and press “Create”.

8. Save this as "cred_file.json" in the same directory.

### 3️⃣ Run the Script
```bash
python amazon_scraper.py
```

## 🛠 Features
- Scrapes multiple Amazon search results
- Extracts sponsored and organic product data
- Saves structured data in **Google Sheets**
- Handles **dynamic content loading** with Selenium
- **Avoids detection** using proper request intervals

## 📌 Notes
- Use a **headless browser** mode to reduce detection.
- Adjust search queries inside `scraper.py`.
- Modify Google Sheets configurations as needed.

## 🤝 Contributions
Feel free to submit pull requests or report issues to improve the script!


---
**Happy Scraping! 🚀**
