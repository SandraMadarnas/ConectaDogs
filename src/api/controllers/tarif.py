from api.models import db, Tariffs
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

def create_tariff(body):

    try:

        # claves_tariff = body.keys()
        # if not "price" in claves_tariff:
        #     return {"code": 400, "msg": "No one tariff to register"}

        services = body["services"]

        sub_token = get_jwt_identity()

        user_id = sub_token["id"]

        for service in services:
            service_active = service["serviceActive"]
            service_id = service["serviceId"]
            price = service["price"]

            query = db.select(Tariffs).filter_by(user_id=user_id, service_id=service_id)
            tarif = db.session.execute(query).scalars().first()         # first()

            if service_active and tarif:
                tarif.price = price
                db.session.commit()
                continue

            if service_active and not tarif:
                new_tarif = Tariffs(
                    price = price,
                    user_id = user_id,
                    service_id = service_id,
                    )

                db.session.add(new_tarif)                
                db.session.commit()
                continue

            if not service_active and tarif:
                db.session.delete(tarif)
                db.session.commit()
                continue

            if not service_active and not tarif:
                continue


        return {"code": 200, "msg": "All ok"}

    except Exception as error:
        print(error)
        return {"code": 500, "msg": "Error in server, something was wrong"}


def get_tariffs():

    try:
    
        # Obtener registros de la base de datos
        query = db.select(Tariffs).order_by(Tariffs.id)
        tariffs = db.session.execute(query).scalars()
        

        tariff_list = [tariff.serialize() for tariff in tariffs]

        return {"code": 200, "msg": "All ok", "tariffs": tariff_list}

    except Exception as error:
        print(error)
        return {"code": 500, "msg": "Error in server, something was wrong"}
        

def get_tariff(id):

    try:
    
        # Obtener registro de la base de datos
        tariff = db.get_or_404(Tariffs, id)
        # tariff = db.session.execute(db.select(Tariff).filter_by(id)).scalars().one()
        
        return {"code": 200, "msg": "All ok", "tariff": tariff.serialize()}

    except Exception as error:
        print(error)
        return {"code": 500, "msg": "Error in server, something was wrong"}


def update_tariff(body, id):

    try:
    
        # Obtener registro de la base de datos
        tariff = db.get_or_404(Tarifs, id)

        tarif.price = body["price"]


        db.session.commit()

        return {"code": 200, "msg": "tariff update ok", "tariff": tarif.serialize()}

    except Exception as error:
        print(error)
        return {"code": 500, "msg": "Error in server, something was wrong"}


def delete_tariff(id):

    try:
    
        # Obtener registros de la base de datos
        tariff = db.get_or_404(Tariffs, id)

        db.session.delete(tariff)
        db.session.commit()

        # query = db.select(Tariff).order_by(Tariff.id)                 # SI DESPUES SE NECESITA UNA LISTA COMPLETA ACTUALIZADA POR PARTE DEL FRONT
        # tariffs = db.session.execute(query).scalars()

        return {"code": 200, "msg": "Delete tariff ok"}

    except Exception as error:
        print(error)
        return {"code": 500, "msg": "Error in server, something was wrong"}

