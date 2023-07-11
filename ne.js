
// const moment = require('moment')
// const at = moment().format('YYYY-MM-DD HH:mm:ss')
// console.log(at)

// const request = require("request");

// const fs =require('fs')
// fs.readFile('./学习.txt','utf8',function(err,dataStr){
//     if(err){
//         return console.log('读取文件失败!'+err.message);
//     }
//     console.log('读取文件成功!'+dataStr);
// })

// const http = request('http');
// const req = http.request({
//     url:'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=7bf8fd07-2414-41b1-9c36-f187807d44ef',
//     method: 'POST',
//     headers: {
//      'Content-Type': 'application/json'
//    },
//     data : { 'msgtype': 'text', 
//              'text':{
//              'content':'hello'
//         }}
// },
// (res)=>{
//     res.resume();
//     res.on('end',()=>{
//         console.log('请求成功');
//     })
// })

// const https = require('https');

// const url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=7bf8fd07-2414-41b1-9c36-f187807d44ef';
// const data = { 'msgtype': 'text', 
//                 'text':{
//                     'content':'hello'
//                 }};

// const postData = JSON.stringify(data);

// const options = {
//   method: 'POST',
//   headers: {
//     'Content-Type': 'application/json',
//   }
// };

// const req = https.request(url, options, (res) => {
//   let responseData = '';

//   res.on('data', (chunk) => {
//     responseData += chunk;
//   });

//   res.on('end', () => {
//     console.log(responseData);
//   });
// });

// req.on('error', (error) => {
//   console.error(error);
// });

// req.write(postData);
// req.end();

const express = require('express');
const app = express();
const port =8084;
app.get('/',(req,res)=> res.send('Hello world'));

app.listen(port,()=> console.log(`Server listening on port ${port}`));