require('dotenv').config
const express=require('express')
const app=express();
const  passport=require('passport');
const GoogleStrategy = require('passport-google-oauth2').Strategy;
app.use(passport.initialize())

require('./DATABS/db')
const google=express.Router()
app.use("/",google);
require("./auth/Google")(app,passport)

// const page=require('./auth/rout/router')
// app.use('/',page)

app.listen(8000,()=>{
  console.log("we are connescted 8000");
})

