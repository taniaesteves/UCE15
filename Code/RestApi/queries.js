var promise = require('bluebird');

var options = {
  // Initialization Options
  promiseLib: promise
};

var pgp = require('pg-promise')(options);
var connectionString = 'postgres://localhost:5432/atlasdb';
var db = pgp(connectionString);

// add query functions
//function createMarker(req, res, next) {}


function getAllMarkers(req, res, next) {
  db.any('select * from marker')
    .then(function (data) {
      res.status(200)
        .json({
          status: 'success',
          data: data
        });
    })
    .catch(function (err) {
      return next(err);
    });
}

module.exports = {
  getAllMarkers: getAllMarkers
  //createMarker: createMarker
};