-- ==========================================================
-- BASE DE DATOS Y TABLAS
-- ==========================================================

CREATE DATABASE IF NOT EXISTS primera_flask;
USE primera_flask;

-- Tabla Mascotas
CREATE TABLE IF NOT EXISTS mascotas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    tipo VARCHAR(100) NOT NULL,
    color VARCHAR(100) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Tabla Usuarios (Ejercicio de consolidación)
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    edad INT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- ==========================================================
-- DATOS DE PRUEBA
-- ==========================================================

INSERT INTO mascotas (nombre, tipo, color) VALUES
    ('Firulais', 'Perro', 'Café'),
    ('Michi', 'Gato', 'Negro'),
    ('Luna', 'Perro', 'Blanco'),
    ('Nala', 'Gato', 'Naranjo'),
    ('Coco', 'Conejo', 'Blanco');

INSERT INTO usuarios (nombre, email, edad) VALUES
    ('Carlos Mendoza', 'carlos@example.com', 28),
    ('Ana Gómez', 'ana@example.com', 34),
    ('Lucía Pérez', 'lucia@example.com', 22);