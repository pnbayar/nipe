import express from 'express';
import { initializeDatabase } from './db/index';

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());

initializeDatabase()
    .then(() => {
        app.listen(PORT, () => {
            console.log(`Server is running on port ${PORT}`);
        });
    })
    .catch(err => {
        console.error('Database initialization failed:', err);
    });