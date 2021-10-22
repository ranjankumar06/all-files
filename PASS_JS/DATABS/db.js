require('dotenv').config()

console.log(process.env.DB_HOST)
const knex=require('knex')({
    client:'mysql',
    connection:{
        user:process.env.DB_USER,
        host:process.env.DB_HOST,
        password:process.env.DB_PASS,
        database:process.env.DB_NAME
    }
})

knex.schema.createTable('google',(table)=>{
    table.increments('Id')
    table.string('Name')
    table.string('Email')
    table.string('Image_url')

}).then((data)=>{
    console.log('table created')
}).catch((err)=>{
    console.log('table already created')
})



module.exports =knex