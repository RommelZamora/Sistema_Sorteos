const express = require('express');
const router = express.Router();
const passport = require('passport');

// Ruta de autenticación con Facebook
router.get('/facebook', passport.authenticate('facebook', { scope: ['email', 'user_photos'] }));

// Ruta de callback de Facebook
router.get('/facebook/callback',
    passport.authenticate('facebook', { failureRedirect: '/' }),
    (req, res) => {
        res.redirect('/');
    }
);

// Ruta de autenticación con Instagram
router.get('/instagram', passport.authenticate('instagram'));

// Ruta de callback de Instagram
router.get('/instagram/callback',
    passport.authenticate('instagram', { failureRedirect: '/' }),
    (req, res) => {
        res.redirect('/');
    }
);

// Ruta para cerrar sesión
router.get('/logout', (req, res) => {
    req.logout((err) => {
        if (err) { return next(err); }
        res.redirect('/');
    });
});

module.exports = router;
