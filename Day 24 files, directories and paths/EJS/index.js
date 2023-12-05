import express from "express";

const app = express();
const port = 3000;

app.get("/", (req, res) => {
    const d = new Date();
    let day = d.getDay();

    //console.log(day);
    let type = "a weekday";
    let adv = "Eat, Code, Sleep";

    if(day === 0 || day === 6){
        type = "a weekend";
        adv = "Sleep, Sleep, Sleep";
    }

    res.render("index.ejs",{
        dayType: type,
        advice: adv,
    });
});


app.listen(port, () => {
    console.log(`Listening on port ${port}`);
});