// Global Variables
var loadeddata;
var rack_hit = "rack1";
var section_hit = "section1";
var captcha;
function generate() {

	// Clear old input
	document.getElementById("submit").value = "";

	// Access the element to store
	// the generated captcha
	captcha = document.getElementById("image");
	var uniquechar = "";

	const randomchar =
"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

	// Generate captcha for length of
	// 5 with random character
	for (let i = 1; i < 5; i++) {
		uniquechar += randomchar.charAt(
			Math.random() * randomchar.length)
	}

	// Store generated input
	captcha.innerHTML = uniquechar;
}

function printmsg() {
	const usr_input = document
		.getElementById("submit").value;
	
	// Check whether the input is equal
	// to generated captcha or not
	if (usr_input == captcha.innerHTML) {
		// var s = document.getElementById("key")
		// 	.innerHTML = "Matched";
		// generate();
    return true;
	}
	else {
		// var s = document.getElementById("key")
		// 	.innerHTML = "not Matched";
		// generate();
    return false;
	}
}

function rack_dis() {
  // Referencing to table based on rack number and section number
  var messagesRef = firebase
    .database()
    .ref("seconddata/" + rack_hit + "/" + section_hit);
  messagesRef.on(
    "value",
    function (snapshot) {
      // Total filtered data will be stored in loadeddata variable
      loadeddata = snapshot.val();

      // Creating multiple cards based loadeddata
      let tab1 = "";
      for (let r in loadeddata) {
        tab1 += `<div class="card" style="width: 18rem;">
            <img class="card-img-top" height="161px" width="286px" src="${loadeddata[r].ImageUrl}" alt="Card image cap">
        <div class="card-body">
          <h5 class="card-title">${loadeddata[r].Name}</h5>
          <p class="card-text">${loadeddata[r].Description}</p>
          <button onclick="seemore('${r}')" class="btn btn-primary">See More</button>
          </div>
        </div>`;
      }
      // Displaying in html in paragraph tag with ID "dispay-data"
      document.getElementById("dispay-data").innerHTML = tab1;
    },
    function (error) {
      
      if (error.code=="PERMISSION_DENIED"){
        alert(error.code+"\n Please Login or Signup!!");
        location.href="index.html";
      }
      
      else{
        alert(error.code);
      }
    }
  );
}
// See more function to Alert card data
function seemore(val) {
  let alert_val = "";
  alert_val =
    "Name : " +
    loadeddata[val].Name +
    "<br />" +
    "Brand : " +
    loadeddata[val].Brand +
    "<br />" +
    "Rating : " +
    loadeddata[val].Rating +
    "<br />" +
    "Price : " +
    loadeddata[val].Price +
    "<br />" +
    "Height : " +
    loadeddata[val].Height +
    "<br />" +
    "Width : " +
    loadeddata[val].Width +
    "<br />" +
    "Rack Number : " +
    loadeddata[val].Rack +
    "<br />" +
    "Section : " +
    loadeddata[val].Section +
    "<br />" +
    "Status : " +
    loadeddata[val].Status +
    "<br />" +
    "Color : " +
    loadeddata[val].Color +
    "<br />" +
    "Description : " +
    loadeddata[val].Description +
    "<br />";
  //  alert(alert_val);
  $(document).ready(function () {
    // document.getElementById("#exampleModal").innerHTML = alert_val;
    $("h5").html(loadeddata[val].Name);
    $("h6").html(alert_val);
    $("#exampleModal").modal("show");
  });
}

// Rack navigating/changing
function rack_change(val) {
  rack_hit = val;
  rack_dis();
}

// Section navigating/changing
function sec_change(val) {
  section_hit = val;
  rack_dis();
}

function createuser() {
  // var email = "Mali@email.com";
  // var password = "password";
  // var con_password=password;

  var email = document.getElementById("signup_email").value;
  var password = document.getElementById("signup_pass").value;
  var con_password = document.getElementById("signup_conpass").value;

  alert("Email: " + email + "\n" + "Password : " + password);

  if (password === con_password) {
    firebase
      .auth()
      .createUserWithEmailAndPassword(email, password)
      .then((userCredential) => {
        alert("created");
        location.href = "home.html";

      })
      .catch(function (error) {
        console.log(error.code);
        console.log(error.message);
      });
  } else {
    alert(
      password +
        con_password +
        "Password and Confirm password is not matching!!!!"
    );
  }
}

function signin() {
  var email = "myemail@email.com";
  var password = "mypassword";

  // var email = document.getElementById("signin_email").value;
  // var password = document.getElementById("signin_pass").value;

  // console.log("Email: "+email+"\n"+"Password : "+password);
if (printmsg()){
  // alert(printmsg)
  firebase
    .auth()
    .signInWithEmailAndPassword(email, password)
    .then((userCredential) => {
      alert("Welcome!!!!");
      // location.reload();
      location.href = "home.html";
    })
    .catch(function (error) {
      console.log(error.code);
      console.log(error.message);
    });
}
else{
  alert("Wrong Captcha!!!");
};
  
  // location.reload();
}

function logout() {
  firebase
    .auth()
    .signOut()
    .then(
      function () {
        alert("Logged out!");
        location.href = "index.html";
      },
      function (error) {
        console.log(error.code);
        console.log(error.message);
      }
    );
}
