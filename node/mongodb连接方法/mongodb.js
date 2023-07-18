
//mongodb连接方法
const { MongoClient, ServerApiVersion } = require("mongodb");

const uri = "mongodb://localhost:27017";

const client = new MongoClient(uri);
client.connect();

// 在这里执行其他操作，例如查询、插入、更新等
const cursor = client.db("my_name").collection("collection").find({}); //collection是集合名

// 处理结果集
// const resu = cursor.toArray()    //和下面的forEach二选一
// console.log(resu);
cursor.forEach(console.log);    

