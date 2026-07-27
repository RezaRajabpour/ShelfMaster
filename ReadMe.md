# 📚 LibManager

> A simple yet powerful library management desktop app built with PyQt6.  
> It's got a modern look, dark/light mode, and handles all the boring stuff like books, authors, publishers, and more — so you don't have to.

---

## 📸 Screenshots

> **Main Window – Dark Theme**  
> ![Main Window Dark](https://private-user-images.githubusercontent.com/165255733/627113663-b0980f1b-d7e8-4bf2-be0b-d88f5fb14bf7.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODUxNTIzMzYsIm5iZiI6MTc4NTE1MjAzNiwicGF0aCI6Ii8xNjUyNTU3MzMvNjI3MTEzNjYzLWIwOTgwZjFiLWQ3ZTgtNGJmMi1iZTBiLWQ4OGY1ZmIxNGJmNy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNzI3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDcyN1QxMTMzNTZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT03MmFkNThkMWExNGNjM2ZiNWMzMDFhMTY5YjY5NGY3YmVlMGZiYTk0NzQwZmQwMjc5NDM4M2ZhMzk3ZjMxNjlkJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.wagnA62D_CN6Vb6MfDmczMMArWusGyW3yzvnFDZj5ck)

> **Main Window – Light Theme**  
> ![Main Window Light](https://private-user-images.githubusercontent.com/165255733/627113494-5f2a75bd-4468-4f83-af68-a361c9639165.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODUxNTIzMzYsIm5iZiI6MTc4NTE1MjAzNiwicGF0aCI6Ii8xNjUyNTU3MzMvNjI3MTEzNDk0LTVmMmE3NWJkLTQ0NjgtNGY4My1hZjY4LWEzNjFjOTYzOTE2NS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNzI3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDcyN1QxMTMzNTZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1hODZmODI0NDc5NWJlYTBlOThlZDgxOWQxMmQ5NGU1Mjc0YWRjYmI0ZmY4OThmZmNlMGQxYjEwOGE5MDY0MzgxJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.nMSHVcLrecRq38GFun4h06-C__jdmejyT0w1Stf7h5I)

> **Add translator Dialog**  
> ![Add translator Dialog](https://private-user-images.githubusercontent.com/165255733/627113615-66cf9872-723f-4db3-a151-c72ed2a717c9.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODUxNTIzMzYsIm5iZiI6MTc4NTE1MjAzNiwicGF0aCI6Ii8xNjUyNTU3MzMvNjI3MTEzNjE1LTY2Y2Y5ODcyLTcyM2YtNGRiMy1hMTUxLWM3MmVkMmE3MTdjOS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNzI3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDcyN1QxMTMzNTZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0wMjVmZDg5YzkyODYxMjQxYjQ2ZmE0YjNkNTdiZGUyNTM5YzVlY2Y5MTAwNTJmZmQ2OWMyMjU1YzJkNDllOTk4JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.KXxVVj2ayBlGmsRY1f-e-JlUFJo6dIPCePFFPe7mT9k)

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
