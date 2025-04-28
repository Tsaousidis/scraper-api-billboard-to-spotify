## 🎵 Scraper API - Billboard to Spotify 🎧

Α Python automation project that scrapes the Billboard Hot 100 chart for a user-specified date and creates a private Spotify playlist with the top 100 songs of that day.

---

### ✨ Features
- 📅 Prompt user to select any historical date
- 🧠 Scrape Billboard's Hot 100 songs for that date
- 🔍 Search each song on Spotify
- 🎼 Automatically create a private playlist with the matching tracks

---

### 🚀 How to Use
1. Clone this repository
2. Create a `.env` file with your Spotify API credentials:
   ```env
   CLIENT_ID=your_spotify_client_id
   CLIENT_SECRET=your_spotify_client_secret
   REDIRECT_URI=your_redirect_uri
   ```
3. Run the script:
   ```bash
   python main.py
   ```
4. Enter a date in format `YYYY-MM-DD` when prompted
5. Check your Spotify account for the new playlist!

---

### 🖥 Requirements
- Python 3.7+
- spotipy
- beautifulsoup4
- requests
- python-dotenv

Install dependencies:
```bash
pip install -r requirements.txt
```

---

### 🛠 Technologies Used
- Python
- Spotify Web API via `spotipy`
- BeautifulSoup for web scraping
- Requests for HTTP calls
- dotenv for environment management

---

### 🙋‍♂️ Author
👨‍💻 Created by [Tsaousidis](https://github.com/Tsaousidis)

🎉 Have fun exploring music through time! Let me know your thoughts and suggestions! 🎉