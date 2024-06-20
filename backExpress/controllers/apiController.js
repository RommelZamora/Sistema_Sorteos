const express = require('express');
const router = express.Router();
const axios = require('axios');

router.get('/photos', async (req, res) => {
    const user = req.user;
    const accessToken = req.user.accessToken; // Asegúrate de que el token de acceso está disponible
    const after = req.query.after || '';
    const before = req.query.before || '';
    const userId = req.user.id;

    let apiUrl = `https://graph.facebook.com/v20.0/${userId}/photos?fields=created_time,id,name,link,images&limit=25&pretty=0`;
    if (after) {
        apiUrl += `&after=${after}`;
    } else if (before) {
        apiUrl += `&before=${before}`;
    }

    try {
        const response = await axios.get(apiUrl, {
            headers: {
                Authorization: `Bearer ${accessToken}`
            }
        });

        res.json(response.data);
    } catch (error) {
        console.error('Error fetching photos:', error);
        res.status(500).json({ error: 'Failed to fetch photos' });
    }
});

module.exports = router;
