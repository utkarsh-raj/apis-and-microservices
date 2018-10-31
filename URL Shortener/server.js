'use strict';

var express = require('express');
var mongo = require('mongodb');
var mongoose = require('mongoose');
var bodyParser = require('body-parser');
var URL = require('url-parse');

var cors = require('cors');

var app = express();

// Basic Configuration 
var port = process.env.PORT || 3000;

/** this project needs a db !! **/ 
// mongoose.connect(process.env.MONGOLAB_URI);

var url = {};
var number = 0;

app.use(cors());

/** this project needs to parse POST bodies **/
// you should mount the body-parser here

app.use(bodyParser.urlencoded({extended: true}));

app.use('/public', express.static(process.cwd() + '/public'));

app.get('/', function(req, res){
  res.sendFile(process.cwd() + '/views/index.html');
});

  
// your first API endpoint... 
app.get("/api/hello", function (req, res) {
  res.json({greeting: 'hello API'});
});

app.get("/api/shorturl/:number", function(req, res) {
  var number = req.params.number;
  res.redirect(url[number]);
});

app.post("/api/shorturl/new", function(req, res, next) {
  var url1 = new URL(req.body.url);
  if (url1.slashes === false) {
    res.json({
      "error": "Invalid URL"
    });
    next();
  }
  console.log(url1);
  number += 1;
  url[number] = req.body.url;
  res.json({
    "original_url": req.body.url,
    "short_url": number
  });
});


app.listen(8080, function () {
  console.log('Node.js listening ...');
});