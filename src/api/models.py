from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import ForeignKey
# from sqlalchemy.orm import relationship

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), unique=False, nullable=False)
    name = db.Column(db.String(30), unique=False, nullable=False)
    lastName = db.Column(db.String(60), unique=False, nullable=False)
    address = db.Column(db.String(150), unique=False, nullable=False)
    province = db.Column(db.String(35), unique=False, nullable=False)
    postalCode = db.Column(db.Integer, unique=False, nullable=False)
    phone = db.Column(db.Integer, unique=False, nullable=False)
    country = db.Column(db.String(50), unique=False, nullable=False)
    aboutMe = db.Column(db.String(300), unique=False, nullable=True)
    birthdate = db.Column(db.String(20), unique=False, nullable=False)
    is_active = db.Column(db.Boolean, unique=False, nullable=False)
    photo = db.Column(db.String(500), unique=True, nullable=True)     # USAR API CLOUDINARY, HACER LLAMADA Y GUARDARSE LA URL DEVUELTA QUE ES LO QUE SE SUBE A LA BASE DE DATOS
    # latitude = db.Column(db.String(40), unique=False, nullable=False)
    # longitude = db.Column(db.String(40), unique=False, nullable=False)

    dogs = db.relationship("Dog", back_populates="user")

    tariffs = db.relationship("Tariffs", back_populates="user")


    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "lastName": self.lastName,
            "address": self.address,
            "province": self.province,
            "postalCode": self.postalCode,
            "phone": self.phone,
            "country": self.country,
            "birthdate": self.birthdate,
            "aboutMe": self.aboutMe,
            "photo": self.photo,
            # "latitude": self.latitude,
            # "longitude": self.longitude,
            "dogs": [dog.serialize() for dog in self.dogs],
            "tariffs": [tariff.serialize() for tariff in self.tariffs],
        # ¡¡¡¡DO NOT serialize the password, its a security breach!!!
        }


class Dog(db.Model):
    __tablename__ = "Dog"
    id = db.Column(db.Integer, primary_key=True)
    dogName = db.Column(db.String(35), unique=False, nullable=False)
    breed = db.Column(db.String(50), unique=False, nullable=False)
    dogBirth = db.Column(db.String(20), unique=False, nullable=False)
    dogSex = db.Column(db.String(20), unique=False, nullable=False)
    dogSize = db.Column(db.String(20), unique=False, nullable=True)
    neutered = db.Column(db.Boolean, unique=False, nullable=False)
    socialCats = db.Column(db.Boolean, unique=False, nullable=False)
    socialKids = db.Column(db.Boolean, unique=False, nullable=False)
    socialDogs = db.Column(db.Boolean, unique=False, nullable=False)
    microchip = db.Column(db.BigInteger, unique=True, nullable=False)
    dogActivity = db.Column(db.String(20), unique=False, nullable=True)
    observations = db.Column(db.String(500), unique=False, nullable=True)
    photo = db.Column(db.String(500), unique=True, nullable=True)         # USAR API CLOUDINARY, HACER LLAMADA Y GUARDARSE LA URL DEVUELTA QUE ES LO QUE SE SUBE A LA BASE DE DATOS

    user_id = db.Column(db.Integer, db.ForeignKey("User.id"))

    user = db.relationship("User", back_populates="dogs")


    def __repr__(self):
        return f'<Dog {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "dogName": self.dogName,
            "breed": self.breed,
            "dogBirth": self.dogBirth,
            "dogSex": self.dogSex,
            "dogSize": self.dogSize,    
            "neutered": self.neutered,
            "socialCats": self.socialCats,
            "socialKids": self.socialKids,
            "socialDogs": self.socialDogs,
            "microchip": self.microchip,
            "dogActivity": self.dogActivity,
            "observations": self.observations,
            "photo": self.photo,
            "user_id": self.user_id,
        }


class Services(db.Model):
    __tablename__ = "Services"                                # id = 1 PARA nurseryDay // Alojamiento        id = 2 PARA walk // Paseo       id = 3 PARA nurseryNight // Guardería de Día
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(350), unique=True, nullable=False)
    title = db.Column(db.String(35), unique=True, nullable=False)
    description = db.Column(db.String(500), unique=True, nullable=False)

    tariff = db.relationship("Tariffs", back_populates="service")

    def __repr__(self):
        return f'<Services {self.title}>'

    def serialize(self):
        return {
            "id": self.id,
            "image": self.image,
            "title": self.title,
            "description": self.description,
        }


class Tariffs(db.Model):
    __tablename__ = "Tariffs"
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, unique=False, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("User.id"))
    service_id = db.Column(db.Integer, db.ForeignKey("Services.id"))

    service = db.relationship("Services", back_populates="tariff")
    user = db.relationship("User", back_populates="tariffs")
    book = db.relationship("Books", back_populates="tariff")


    def __repr__(self):
        return f'<Tariffs {self.price}>'

    def serialize(self):
        return {
            "id": self.id,
            "price": self.price,
            "service": self.service.serialize(),
        }


class Books(db.Model):
    __tablename__ = "Books"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, unique=False, nullable=False)
    hourPick = db.Column(db.String, unique=False, nullable=False)
    hourDeliver = db.Column(db.String, unique=False, nullable=False)
    dogsAcepted = db.Column(db.Integer, unique=False, nullable=False)
    dogIdAcepted = db.Column(db.Integer, unique=False, nullable=False)
    acepted = db.Column(db.Boolean, unique=False, nullable=False, default=False)

    user_from_id = db.Column(db.Integer, db.ForeignKey("User.id"))
    tarif_id = db.Column(db.Integer, db.ForeignKey("Tariffs.id"))

    tariff = db.relationship("Tariffs", back_populates="book")


    def __repr__(self):
        return f'<Book {self.date}>'

    def serialize(self):
        return {
            "id": self.id,
            "date": self.date,
            "hourPick": self.hourPick,
            "hourDeliver": self.hourDeliver,
            "dogsAcepted": self.dogsAcepted,
            "dogIdAcepted": self.dogIdAcepted,
            "user_from_id": self.user_from_id,
            "tarif_id": self.tarif_id,
            "acepted": self.acepted,
            "tariff": self.tariff.serialize(),
        }








#     daily_food_rations = db.Column(db.String, unique=False, nullable=False)
#     meal_times = db.Column(db.String, unique=False, nullable=False)
#     schedule_walks = db.Column(db.String, unique=False, nullable=False)
#     caretaker_comments = db.Column(db.String, unique=False, nullable=False)
