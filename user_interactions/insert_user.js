var mysql = require('mysql');

var con = mysql.createConnection({
    host: "localhost",
    user: "Aiden",
    password: "Freemann098%%",
    database: "cloud_storage"
});

function createUser(userdata) {
    var user = userdata;
    var userObj = JSON.parse(user);

    return userObj
}

const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
  })
  
  readline.question(`What's your user JSON?`, (userdata) => {
    // console.log(`Hi ${userdata}!`)
    var user = createUser(userdata);
    var username = user.username;
    var password = user.password;

    con.connect(function(err) {
        if (err) throw err;
        console.log("Connected!");
        var sql = "INSERT INTO users (username, password) VALUES (" + username + ", " + password + ")";
        con.query(sql, function (err, result) {
          if (err) throw err;
          console.log("1 record inserted");
        });
      });
    readline.close()
  })

// con.connect(function(err) {
//   if (err) throw err;
//   console.log("Connected!");
//   var sql = "INSERT INTO customers (name, address) VALUES ('Company Inc', 'Highway 37')";
//   con.query(sql, function (err, result) {
//     if (err) throw err;
//     console.log("1 record inserted");
//   });
// });