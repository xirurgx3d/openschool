require('dotenv').config()
const express = require('express');
const bodyParser = require('body-parser');
const { randomBytes } = require('crypto');
const cors = require('cors');
const axios = require('axios');

const app = express();
app.use(bodyParser.json());
app.use(cors());


app.listen(process.env.PORT | 4000, () => {
  console.log('article Listening on ' + process.env.PORT);
});
