from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QListWidget, 
    QListWidgetItem, QLabel, QLineEdit, QPushButton, QMessageBox,
    QDialog, QFormLayout, QDateEdit, QComboBox
)
from PyQt6.QtCore import Qt

from app.api.adapters.authors_data_adapter import AuthorsDataAdapter


# =========================================================
# فرم افزودن نویسنده (داخل همین فایل)
# =========================================================
class AddAuthorDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Add New Author")
        self.setFixedSize(400, 350)
        self.setModal(True)

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(12)

        form_layout = QFormLayout()
        form_layout.setSpacing(10)

        self.national_code_input = QLineEdit()
        self.national_code_input.setPlaceholderText("Enter national code")
        form_layout.addRow("National Code:", self.national_code_input)

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter first name")
        form_layout.addRow("Name:", self.name_input)

        self.last_name_input = QLineEdit()
        self.last_name_input.setPlaceholderText("Enter last name")
        form_layout.addRow("Last Name:", self.last_name_input)

        self.birthday_input = QDateEdit()
        self.birthday_input.setCalendarPopup(True)
        self.birthday_input.setDate(self.birthday_input.date().currentDate())
        form_layout.addRow("Birthday:", self.birthday_input)

        self.grade_input = QComboBox()
        self.grade_input.addItems(["A", "B", "C", "D", "E", "F"])
        form_layout.addRow("Grade:", self.grade_input)

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
        self.save_btn.clicked.connect(self.save_author)

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

    def save_author(self):
        national_code = self.national_code_input.text().strip()
        name = self.name_input.text().strip()
        last_name = self.last_name_input.text().strip()
        birthday = self.birthday_input.date().toString("yyyy-MM-dd")
        grade = self.grade_input.currentText()

        if not name or not last_name:
            QMessageBox.warning(self, "Error", "Name and Last Name are required!")
            return

        # ===== ذخیره‌سازی با insert =====
        try:
            AuthorsDataAdapter.insert(
                national_code=national_code,
                name=name,
                last_name=last_name,
                birthday=birthday,
                grade=grade
            )
            QMessageBox.information(self, "Success", "Author saved successfully!")
            self.accept()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Save failed: {str(e)}")


# =========================================================
# ویجت لیست نویسنده‌ها
# =========================================================
class AuthorsListWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.authors = []

        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(6)

        self.title_label = QLabel("AUTHORS")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.title_label)

        search_layout = QHBoxLayout()
        search_layout.setSpacing(4)

        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("Search authors...")
        self.search_box.textChanged.connect(self.filter_list)

        self.add_button = QPushButton("+")
        self.add_button.setFixedWidth(40)
        self.add_button.setObjectName("addButton")
        self.add_button.clicked.connect(self.add_new_author)

        search_layout.addWidget(self.search_box)
        search_layout.addWidget(self.add_button)
        layout.addLayout(search_layout)

        self.list_widget = QListWidget()
        self.list_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.list_widget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        layout.addWidget(self.list_widget)

        self.load_authors_data()

    def load_authors_data(self):
        self.list_widget.clear()

        try:
            self.authors = AuthorsDataAdapter.get_all()

            if not self.authors:
                self.list_widget.addItem("No authors found")
                return

            for author in self.authors:
                item = QListWidgetItem(author.name)
                item.setData(Qt.ItemDataRole.UserRole, author.id)
                self.list_widget.addItem(item)

        except Exception as e:
            self.list_widget.addItem(f"Error: {str(e)}")

    def filter_list(self, text):
        self.list_widget.clear()
        text = text.lower()

        for author in self.authors:
            if author.name.lower().startswith(text):
                item = QListWidgetItem(author.name)
                item.setData(Qt.ItemDataRole.UserRole, author.id)
                self.list_widget.addItem(item)

    def add_new_author(self):
        dialog = AddAuthorDialog(self)
        if dialog.exec():
            self.load_authors_data()
            self.search_box.clear()

    def delete_selected_author(self):
        current_item = self.list_widget.currentItem()
        if not current_item:
            QMessageBox.warning(self, "Warning", "Please select an author to delete.")
            return

        author_id = current_item.data(Qt.ItemDataRole.UserRole)
        if not author_id:
            return

        reply = QMessageBox.question(
            self,
            "Delete Author",
            "Are you sure you want to delete this author?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            try:
                success = AuthorsDataAdapter.delete(author_id)
                if success:
                    self.load_authors_data()
                    self.search_box.clear()
                else:
                    QMessageBox.warning(
                        self,
                        "Error",
                        "Cannot delete this author. It may be referenced elsewhere."
                    )
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Delete failed: {str(e)}")