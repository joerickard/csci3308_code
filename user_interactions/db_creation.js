// This script really is not necessary for more than one use

var mysql = require('mysql');

var con = mysql.createConnection({
    host: "localhost",
    user: "drive",
    password: "Freemann098%%"
  });

con.connect(function(err) {
    if (err) throw err;
    console.log("Connected!");
    con.query("CREATE DATABASE cloud_storage", function (err, result) {
      if (err) throw err;
      console.log("Database created");
    });
});