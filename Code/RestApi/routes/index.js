var express = require('express');
var router = express.Router();


var db = require('../queries');

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Atlas Innovation RESTful API' });
});

router.get('/api/getAllMarkers', db.getAllMarkers);
router.post('/api/createMarker', db.createMarker);


module.exports = router;
