# ORDBMS Project

This project implements an Object-Relational Database Management System (ORDBMS) using a SQL schema for managing user engagement with multimedia content across different platforms.

## Project Structure

```
ordbms-project
├── src
│   ├── db
│   │   ├── schema.sql        # SQL schema for database tables
│   │   └── index.ts          # Database connection and initialization
│   ├── models
│   │   └── index.ts          # Models representing database tables
│   └── app.ts                # Entry point for the application
├── package.json               # npm configuration file
├── tsconfig.json              # TypeScript configuration file
└── README.md                  # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd ordbms-project
   ```

2. **Install dependencies:**
   ```
   npm install
   ```

3. **Compile TypeScript files:**
   ```
   npm run build
   ```

4. **Run the application:**
   ```
   npm start
   ```

## Usage Guidelines

- The `src/db/schema.sql` file contains the SQL schema for the database tables, including dimension tables and the fact table.
- The `src/db/index.ts` file is responsible for connecting to the database and executing the SQL schema.
- The `src/models/index.ts` file exports models that represent the database tables.
- The `src/app.ts` file serves as the entry point for the application, setting up the database connection and initializing services.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features you'd like to add.