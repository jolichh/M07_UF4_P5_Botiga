# M07_UF4_P5_Botiga

//CARRETO

Introducir datos:	(Se crea un carrito y dentro de las llaves le indicas los IDs de los Productos 


{
    "productos": [
        {
            "producto_id": 1,
            "cantidad": 2
        },
        {
            "producto_id": 3,
            "cantidad": 1
        }
    ]
}



Modificar Datos:

http://127.0.0.1:8000/carreto/4/	->Le paso la ID del carrito por el enlace

{
    "productos": [
        {
            "producto_id": 1,
            "cantidad": 2
        },
        {
            "producto_id": 3,
            "cantidad": 1
        }
    ]
}



/////////////////////////

-Cataleg_Categoria
-----------------------

INSERT INTO public.cataleg_categoria(name)
VALUES ('electronica');

INSERT INTO public.cataleg_categoria(name)
VALUES ('ropa');


INSERT INTO public.cataleg_categoria(name)
VALUES ('muebles');


-Cataleg_Producte
-----------------------

INSERT INTO  public.cataleg_producte( name, description, price, valoration, quantity, categoria_id)
VALUES ('cama','Buena Buena',10.99,5,100,3);


INSERT INTO  public.cataleg_producte( name, description, price, valoration, quantity, categoria_id)
VALUES ('teclado','Buena Barato',12.99,4,200,1);


INSERT INTO  public.cataleg_producte( name, description, price, valoration, quantity, categoria_id)
VALUES ('camiseta','Fea Barato',20.99,4,150,2);



-Carreto_carrito
--------------------
INSERT INTO public.carreto_carrito(compra_realizada)
VALUES(false)


-Carreto_producteencarrito
