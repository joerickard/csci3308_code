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
  var sql = "SELECT * FROM users";
  con.query(sql, function (err, result) {
    if (err) throw err;
    console.log("1 record inserted");
  });
});