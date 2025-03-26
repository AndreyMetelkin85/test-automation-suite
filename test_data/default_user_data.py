from dataclasses import dataclass
from typing import List, Optional


@dataclass
class User:
    id: Optional[int] = None
    username: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    phone: Optional[int] = None
    userStatus: Optional[int] = None


@dataclass
class Category:
    id: Optional[int] = None
    name: Optional[str] = None


@dataclass
class Tags:
    id: Optional[int] = None
    name: Optional[str] = None


@dataclass
class PetData:
    id: Optional[int] = None
    name: Optional[str] = None
    photoUrls: List[str] = None


@dataclass
class OrderData:
    id: Optional[int] = None
    quantity: Optional[int] = None
    shipDate: Optional[str] = None


@dataclass
class TextBoxFormData:
    fullname: Optional[str] = None
    email: Optional[str] = None
    current_address: Optional[str] = None
    permanent_address: Optional[str] = None


@dataclass
class RegistrationFormData:
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    age: Optional[int] = None
    salary: Optional[int] = None
    department: Optional[str] = None


@dataclass
class StudentRegistrationData:
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    mobile_number: Optional[int] = None
    current_address: Optional[str] = None
