import axios from 'axios';

export default axios.create({
    baseURL: process.env.NODE_ENV === 'production' ? 'https://www.johnclaro.com/podplayer' : 'http://localhost:8000/podplayer'
})