from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QListWidget, 
    QListWidgetItem, QLabel, QLineEdit, QPushButton, QMessageBox,
    QDialog, QFormLayout
)
from PyQt6.QtCore import Qt

from app.api.adapters.genres_data_adapter import GenresDataAdapter


# =========================================================
# فرم افزودن ژانر (داخل همین فایل)
# =========================================================
class AddGenreDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Add Genre")
        self.setFixedSize(400, 200)
        self.setModal(True)

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(12)

        form_layout = QFormLayout()
        form_layout.setSpacing(10)

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter genre name (e.g. Fiction, Mystery)")
        form_layout.addRow("Name:", self.name_input)

        self.description_input = QLineEdit()
        self.description_input.setPlaceholderText("Enter description (optional)")
        form_layout.addRow("Description:", self.description_input)

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
        self.save_btn.clicked.connect(self.save_genre)

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

    def save_genre(self):
        name = self.name_input.text().strip()
        description = self.description_input.text().strip()

        if not name:
            QMessageBox.warning(self, "Error", "Name is required!")
            return

        # ===== ذخیره‌سازی واقعی =====
        try:
            GenresDataAdapter.add(
                name=name,
                description=description
            )
            QMessageBox.information(self, "Success", "Genre saved successfully!")
            self.accept()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Save failed: {str(e)}")


# =========================================================
# ویجت لیست ژانرها
# =========================================================
class GenresListWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.genres = []

        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(6)

        self.title_label = QLabel("GENRES")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.title_label)

        search_layout = QHBoxLayout()
        search_layout.setSpacing(4)

        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("Search genres...")
        self.search_box.textChanged.connect(self.filter_list)

        self.add_button = QPushButton("+")
        self.add_button.setFixedWidth(40)
        self.add_button.setObjectName("addButton")
        self.add_button.clicked.connect(self.add_new_genre)

        search_layout.addWidget(self.search_box)
        search_layout.addWidget(self.add_button)
        layout.addLayout(search_layout)

        self.list_widget = QListWidget()
        self.list_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.list_widget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        layout.addWidget(self.list_widget)

        self.load_genres_data()

    def load_genres_data(self):
        self.list_widget.clear()

        try:
            self.genres = GenresDataAdapter.get_all()

            if not self.genres:
                self.list_widget.addItem("No genres found")
                return

            for genre in self.genres:
                item = QListWidgetItem(genre.name)
                item.setData(Qt.ItemDataRole.UserRole, genre.id)
                self.list_widget.addItem(item)

        except Exception as e:
            self.list_widget.addItem(f"Error: {str(e)}")

    def filter_list(self, text):
        self.list_widget.clear()
        text = text.lower()

        for genre in self.genres:
            if genre.name.lower().startswith(text):
                item = QListWidgetItem(genre.name)
                item.setData(Qt.ItemDataRole.UserRole, genre.id)
                self.list_widget.addItem(item)

    def add_new_genre(self):
        dialog = AddGenreDialog(self)
        if dialog.exec():
            self.load_genres_data()
            self.search_box.clear()

    def delete_selected_genre(self):
        current_item = self.list_widget.currentItem()
        if not current_item:
            QMessageBox.warning(self, "Warning", "Please select a genre to delete.")
            return

        genre_id = current_item.data(Qt.ItemDataRole.UserRole)
        if not genre_id:
            return

        reply = QMessageBox.question(
            self,
            "Delete Genre",
            "Are you sure you want to delete this genre?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            try:
                success = GenresDataAdapter.delete(genre_id)
                if success:
                    self.load_genres_data()
                    self.search_box.clear()
                else:
                    QMessageBox.warning(
                        self,
                        "Error",
                        "Cannot delete this genre. It may be referenced elsewhere."
                    )
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Delete failed: {str(e)}")