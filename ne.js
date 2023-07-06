
// const moment = require('moment')
// const at = moment().format('YYYY-MM-DD HH:mm:ss')
// console.log(at)

const fs =require('fs')
fs.readFile('../学习.txt','utf8',function(err,dataStr){
    if(err){
        return console.log('读取文件失败!'+err.message);
    }
    console.log('读取文件成功!'+dataStr);
})