const passport = require('passport');
const InstagramStrategy = require('passport-instagram').Strategy;
const FacebookStrategy = require('passport-facebook').Strategy;
const axios = require('axios');

passport.use(new InstagramStrategy({
    clientID: '3132238710246080', // Reemplaza con tu clientID de Instagram
    clientSecret: '660b85e7600de6ccf63d2ef40eca7ce7', // Reemplaza con tu clientSecret de Instagram
    callbackURL: 'https://localhost:3200/auth/instagram/callback',
    scope: ['user_profile'],
    passReqToCallback: true
},
async (req, accessToken, refreshToken, profile, done) => {
    try {
        // Intercambiar el código de autorización por un token de acceso
        const response = await axios.post('https://api.instagram.com/oauth/access_token', {
            client_id: '3132238710246080', // Reemplaza con tu clientID de Instagram
            client_secret: '660b85e7600de6ccf63d2ef40eca7ce7', // Reemplaza con tu clientSecret de Instagram
            grant_type: 'authorization_code',
            redirect_uri: 'https://localhost:3200/auth/instagram/callback',
            code: req.query.code
        });

        const accessToken = response.data.access_token;

        // Obtener el ID del usuario con el token de acceso
        const userResponse = await axios.get(`https://graph.instagram.com/me?fields=id&access_token=${accessToken}`);
        const user = userResponse.data;

        return done(null, user); // Devuelve el usuario directamente
    } catch (err) {
        console.error('Error fetching user profile:', err);
        console.error('Response data:', err.response ? err.response.data : 'No response data');
        return done(err);
    }
}));

passport.use(new FacebookStrategy({
    clientID: '2616988788481233', // Reemplaza con tu clientID de Facebook
    clientSecret: '269cd70fdbf815535e7ff7b52456f2a7', // Reemplaza con tu clientSecret de Facebook
    callbackURL: 'https://localhost:3200/auth/facebook/callback',
    scope: ['email', 'user_photos'], // Asegúrate de solicitar los permisos adecuados
    passReqToCallback: true
},
async (req, accessToken, refreshToken, profile, done) => {
    try {
        // Obtener el perfil del usuario con el token de acceso
        const userResponse = await axios.get(`https://graph.facebook.com/me?fields=id,photos{created_time,id,name,link,images}&access_token=${accessToken}`);
        const user = userResponse.data;

        return done(null, user); // Devuelve el usuario directamente
    } catch (err) {
        console.error('Error fetching user profile:', err);
        console.error('Response data:', err.response ? err.response.data : 'No response data');
        return done(err);
    }
}));

passport.serializeUser((user, done) => {
    done(null, user);
});

passport.deserializeUser((user, done) => {
    done(null, user);
});

module.exports = passport;
