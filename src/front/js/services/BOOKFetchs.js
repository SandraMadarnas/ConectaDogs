import { RUTABACK } from "../constants/RutaBack.js";


export const GET_Book = (book_id) => {
    return (fetch(`${RUTABACK}/api/books/${book_id}`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json"
        }
      })
      .then(resp => {
          return resp.json(); // (returns promise) will try to parse the result as json as return a promise that you can .then for results
      })
      .then(data => {
        return data;
      })
      .catch(error => {console.log(error);}));  //Error handling
  };

export const GET_All_Books = () => {
    return (fetch(`${RUTABACK}/api/books`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json"
        }
      })
      .then(resp => {
          return resp.json(); // (returns promise) will try to parse the result as json as return a promise that you can .then for results
      })
      .then(data => {
        return data;
      })
      .catch(error => {console.log(error);}));  //Error handling
};
      
export const UPDATE_Book = (newObj, book_id) => {

    const token = sessionStorage.getItem("jwt-token");

    return (fetch(`${RUTABACK}/api/books/${book_id}`, {
        method: "PUT",
        body: JSON.stringify(newObj),
        headers: {
          "Content-Type": "application/json",
          "Authorization": "Bearer " + token,                 // ⬅⬅⬅ authorization token
        }
    })
    .then(resp => {
        return resp.json(); // (returns promise) will try to parse the result as json as return a promise that you can .then for results
    })
    .then(data => {
        //here is were your code should start after the fetch finishes
        return data;
    })
    .catch(error => {console.log(error);}));  //Error handling
};


export const DELETE_Book = (book_id) => { 

    const token = sessionStorage.getItem("jwt-token");

    return (fetch(`${RUTABACK}/api/books/${book_id}`, {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
          "Authorization": "Bearer " + token,                 // ⬅⬅⬅ authorization token
      }
      })
      .then(resp => {
          return resp.json(); // (returns promise) will try to parse the result as json as return a promise that you can .then for results
      })
      .then(data => {
          //here is were your code should start after the fetch finishes
          return data;
        })
      .catch(error => {console.log(error);}));  //Error handling
};


export const GET_Confirm_Book = (book_id) => { 

  const token = sessionStorage.getItem("jwt-token");

  return (fetch(`${RUTABACK}/api/acepted-book/${book_id}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token,                 // ⬅⬅⬅ authorization token
    }
    })
    .then(resp => {
        return resp.json(); // (returns promise) will try to parse the result as json as return a promise that you can .then for results
    })
    .then(data => {
        //here is were your code should start after the fetch finishes
        return data;
      })
    .catch(error => {console.log(error);}));  //Error handling
};


export const GET_Deny_Book = (book_id) => { 

  const token = sessionStorage.getItem("jwt-token");

  return (fetch(`${RUTABACK}/api/rejected-book/${book_id}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token,                 // ⬅⬅⬅ authorization token
    }
    })
    .then(resp => {
        return resp.json(); // (returns promise) will try to parse the result as json as return a promise that you can .then for results
    })
    .then(data => {
        //here is were your code should start after the fetch finishes
        return data;
      })
    .catch(error => {console.log(error);}));  //Error handling
};



export const POST_Book = (nuevaReserva) => {

    const token = sessionStorage.getItem("jwt-token");

    return (fetch(`${RUTABACK}/api/signup-book`, {
        method: "POST",
        body: JSON.stringify(nuevaReserva),
        headers: {
          "Content-Type": "application/json",
          "Authorization": "Bearer " + token,
        }
      })
      .then((resp) => {
        return resp.json(); //(returns promise) will try to parse the result as json as return a promise that you can .then for results
      })
      .then((data) => {
        //here is were your code should start after the fetch finishes
        return data;
      })
      .catch(error => {console.log(error);}));  //Error handling
};
