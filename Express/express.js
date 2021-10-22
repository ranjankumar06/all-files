// const express=require("express");
// const app=express();
// app.get('/',(req,res)=>{
//     res.send("hello ranjan kumar")
// });
// app.get("/about",(req,res)=>{
//     console.log("hello from the about page");
// })
// app.listen(8008,()=>{
//     console.log("server is running on 8000 thousand port");
// })


const express=require('express');
const app=express();
const port=9000;
app.get("/",(req,res)=>{
    res.send("this is home page");
});

app.get("/about",(req,res)=>{
    res.send("this is about page");
})
app.listen(port,()=>{
    console.log("port is running 9000");
})
   


