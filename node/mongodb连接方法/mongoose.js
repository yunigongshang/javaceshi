//mongoose连接方法
const mongoose = require('mongoose');

const url = 'mongodb://localhost:27017/my_name';

mongoose.connect(url, {useNewUrlParser: true, useUnifiedTopology: true});
const db = mongoose.connection;

db.on('error', console.error.bind(console, '连接错误：'));

db.once('open', function() {

db.collection('collection').find({}).toArray(function(err, docs) {
  if (err) throw err;
  console.log(docs);
});
});
