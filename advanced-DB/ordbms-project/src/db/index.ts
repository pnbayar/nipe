import { Pool } from 'pg';
import fs from 'fs';
import path from 'path';

const pool = new Pool({
    user: 'your_username',
    host: 'localhost',
    database: 'your_database',
    password: 'your_password',
    port: 5432,
});

const initializeDatabase = async () => {
    const schemaPath = path.join(__dirname, 'schema.sql');
    const schema = fs.readFileSync(schemaPath, 'utf8');

    try {
        await pool.query(schema);
        console.log('Database initialized successfully.');
    } catch (error) {
        console.error('Error initializing database:', error);
    }
};

const closeConnection = async () => {
    await pool.end();
    console.log('Database connection closed.');
};

export { initializeDatabase, closeConnection };