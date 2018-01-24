'use strict'
var promise = require('bluebird');
var NodeGeocoder = require('node-geocoder');
const fs = require('fs');

var options = {
  // Initialization Options
  promiseLib: promise
};

var options2 = {
  provider: 'google',
  httpAdapter: 'https', // Default
  apiKey: 'AIzaSyBA3lXQUMnKgOvmrdRM_PjEAgFjWRApbPo', // for Mapquest, OpenCage, Google Premier
  formatter: null         // 'gpx', 'string', ...
};

var geocoder = NodeGeocoder(options2);

var pgp = require('pg-promise')(options);
var connectionString = 'postgres://localhost:5432/atlas';
var db = pgp(connectionString);

// add query functions
// curl --data "label=B2&latitude=41.560404&longitude=-8.4056225&imagepath=https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/figures/b2_2017-11-25_20-38-25.PNG?raw=true&timestamp=2017-11-25 20:38:25&precision=0.89" http://localhost:3000/api/createMarker

function multiMarker(req, res, next){
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


function createMarker(req, res, next) {
  let data = req.body.image;
  let buff = new Buffer(data, 'base64');
  var localidade;
  var idfeat;
  geocoder.reverse({lat:req.body.latitude, lon:req.body.longitude}).then(res1 => {
    localidade = res1[0].streetName + ', ' + res1[0].city;
    // console.log(localidade);
    req.body.latitude = parseFloat(req.body.latitude);
    req.body.longitude = parseFloat(req.body.longitude);
    req.body.precision = parseFloat(req.body.precision);


    db.one("select id from feature where code = $1",req.body.label)
    .then(data => {
      var imageName = req.body.label +'_'+req.body.latitude +'_'+req.body.longitude+'_'+req.body.timestamp+'.PNG';
      imageName = imageName.replace(/ /g, "_");
      imageName = imageName.replace(/:/g, "-");
      var filesave = '../Model/Catalogs/sinais_de_transito/figures/' + imageName;
      idfeat = data.id;
      fs.writeFileSync(filesave, buff);
      // console.log(idfeat);
      req.body.label = idfeat;
      req.body.image = 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/figures/'+imageName+'?raw=true';
      db.many('select * from marker where (abs(latitude-($1)) < 0.00005) and (abs(longitude-($2)) < 0.00007) and featureid = $3', 
          [req.body.latitude, req.body.longitude, req.body.label])
          .then(dados => {
            // fazer update ao marker

            // reposta
            console.log("marker ja existe");
            res.status(200).json({
               status: 'success',
               message: 'Inserted one marker'
            });

          })
          .catch(err => {
              console.log("novo marker");
              db.none('insert into marker(featureid, latitude, longitude, imagepath , timestamp, precision, address, ocurr)' +
                'values($1, $2, $3, $4, $5, $6, $7, 1)', 
                [req.body.label, req.body.latitude, req.body.longitude, req.body.image, req.body.timestamp, req.body.precision, localidade])
              .then(function () {            
                res.status(200).json({
                status: 'success',
                message: 'Inserted one marker'
                });
              })
              .catch(function (err) {
                console.log(err);
                return next(err);
              });
          });
      // db.none('insert into marker(featureid, latitude, longitude, imagepath , timestamp, precision, address, ocurr)' +
      //     'values($1, $2, $3, $4, $5, $6, $7, 1)', 
      //     [req.body.label, req.body.latitude, req.body.longitude, req.body.image, req.body.timestamp, req.body.precision, localidade])
      //     .then(function () {
            
      //         res.status(200).json({
      //         status: 'success',
      //         message: 'Inserted one marker'
      //       });
      //     })
      //   .catch(function (err) {
      //       console.log(err);
      //       return next(err);
      //   });
    })
    .catch(error => {
          console.log(error);
          //return next(error);
    });
  })
  .catch(function(err) {
    console.log(err);
  });

  // console.log(localidade);
  // req.body.latitude = parseFloat(req.body.latitude);
  // req.body.longitude = parseFloat(req.body.longitude);
  // req.body.precision = parseFloat(req.body.precision);

  // db.one("select id from feature where code = $1",req.body.label)
  //    .then(data => {
  //      var imageName = req.body.label +'_'+req.body.latitude +'_'+req.body.longitude+'_'+req.body.timestamp+'.PNG';
  //    imageName = imageName.replace(/ /g, "_");
  //    imageName = imageName.replace(/:/g, "-");
  //    var filesave = '../Model/Catalogs/sinais_de_transito/figures/' + imageName;
  //       idfeat = data.id;
  //       // console.log(idfeat);
  //       fs.writeFileSync(filesave, buff);
  //       // successful transaction output;
  //       console.log(idfeat);
  //    req.body.label = idfeat;
  //    req.body.image = 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/figures/'+imageName+'?raw=true'
  //    db.none('insert into marker(featureid, latitude, longitude, imagepath , timestamp, precision)' +
  //        'values(${label}, ${latitude}, ${longitude}, ${image}, ${timestamp}, ${precision})', req.body)
  //      .then(function () {
  //          res.status(200).json({
    //          status: 'success',
  //              message: 'Inserted one marker'
    //         });
  //        })
  //      .catch(function (err) {
  //          return next(err);
  //      });
  //   })
  //  .catch(error => {
  //        console.log(error);
  //        //return next(error);
  //   });
  //var imageName = req.body.label +'_'+req.body.latitude +'_'+req.body.longitude+'_'+req.body.timestamp+'.PNG';
  //imageName = imageName.replace(/ /g, "_");
  //imageName = imageName.replace(/:/g, "-");
  //var filesave = '../Model/Catalogs/sinais_de_transito/figures/' + imageName;
  // filesave = filesave.replace(/ /g, "_");
  // filesave = filesave.replace(/:/g, "-");
  //console.log(filesave);
  //fs.writeFileSync(filesave, buff);
  // fs.writeFile(filesave, buff, 'base64', function(err) {
  //  console.log(err);
  //});
  //fs.writeFileSync("../Model/Catalogs/sinais_de_transito/figures/" + imageName, buff);
  //console.log("Object: %j", req.body);
  //console.log(idfeat);
  //req.body.label = idfeat;
  //req.body.image = 'https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/figures/'+imageName+'?raw=true'
    //db.none('insert into marker(featureid, latitude, longitude, imagepath , timestamp, precision)' +
    //  'values(${label}, ${latitude}, ${longitude}, ${image}, ${timestamp}, ${precision})', req.body)
    //.then(function () {
     // res.status(200).send('Acceptable');
//        status(200)
//         .json({
//           status: 'success',
//           message: 'Inserted one marker'
//         });
   // })
    //.catch(function (err) {
    //  return next(err);
    //});
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
    multiMarker : multiMarker,
    createMarker: createMarker,
    getAllMarkers: getAllMarkers
};