from .users import UsersNamespace
from .info import InfoNamespace
from .auth import AuthNamespace
from .data_for_auth import DataForAuthNamespace
from .categories import CategoriesNamespace
from .images import ImagesNamespace
from .products import ProductsNamespace
from .cities import CitiesNamespace
from .menu import MenuNamespace
from .slider import SliderItemsNamespace
from .orders import OrdersNamespace
from .promo_codes import PromoCodesNamespace
from .answers import AnswersNamespace
from .main_page import MainPageNamespace
from .callbacks import CallbacksNamespace
from .full_text_search import FullTextSearchNamespace
from .occasions import OccasionsNamespace
from .subscribe import SubscribesNamespace
from .bills import BillsNamespace
from .seo import SEONamespace


NAMESPACES = {
    "users": UsersNamespace,
    "info": InfoNamespace,
    "auth": AuthNamespace,
    "data_for_auth": DataForAuthNamespace,
    "categories": CategoriesNamespace,
    "images": ImagesNamespace,
    "products": ProductsNamespace,
    "cities": CitiesNamespace,
    "menu": MenuNamespace,
    "slider_items": SliderItemsNamespace,
    "orders": OrdersNamespace,
    "promos": PromoCodesNamespace,
    "answers": AnswersNamespace,
    "main_page": MainPageNamespace,
    "callbacks": CallbacksNamespace,
    "full_text_search": FullTextSearchNamespace,
    "occasions": OccasionsNamespace,
    "subscribes": SubscribesNamespace,
    "bills": BillsNamespace,
    "seo": SEONamespace,
}
