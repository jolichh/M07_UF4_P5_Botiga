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

**Tabla Pagament**

