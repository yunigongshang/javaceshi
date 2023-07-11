const   userRouter = require('./dam.js')
const express = require('express')
const app = express()
// app.use(userRouter)
app.use('/api',userRouter)

app.listen(8083,()=>{
    console.log('http://localhost:8083')
})