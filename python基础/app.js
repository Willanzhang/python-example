let http = require('http')
http.createServer(function(req, res) {
  res.writeHead(200, {'Content-type': 'text/plain;charset=utf-8'})
    console.log('你好')
    res.end('派洛')
  }).listen('3000')
  console.log('Server is running on 47.106.156.14:3000')
