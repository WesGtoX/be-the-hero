import axios from 'axios'

url = process.env.BASE_URL || 'http://api.bethehero.wesleymends.com.br'

const api = axios.create({
  baseURL: url
})

export default api
