var mysql = require('mysql');

var con = mysql.createConnection({
  host: "localhost",
  user: "Aiden",
  password: "Freemann098%%",
  database: "cloud_storage"
});

con.connect(function(err) {
  if (err) throw err;
  console.log("Connected!");
  var sql = "CREATE TABLE users (username VARCHAR(255), password VARCHAR(255))";
  con.query(sql, function (err, result) {
    if (err) throw err;
    console.log("User table created");
  });
});