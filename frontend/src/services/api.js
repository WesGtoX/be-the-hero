import axios from 'axios'


const api = axios.create({
  baseURL: 'http://api.bethehero.wesleymends.com.br'
})

export default api
