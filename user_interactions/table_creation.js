// This script really is not necessary for more than one use

var mysql = require('mysql');

var con = mysql.createConnection({
  host: "localhost",
  user: "drive",
  password: "Freemann098%%",
  database: "cloud_storage",
});

con.connect(function(err) {
  if (err) throw err;
  console.log("Connected!");
  var sql = "CREATE TABLE users (username VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL)";
  con.query(sql, function (err, result) {
    if (err) throw err;
    console.log("User table created");
  });
});