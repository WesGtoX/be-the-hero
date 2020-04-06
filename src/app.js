const express = require('express')
const cors = require('cors')
const { errors } = require('celebrate');
const routes = require('./routes')

const app = express()

domain = process.env.WHITELIST_DOMAIN
subDomain = process.env.WHITELIST_SUB_DOMAIN

const whitelist = [domain, subDomain]
const corsOptions = {
  origin: function (origin, callback) {
    if (whitelist.indexOf(origin) !== -1) {
      callback(null, true)
    } else {
      callback(new Error('Not allowed by CORS'))
    }
  }
}

app.use(cors(corsOptions))
// app.use(cors())
app.use(express.json())
app.use(routes)
app.use(errors())


module.exports = app
