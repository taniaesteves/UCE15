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

// query functions
// curl --data "label=B2&latitude=41.560404&longitude=-8.4056225&imagepath=https://github.com/taniaesteves/UCE15/blob/master/Code/Model/Catalogs/sinais_de_transito/figures/b2_2017-11-25_20-38-25.PNG?raw=true&timestamp=2017-11-25 20:38:25&precision=0.89" http://localhost:3000/api/createMarker

function multiMarker(req, res, next){

  console.log(req.body);
  res.status(200).json({
    status: 'success',
    message: 'Multi Marker inserido'
  });
}


function createMarker(req, res, next) {
  let data = req.body.image;
  let buff = new Buffer(data, 'base64');
  var localidade;
  var idfeat, idmarker;
  
  // buscar o ID da feature 
  db.one("select id from feature where code = $1",req.body.label).then(data => {
    idfeat = data.id;
    // filtro para ver se o marker esta dentro do raio de 20m de um dos markers usando a formula de haversine
    db.many('select * from ( select *, ((asin(sqrt((sin(latitude*(pi() / 180)) - sin($1*(pi() / 180))) * (sin(latitude*(pi() / 180)) - sin($1*(pi() / 180))) + (sin((longitude - ($2))*(pi() / 180)) * cos(latitude*(pi() / 180))) * (sin((longitude - ($2))*(pi() / 180)) * cos(latitude*(pi() / 180))) + (sin(latitude*(pi() / 180)) - sin($1*(pi() / 180))) * (sin(latitude*(pi() / 180)) - sin($1*(pi() / 180)))) / 2) * 2 * 6371)*1000) as Cal '+
      'from marker where featureid = $3 order by Cal ASC) as foo where foo.cal < 20', 
        [req.body.latitude, req.body.longitude, idfeat]).then(dados => {
        console.log("Marker atualizado");
        // marker mais perto
        // console.log(dados[0]);
        // calcular as media das precisions e da longi e lati para dar update ao marker(last timestamp, longi, lat e preci e total-detections)
        var uplatitude = (dados[0].latitude * dados[0].total_detections + req.body.latitude) / (dados[0].total_detections + 1);
        var uplongitude = (dados[0].longitude * dados[0].total_detections + req.body.longitude) / (dados[0].total_detections + 1);
        var upprecision = (dados[0].precision * dados[0].total_detections + req.body.precision) / (dados[0].total_detections + 1);
        // guardar imagem com informações do marker correspondente
        var imageName = dados[0].id +'_'+ req.body.label +'_'+req.body.timestamp +'_'+req.body.latitude+'_'+req.body.longitude+'.PNG';
        imageName = imageName.replace(/ /g, "_"); imageName = imageName.replace(/:/g, "-");
        var filesave = '../Model/Catalogs/sinais_de_transito/figures/' + imageName;
        fs.writeFileSync(filesave, buff);
        req.body.image = 'sinais_de_transito/figures/'+imageName;
        db.none('update marker set latitude = $1, longitude = $2, imagepath = $3, last_timestamp = $4 , precision = $5, total_detections = $6 where id = $7', [uplatitude, uplongitude, req.body.image, req.body.timestamp, upprecision, (dados[0].total_detections+1), dados[0].id]).then(function () {}).catch(function (err) { console.log(err); return next(err); });
        // resposta ao pedido
        res.status(200).json({
        status: 'success',
        message: 'Updated one marker'
      });

    }).catch(newM =>{
        console.log("Novo marker");
        // buscar localização com o geocoder para o novo marker
        geocoder.reverse({lat:req.body.latitude, lon:req.body.longitude}).then(res1 => {
          // console.log(res1);
          localidade = res1[0].streetName + ', ' + res1[0].city;
          // inserir marker na BD
          db.one('insert into marker(featureid, latitude, longitude,imagepath, first_timestamp, last_timestamp, precision, total_detections, address, ocurr)' +
              'values($1, $2, $3, $4, $5, $5, $6, 1, $7, 1) RETURNING id', 
                [idfeat, req.body.latitude, req.body.longitude, 'temp' ,req.body.timestamp, req.body.precision, localidade])
          .then(rs => {
              // guardar imagem com o id do marker e atualizar BD
              idmarker = rs.id;
              var imageName = idmarker +'_'+ req.body.label +'_'+req.body.timestamp +'_'+req.body.latitude+'_'+req.body.longitude+'.PNG';
              imageName = imageName.replace(/ /g, "_"); imageName = imageName.replace(/:/g, "-");
              var filesave = '../Model/Catalogs/sinais_de_transito/figures/' + imageName;
              fs.writeFileSync(filesave, buff);
              req.body.image = 'sinais_de_transito/figures/'+imageName;
              db.none('update marker set imagepath = $1 where id = $2', [req.body.image, idmarker]).then(function () {}).catch(function (err) { console.log(err); return next(err); });

              // resposta ao pedido
              res.status(200).json({
              status: 'success',
              message: 'Inserted one marker'
            });
          }).catch(function (err) {
            console.log(err);
            return next(err);
          });
          

        }).catch(error => {
          console.log(error);
          return next(error);
        });
    });

  }).catch(error => {
    console.log(error);
    return next(error);
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
    multiMarker : multiMarker,
    createMarker: createMarker,
    getAllMarkers: getAllMarkers
};