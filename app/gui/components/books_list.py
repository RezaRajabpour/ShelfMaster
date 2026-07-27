from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QListWidget, 
    QListWidgetItem, QLabel, QLineEdit, QPushButton, QMessageBox,
    QDialog, QFormLayout, QDateEdit, QComboBox
)
from PyQt6.QtCore import Qt

from app.api.adapters.books_data_adapter import BooksDataAdapter


# =========================================================
# فرم افزودن کتاب (داخل همین فایل)
# =========================================================
class AddBookDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Add New Book")
        self.setFixedSize(450, 400)
        self.setModal(True)

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(12)

        form_layout = QFormLayout()
        form_layout.setSpacing(10)

        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("Enter book title")
        form_layout.addRow("Title:", self.title_input)

        self.author_input = QLineEdit()
        self.author_input.setPlaceholderText("Enter author name")
        form_layout.addRow("Author:", self.author_input)

        self.isbn_input = QLineEdit()
        self.isbn_input.setPlaceholderText("Enter ISBN")
        form_layout.addRow("ISBN:", self.isbn_input)

        self.year_input = QDateEdit()
        self.year_input.setCalendarPopup(True)
        self.year_input.setDate(self.year_input.date().currentDate())
        form_layout.addRow("Publication Year:", self.year_input)

        self.publisher_input = QLineEdit()
        self.publisher_input.setPlaceholderText("Enter publisher")
        form_layout.addRow("Publisher:", self.publisher_input)

        layout.addLayout(form_layout)

        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)

        self.save_btn = QPushButton("Save")
        self.save_btn.setFixedHeight(35)
        self.save_btn.setStyleSheet("""
            QPushButton {
                background-color: #107C41;
                color: white;
                border: none;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #0B5931;
            }
        """)
        self.save_btn.clicked.connect(self.save_book)

        self.close_btn = QPushButton("Close")
        self.close_btn.setFixedHeight(35)
        self.close_btn.setStyleSheet("""
            QPushButton {
                background-color: #dc3545;
                color: white;
                border: none;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #c82333;
            }
        """)
        self.close_btn.clicked.connect(self.reject)

        button_layout.addStretch()
        button_layout.addWidget(self.save_btn)
        button_layout.addWidget(self.close_btn)

        layout.addLayout(button_layout)

    def save_book(self):
        title = self.title_input.text().strip()
        author = self.author_input.text().strip()
        isbn = self.isbn_input.text().strip()
        year = self.year_input.date().toString("yyyy")
        publisher = self.publisher_input.text().strip()

        if not title or not author:
            QMessageBox.warning(self, "Error", "Title and Author are required!")
            return

        # ===== ذخیره‌سازی واقعی =====
        try:
            BooksDataAdapter.add(
                title=title,
                author=author,
                isbn=isbn,
                year=year,
                publisher=publisher
            )
            QMessageBox.information(self, "Success", "Book saved successfully!")
            self.accept()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Save failed: {str(e)}")


# =========================================================
# ویجت لیست کتاب‌ها
# =========================================================
class BooksListWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.items = []

        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(6)

        self.title_label = QLabel("BOOKS")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.title_label)

        search_layout = QHBoxLayout()
        search_layout.setSpacing(4)

        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("Search books...")
        self.search_box.textChanged.connect(self.filter_list)

        self.add_button = QPushButton("+")
        self.add_button.setFixedWidth(40)
        self.add_button.setObjectName("addButton")
        self.add_button.clicked.connect(self.add_new_item)

        search_layout.addWidget(self.search_box)
        search_layout.addWidget(self.add_button)
        layout.addLayout(search_layout)

        self.list_widget = QListWidget()
        self.list_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.list_widget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        layout.addWidget(self.list_widget)

        self.load_data()

    def load_data(self):
        self.list_widget.clear()
        try:
            self.items = BooksDataAdapter.get_all()
            if not self.items:
                self.list_widget.addItem("No items found")
                return
            for item in self.items:
                display_text = item.name  # یا item.title
                list_item = QListWidgetItem(display_text)
                list_item.setData(Qt.ItemDataRole.UserRole, item.id)
                self.list_widget.addItem(list_item)
        except Exception as e:
            self.list_widget.addItem(f"Error: {str(e)}")

    def filter_list(self, text):
        self.list_widget.clear()
        text = text.lower()
        for item in self.items:
            display_text = item.name
            if display_text.lower().startswith(text):
                list_item = QListWidgetItem(display_text)
                list_item.setData(Qt.ItemDataRole.UserRole, item.id)
                self.list_widget.addItem(list_item)

    def add_new_item(self):
        dialog = AddBookDialog(self)
        if dialog.exec():
            self.load_data()
            self.search_box.clear()

    def delete_selected_item(self):
        current_item = self.list_widget.currentItem()
        if not current_item:
            QMessageBox.warning(self, "Warning", "Please select an item to delete.")
            return
        item_id = current_item.data(Qt.ItemDataRole.UserRole)
        if not item_id:
            return
        reply = QMessageBox.question(
            self, "Delete Item", "Are you sure?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if reply == QMessageBox.StandardButton.Yes:
            try:
                success = BooksDataAdapter.delete(item_id)
                if success:
                    self.load_data()
                    self.search_box.clear()
                else:
                    QMessageBox.warning(self, "Error", "Cannot delete, referenced elsewhere.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Delete failed: {str(e)}")