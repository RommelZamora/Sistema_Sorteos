const express = require('express');
const passport = require('passport');
const router = express.Router();

// Ruta para iniciar la autenticación con Instagram
router.get('/instagram', passport.authenticate('instagram'));

// Ruta de callback para Instagram
router.get('/instagram/callback',
    passport.authenticate('instagram', { failureRedirect: '/auth/failure' }),
    (req, res) => {
        // Autenticación exitosa, redirigir a la página principal
        res.redirect('/');
    });

// Ruta para iniciar la autenticación con Facebook
router.get('/facebook', passport.authenticate('facebook'));

// Ruta de callback para Facebook
router.get('/facebook/callback',
    passport.authenticate('facebook', { failureRedirect: '/auth/failure' }),
    (req, res) => {
        // Autenticación exitosa, redirigir a la página principal
        res.redirect('/');
    });

// Ruta para manejar el fallo en la autenticación
router.get('/failure', (req, res) => {
    res.send('Autenticación cancelada o fallida. Por favor, inténtalo de nuevo.');
});

// Ruta para cerrar sesión
router.get('/logout', (req, res) => {
    req.logout(err => {
        if (err) {
            return next(err);
        }
        res.redirect('/');
    });
});

module.exports = router;
