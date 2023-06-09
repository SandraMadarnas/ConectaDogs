import React from "react";
import { Link } from "react-router-dom";

const ExpiredCard = () => {
  return (
    <>
      <div className="card card-reserves my-3 mx-auto">
          <div className="row">
            <div className="col-12 col-md-6 py-2">
              <img
                src="https://cdn.pixabay.com/photo/2019/02/06/15/18/puppy-3979350_960_720.jpg"
                className="img-fluid rounded-start"
                alt=""
              />
              <p className="card-text">
                <small className="text-muted">Día de la reserva: 02-05-2023</small>
              </p>
            </div>
            <div className="col-12 col-md-6">
              <div className="card-body">
                <h4 className="card-title p-2 text-primary">
                  <i className="fa-solid fa-dog"></i> Pelusa
                </h4>
                <p>
                  <i className="fas fa-sun fa-xl"></i> Guardería de día
                </p>
                <p>
                  <i className="fas fa-user fa-xl"></i> Dueño: Luis
                </p>
                <p>
                  <i className="fas fa-money-check-alt fa-xl"></i> Monto pagado: 20<i className="fas fa-euro-sign"></i>
                </p>
              </div>
            </div>
          </div>
      </div>
    </>
  );
};

export default ExpiredCard;
