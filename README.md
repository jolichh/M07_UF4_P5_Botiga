# M07_UF4_P5_Botiga
Crear un projecte de Django REST FRAMEWORK de nom botiga_grupX (on X es el número del grup). El producte ha de tindre, mńim, 6 camps sense comptar id.
    
Aquest projecte haurà de tindre les següents 4 aplicacions:

**(INTEGRAN A)**

Gestió del catàleg del producte (mínim 10 registres) (branca catalog).
Afegir nous productes (commit amb missatge). 
Actualitzar productes (commit amb missatge).
Eliminar productes (commit amb missatge).
Veure informació del producte (commit amb missatge).

**(INTEGRAN B)**

Gestió del carretó de la compra (mínim, un carretó amb 4 productes) (branca cart).
Afegir productes al carretó (commit amb missatge).
Eliminar productes del carretó (commit amb missatge).
Eliminar tot el carretó (commit amb missatge).
Modificar quantitats (commit amb missatge).
Mètode de compra de carretó (commit amb missatge).

**(INTEGRAN B)**

Gestió de comandes (repartir 10 registres entre cada estat) (branca orders).
Mostrar historial de compres fetes (commit amb missatge).
Mostrar informació de carretons sense finalitzar. No cal treballar amb tokens. Si es realitza la compra (mirar pagaments) passa a històrics, si no és el cas, es queda en historial de carretons sense finalitzar i si se li dona a eliminar carretó s’elimina i no queda registre (commit amb missatge).

**(INTEGRAN A)**

Gestió pagaments (simulat) (branca payments).
Ha de tindre les opcions de; posar número de tarjeta, data caducitat i CVC.
Cal consultar si les dades son correctes, i si son correctes es procedeix al pagament. 
Quan es faci el pagament, es demana una autenticació (usuari i password) altra vegada i  es fa la verificació de dades (commit amb missatge).
Una vegada feta la compra, afegir-la a històrics (gestió comandes) .Enviarà un missatge de compra feta (commit amb missatge).


## Ejemplos de Datos de prueba DDBB
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

**Ejemplo inserción de datos en Categoria (nuevo producto)**
```
{ "name": "Producto Nuevo", "description": "Descripcion de producto nuevo...", "price": "200", "valoration": 4, "quantity": 20, "categoria": 1 }
```

* Para editar sigue el mismo formato json 

**Tabla Pagament Insertar datos prueba a User**
```
INSERT INTO pagaments_user (name, email, password) VALUES
('Usuario 1', 'usuario1@example.com', 'contraseña1'),
('Usuario 2', 'usuario2@example.com', 'contraseña2'),
('Usuario 3', 'usuario3@example.com', 'contraseña3');
```
Insertar datos de pagamentos
```
INSERT INTO pagaments_pagament (tarjet_num, exp_date, cvc, user_id) VALUES
('1234567890123456', '2025-12-31', 123, 1),
('9876543210987654', '2026-12-31', 456, 2),
('1111222233334444', '2027-12-31', 789, 3);
```

Insertar datos de Carreto_carrito
```
INSERT INTO public.carreto_carrito(compra_realizada) VALUES(false)
```

Update payment format:
```
{   
    "username": "Usuario 1",
    "password": "contraseña1",
    "tarjet_num": "1234567890123456", //nuevos datos
    "exp_date": "2025-12-31", //nuevos datos
    "cvc": "123" //nuevos datos
}
```
## VIDEO
[Carpeta Drive de VIDEOs](https://drive.google.com/drive/folders/1DEyfNLLJuY4ljnYUNJ9dc3j8RsvN88JT?usp=sharing)

Orden de los 4 videos enumerados en la carpeta en este orden: 1-Cataleg, 2-Carreto, 3-Comandas, 4-Pagament

## CAPTURAS DE PANTALLA
### CAPTURAS DE PANTALLA CARRETO:

En esta captura se ve el GET de carreto donde se muestra su id mas los productos que hay dentro del carrito con su cantidad

![GET CARRETO](img/CARRETO/1.GET_CARRETO.png)

Aqui se ve el JSON para hacer el POST en Carreto y crear un nuevo carreto

![POST CARRETO](img/CARRETO/2.POST_CARRETO.png)

Se muestra una confirmación de que se ha creado el carrito y se han introducido los datos

![Confirmación de que se ejecuto correctamente el metodo POST](img/CARRETO/2.1.Confirmación_POST_CARRETO.png)

Aqui se muestra el metodo GET de un carrito con una ID en especifico, y la id del carrito se puede ver en el path o en el propio GET 

![GET CARRETO ESPECIFICO](img/CARRETO/3.GET_CARRETO_ESPECIFIC.png)

Se muestra el JSON para modificar los productos de un carrito y que hay que introducir uno nuevo con los cambios que se quiera hacer

![PUT CARRETO ESPECIFICO](img/CARRETO/4.PUT_CARRETO.png)

Aqui esta la confirmación de que se ha modificado el carrito:

![CONFIRMACIÓN PUT CARRETO ESPECIFICO](img/CARRETO/4.1.Confirmacio_PUT_CARRETO.png)

Aqui se muestra como hacer el delete de un carrito: 

![DELETE CARRETO ESPECIFICO](img/CARRETO/5.DELETE_CARRETO.png)

Esta es la confirmación conforme se ha borrado el carrito:

![CONFIRMACIÓN DELETE CARRETO ESPECIFICO](img/CARRETO/5.1.Confirmacio_DELETE_CARRTEO.png)


//////////////////////////////////////////

CAPTURAS DE PANTALLA COMANDA:

Se muestran todas las comandas que hay, tanto las finalizadas como las que todavia no lo estan:

![GET Todas las Comandas](img/COMANDAS/1.GET_TODAS_LAS_COMANDAS.png)

Moviendome al path de no-completadas muestro todas las comandas que no estan completadas:

![GET Comandas no-completadas](img/COMANDAS/2.GET_COMANDAS_NO-COMPLETADAS.png)

Moviendome al path de completadas muestro todas las comandas que ya estan completadas:

![GET Comandas completadas](img/COMANDAS/3.GET_COMANDAS_COMPLETADAS.png)


### CATALEG
Obtenir tots els productes
![get_cat](img/Catalog/mostrar-todo.png)
Afegir un producte
![add_cat](img/Catalog/create.png)
Mostrar 1 producte
![get_one_cat](img/Catalog/one-data.png)
Actualitzar un producte
![update_cat](img/Catalog/update.png)
Eliminar producte
![delete_cat](img/Catalog/delete.png)

### PAGAMENT
Mostrar todos los usuarios con sus datos y comandas
![get_pay](img/Payment/mostrar-todo.png)
Mostrar datos especificos de un usuario
![show_pay](img/Payment/datos-user.png)
Realizar pago y limpieza de carrito
![op_pay](img/Payment/realizar-pago.png)

## KANBAN
Evidencia de kanban durante el proceso
![kanban](img/Kanban_inProgress.png)
