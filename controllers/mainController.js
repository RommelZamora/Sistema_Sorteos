const express = require('express');
const router = express.Router();
const mainModel = require('../models/mainModel');

// Ruta para la página principal
router.get('/', (req, res) => {
    const data = mainModel.getData();
    res.render('index', { data, user: req.user });
});

module.exports = router;
