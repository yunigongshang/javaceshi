
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

// const express = require('express');
// const bodyParse = require('body-parser')
// const app = express();
// const port =8084;
// app.use(bodyParse.urlencoded({extended:false}))
// app.use(bodyParse.json())

// app.use(express.static('puli'))
// app.get('/',(req,res)=> res.send('Hello world'));

// app.post('/ent',(req,res)=>{
//     console.log(req.body)
//     res.send('post请求成功')
// })
// app.listen(port,()=> console.log(`http://localhost:${port}`))

//======================================================================2023年7月12日
// const express = require('express')
// const app = express()
// app.get('/',function(req,res){
//     throw new Error('服务器内部发生了错误！')
//     res.send('Home Page.')
// })
// app.use(function (err,req,res,next){
//     console.log('发生了错误：'+ err.message)
//     res.send('Error!'+err.message)
// })

// app.listen(8083,()=>{
//     console.log('http://localhost:8083')
// })


const express = require('express')
const app = express()
const apiRouter=require('./sever.js')
app.use('/api',apiRouter)

apiRouter.get('/get',(req,res)=>{
    const query= req.query
    res.send({
        status:0,
        msg:'GET请求成功',
        data:query
    })
})
apiRouter.post('/post',(req,res)=>{
    const body= req.body
    res.send({
        status:0,
        msg:'POST请求成功',
        data:body
    })
})

app.listen(8083,()=>{
    console.log('http://localhost:8083/api/get')
})