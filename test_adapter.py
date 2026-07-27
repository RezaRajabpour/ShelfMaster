import sys
sys.path.insert(0, r"C:\Users\Asus\Desktop\library")

from app.api.adapters.authors_data_adapter import AuthorsDataAdapter
from app.api.adapters.books_data_adapter import BooksDataAdapter
from app.api.adapters.esrbs_data_adapter import EsrbsDataAdapter
from app.api.adapters.genres_data_adapter import GenresDataAdapter
from app.api.adapters.languages_data_adapter import LanguagesDataAdapter
from app.api.adapters.publishers_data_adapter import PublishersDataAdapter
from app.api.adapters.resources_data_adapter import ResourcesDataAdapter
from app.api.adapters.translators_data_adapter import TranslatorsDataAdapter

adapters = [
    ("Authors", AuthorsDataAdapter),
    ("Books", BooksDataAdapter),
    ("ESRB", EsrbsDataAdapter),
    ("Genres", GenresDataAdapter),
    ("Languages", LanguagesDataAdapter),
    ("Publishers", PublishersDataAdapter),
    ("Resources", ResourcesDataAdapter),
    ("Translators", TranslatorsDataAdapter),
]

for name, adapter in adapters:
    print(f"\n=== {name} ===")
    methods = [m for m in dir(adapter) if not m.startswith('_')]
    print("Methods:", methods)
    
    # دنبال متدهای ذخیره‌سازی
    save_methods = [m for m in methods if m in ['create', 'add', 'save', 'insert', 'add_record', 'new']]
    if save_methods:
        print(f"Save methods found: {save_methods}")
    else:
        print("No save method found!")