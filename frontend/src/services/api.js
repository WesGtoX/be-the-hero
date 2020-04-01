import axios from 'axios'

url = process.env.BASE_URL || 'http://localhost:3333'

const api = axios.create({
  baseURL: url
})

export default api
