from dataclasses import dataclass
from typing import List


@dataclass
class User:
    id: int = None,
    username: str = None,
    firstName: str = None,
    lastName: str = None,
    email: str = None,
    password: str = None,
    phone: int = None,
    userStatus: int = None


@dataclass
class Category:
    id: int = None,
    name: str = None


@dataclass
class Tags:
    id: int = None,
    name: str = None


@dataclass
class PetData:
    category: Category
    id: int = None
    name: str = None,
    photoUrls: List[str] = None,
    tags: List[Tags] = None


@dataclass
class OrderData:
    id: int = None,
    quantity: int = None,
    shipDate: int = None


@dataclass
class TextBoxFormData:
    fullname: str = None,
    email: str = None,
    current_address: str = None,
    permanent_address: str = None


@dataclass
class RegistrationFormData:
    first_name: str = None,
    last_name: str = None,
    email: str = None,
    age: int = None,
    salary: int = None,
    department: str = None


@dataclass
class StudentRegistrationData:
    first_name: str = None,
    last_name: str = None,
    email: str = None,
    mobile_number: int = None,
    current_address: str = None
