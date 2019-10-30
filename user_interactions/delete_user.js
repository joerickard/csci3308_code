// Delete user string format
// '{"username": "joerick69", "password": "123456"}'


// connect to local mysql database
var mysql = require('mysql');
var con = mysql.createConnection({
    host: "localhost",
    user: "drive",
    password: "Freemann098%%",
    database: "cloud_storage"
});

// Parse JSON string for user data
function createUser(userdata) {
    var user = userdata;
    var userObj = JSON.parse(user);

    return userObj
}

// take user input from command line
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
  })

  // prompt
  readline.question(`What's your user JSON to delete?`, (userdata) => {

    // separate user data
    var user = createUser(userdata);
    var username = user.username;
    var password = user.password;

    // connect to server
    con.connect(function(err) {
        if (err) throw err;
        console.log("Connected!");

        // delete user
        var sql = "DELETE FROM users WHERE username = '" + username + "' AND password = '" + password + "'";


        con.query(sql, function (err, result) {
          if (err) throw err;
          console.log("1 record deleted");
        });
      });
    readline.close()
  })
