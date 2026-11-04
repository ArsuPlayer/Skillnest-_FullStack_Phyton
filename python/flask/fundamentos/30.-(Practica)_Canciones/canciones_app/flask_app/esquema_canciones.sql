-- 1. Crear la base de datos si no existe
CREATE DATABASE IF NOT EXISTS esquema_canciones;
USE esquema_canciones;

-- 2. Crear la tabla de usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(45) NOT NULL,
    email VARCHAR(45) NOT NULL,
    contrasena VARCHAR(45) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 3. Crear la tabla de canciones
CREATE TABLE IF NOT EXISTS canciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(45) NOT NULL,
    artista VARCHAR(45) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 4. Crear la tabla intermedia de favoritos (relación N:N con clave primaria compuesta)
CREATE TABLE IF NOT EXISTS favoritos (
    usuario_id INT NOT NULL,
    cancion_id INT NOT NULL,
    PRIMARY KEY (usuario_id, cancion_id),
    CONSTRAINT fk_usuarios_has_canciones_usuarios
        FOREIGN KEY (usuario_id)
        REFERENCES usuarios (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fk_usuarios_has_canciones_canciones
        FOREIGN KEY (cancion_id)
        REFERENCES canciones (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);