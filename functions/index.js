const functions = require('firebase-functions');
const express = require('express');
const cors = require('cors');
const axios = require('axios');

const app = express();

// Use CORS middleware to allow requests from all origins
app.use(cors({ origin: true }));  // Allow all origins

// API endpoint to fetch Google Sheets data
app.get('/getDonations', async (req, res) => {
  try {
    const response = await axios.get(
      `https://sheets.googleapis.com/v4/spreadsheets/${process.env.SHEETS_ID}/values/donationList?key=${process.env.SHEETS_API_KEY}`
    );
    console.log(response.data); // Log the data for debugging
    res.json(response.data);
  } catch (error) {
    console.error('Error fetching data from Google Sheets:', error);
    res.status(500).send('Error fetching data');
  }
});

// Export the function
exports.api = functions.https.onRequest(app);
