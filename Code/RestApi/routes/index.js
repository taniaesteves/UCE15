var express = require('express');
var router = express.Router();


var db = require('../queries');

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

//router.post('/api/createMarker', db.createMarker);
router.get('/api/getAllMarkers', db.getAllMarkers);


module.exports = router;
