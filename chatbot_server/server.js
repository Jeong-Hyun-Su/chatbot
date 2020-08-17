const express = require('express');
const request = require('request');
const urlencode = require('urlencode');
const app = express();
const port = 4000


app.get('/chatbot', (req, res) => {
    let data = Object();
    data.okay = true;
    data.answer = "";
    data.question = req.query['sentence'];
    
    if(data.question == undefined || data.question == ""){
         data.okay = false;
         data.question = "";
    }

    let url = 'http://172.22.0.1:' + 5000 + '/chatbot?sentence=' + urlencode(data.question);
    
    request({ 
                method:'GET',
                uri: url,
                encoding: null
            }, 
            function(error, response, body) { 
                if(!error && response.statusCode == 200){
                    data.answer = (JSON.parse(body))['answer'];
                    console.log(data.answer);   
                
                    res.json(data);
                }
                else{
                    throw error;
                } 
            }
    );
});

app.listen(port, '0.0.0.0');