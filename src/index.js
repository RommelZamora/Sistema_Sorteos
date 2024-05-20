const express = require('express');
const session = require('cookie-session');
const path = require('path');
const engine = require('ejs-mate');//motor de plantillas
const morgan = require('morgan');

// Initializations
const app = express();

// settings
app.set('port', process.env.PORT || 3000); //inicializar en el port 3000
//path.join(__dirname,, 'views') -> retorna la ruta inicial del proycto para concatenarlo con views
app.set('views', path.join(__dirname, 'views'));
app.engine('ejs', engine); //definir motor de plantillas
app.set('view engine', 'ejs'); //inicializar motor de plantillas

// Middlewares(funciones que se ejecutan antes de darselas a las rutas)
app.use(morgan('dev'));
app.use(session({
  secret: 'mysecretword',
  signed: true
}));

// Global Variables
app.use((req, res, next) => {
  res.locals.formatDate = (date) => {
    let myDate = new Date(date * 1000);
    return myDate.toLocaleString();
  }

  if(req.session.access_token && req.session.access_token != 'undefined') {
    res.locals.isLoggedIn = true;
  } else {
    res.locals.isLoggedIn = false;
  }
  next();
});

// Routes
app.use(require('./routes/index'));

// static files
app.use(express.static(path.join(__dirname, 'public')));

// Starting the Server
app.listen(app.get('port'), () => {
  //escuchar en el puerto 3000
  console.log('server on port', app.get('port'));
});