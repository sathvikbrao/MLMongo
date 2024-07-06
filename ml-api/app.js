const express = require('express');
const mongoose = require('mongoose');
const { exec } = require('child_process');
const fs = require('fs');

const app = express();
const port = 3000;

// Connect to MongoDB
mongoose.connect('mongodb://127.0.0.1:27017/modeldb');

const conn = mongoose.connection;
conn.once('open', () => {
    console.log('Connected to MongoDB');
});

// Define a route to fetch and use the model
app.get('/fetch-model', async (req, res) => {
    const collection = conn.db.collection('models');
    const modelData = await collection.findOne({ model_name: 'random_forest' });

    if (modelData) {
        // Save the model bytes to a temporary file
        fs.writeFileSync('temp_model.joblib', modelData.model.buffer);

        // Run a Python script to load and use the model
        exec('python use_model.py temp_model.joblib', (error, stdout, stderr) => {
            if (error) {
                res.status(500).send(`Error: ${error.message}`);
                return;
            }
            if (stderr) {
                res.status(500).send(`Stderr: ${stderr}`);
                return;
            }
            res.send(`Output: ${stdout}`);
        });
    } else {
        res.status(404).send('Model not found');
    }
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
