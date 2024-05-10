# M07_UF4_P5_Botiga

## Datos de prueba DDBB
**Tabla Cataleg**
Insertar datos de categorías
```
INSERT INTO cataleg_categoria (name) VALUES
('Electrónica'),
('Ropa'),
('Hogar');
```

Insertar datos de productos asociados a categorías
```
INSERT INTO cataleg_producte (name, description, price, valoration, quantity, categoria_id) VALUES
('Laptop', 'Laptop de última generación', 1200.00, 4, 10, 1),
('Camisa', 'Camisa de algodón de alta calidad', 30.00, 5, 20, 2),
('Sartén', 'Sartén antiadherente de 24 cm', 25.00, 4, 15, 3),
('Teléfono móvil', 'Teléfono inteligente con cámara de alta resolución', 800.00, 4, 12, 1),
('Pantalón', 'Pantalón vaquero de estilo casual', 40.00, 5, 25, 2),
('Cafetera', 'Cafetera de cápsulas con sistema de autolimpieza', 90.00, 4, 8, 3);
```
### Ejemplo inserción de datos en Categoria (nuevo producto)
{
    "name": "Producto Nuevo",
    "description": "Descripcion de producto nuevo...",
    "price": "200",
    "valoration": 4,
    "quantity": 20,
    "categoria": 1
}
* Para editar sigue el mismo formato json
**Tabla Pagament**
Insertar datos prueba a User
```
INSERT INTO pagaments_user (name, email, password) VALUES
('Usuario 1', 'usuario1@example.com', 'contraseña1'),
('Usuario 2', 'usuario2@example.com', 'contraseña2'),
('Usuario 3', 'usuario3@example.com', 'contraseña3');
```

Insertar datos de pagamentos
```
INSERT INTO tuapp_pagament (tarjet_num, exp_date, cvc, user_id) VALUES
('1234567890123456', '2025-12-31', 123, 1),
('9876543210987654', '2026-12-31', 456, 2),
('1111222233334444', '2027-12-31', 789, 3);
```


