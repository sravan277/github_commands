const express = require("express");

const app = express();


app.get("/", (req, res)=>{
    res.status(200).json({"Message":"Hello World"});
})

app.listen(3000, (req, res)=>{
    console.log("http://localhost:3000");
})