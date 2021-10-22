const express=require('express')
const Port=30000
const app=express()
app.get("/",(req, res, next)=>{
    res.send("hello server")
})

app.listen(Port,(err)=>{
    console.log(`server is running on ${Port}`);
})