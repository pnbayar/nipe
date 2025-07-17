-- 1️⃣ Create a table
CREATE TABLE pets (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50),
  breed VARCHAR(50),
  age INT
);

-- 2️⃣ Insert some rows
INSERT INTO pets (name, breed, age) VALUES
  ('Milo', 'Tabby', 3),
  ('Zara', 'Labrador', 5),
  ('Rex', 'German Shepherd', 2);

-- 3️⃣ Select all pets older than 2
SELECT id, name, breed, age
  FROM pets
 WHERE age > 2
 ORDER BY age DESC;
-- 4️⃣ Update a pet's age
UPDATE pets 
 SET age = 4
 WHERE name = 'Milo';                   
-- 5️⃣ Delete a pet by name
DELETE FROM pets
 WHERE name = 'Rex';    