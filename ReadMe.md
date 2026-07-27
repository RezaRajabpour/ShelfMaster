# 📚 LibManager

> A simple yet powerful library management desktop app built with PyQt6.  
> It's got a modern look, dark/light mode, and handles all the boring stuff like books, authors, publishers, and more — so you don't have to.

---

## 📸 Screenshots

> **Main Window – Dark Theme**  
> ![Main Window Dark](<img width="1920" height="886" alt="IMG_20260727_143454" src="https://github.com/user-attachments/assets/ae90b2bf-d446-4195-b881-f53a1819b92c" />)

> **Main Window – Light Theme**  
> ![Main Window Light](<img width="1920" height="962" alt="IMG_20260727_143503" src="https://github.com/user-attachments/assets/a911c123-e33a-4dd0-b4aa-483bdb20833c" />)

> **Add translator Dialog**  
> ![Add translator Dialog](<img width="1434" height="1100" alt="۲۰۲۶۰۷۲۷_۱۴۴۰۴۱" src="https://github.com/user-attachments/assets/ffc1a0f0-dea4-4647-9c27-caf2c163feca" />)

---

## ✨ What it does

- Manage books, authors, translators, publishers, genres, languages, resources, and ESRB ratings  
- Search anything instantly — just start typing  
- Add new entries with a single click (`+` button)  
- Delete stuff too (but it’ll ask you first, don't worry)  
- Dark / Light theme — switch anytime from the menu  
- Sidebar icons are SVG, so they stay sharp and change color with the theme  
- Code is split cleanly: GUI, logic, and data are in their own places  

---

## 🛠️ Built with

- Python 3.8+  
- PyQt6 for the interface  
- SQLite for storage (nothing fancy, just works)  
- Good old CSS-like stylesheets for the UI  

---

## 🚀 Getting it running

```bash
git clone https://github.com/yourusername/LibManager.git
cd LibManager
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

That's it. Should pop right up.

---

## 📁 How it's organized

```
LibManager/
├── app/
│   ├── api/adapters/     # talks to the database
│   ├── gui/              # all the UI widgets and dialogs
│   ├── logic/            # business rules (if any)
│   └── utils/            # random helpers
├── database/             # the actual .db file
├── screenshots/          # screenshots for README
├── tests/                # (hopefully) some tests
├── main.py               # start here
└── requirements.txt      # what you need to install
```

Nothing crazy — pretty standard Python project layout.

---

## 🖥️ How to use it

1. Pick a section from the sidebar (Books, Authors, etc.)  
2. Use the search box to filter the list — updates as you type  
3. Hit the `+` button to open a dialog and add something new  
4. Select an item and press `Delete` to remove it (you'll get a confirmation prompt)  
5. Change the theme from `Settings → Appearance` if the default isn't your vibe  

---
