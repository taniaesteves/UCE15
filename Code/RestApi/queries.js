'use strict'
var promise = require('bluebird');
const fs = require('fs');

var options = {
  // Initialization Options
  promiseLib: promise
};

var pgp = require('pg-promise')(options);
var connectionString = 'postgres://localhost:5432/atlas';
var db = pgp(connectionString);

// add query functions
// curl --data "featureid=2&latitude=41.560404&longitude=-8.4056225&imagepath=https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/figures/b2_2017-11-25_20-38-25.PNG?raw=true&timestamp=2017-11-25 20:38:25&precision=89" http://localhost:3000/api/createMarker



function createMarker(req, res, next) {
  let data = req.body.image;
  let buff = new Buffer(data, 'base64');
  req.body.featureid = parseInt(req.body.featureid);
  req.body.latitude = parseFloat(req.body.latitude);
  req.body.longitude = parseFloat(req.body.longitude);
  req.body.precision = parseFloat(req.body.precision);
  
  var imageName = req.body.featureid +'_'+req.body.latitude +'_'+req.body.longitude+'_'+req.body.timestamp+'.PNG';
  var filesave = '../Model/Catalogs/sinais_de_transito/figures/' + imageName;
  filesave = filesave.replace(/ /g, "_");
  filesave = filesave.replace(/:/g, "-");
  //console.log(filesave);
  fs.writeFileSync(filesave, buff);
  // fs.writeFile(filesave, buff, 'base64', function(err) {
  // 	console.log(err);
  // });
  //fs.writeFileSync("../Model/Catalogs/sinais_de_transito/figures/" + imageName, buff);
  //console.log("Object: %j", req.body);
  req.body.image = 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/figures/'+imageName+'?raw=true'
    db.none('insert into marker(featureid, latitude, longitude, imagepath , timestamp, precision)' +
      'values(${featureid}, ${latitude}, ${longitude}, ${image}, ${timestamp}, ${precision})', req.body)
    .then(function () {
      res.status(200).send('Acceptable');
//        status(200)
//         .json({
//           status: 'success',
//           message: 'Inserted one marker'
//         });
    })
    .catch(function (err) {
      return next(err);
    });
}

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
    createMarker: createMarker,
    getAllMarkers: getAllMarkers
};