;Plantillas

(deftemplate maquina
    (multislot productos (type INTEGER) (cardinality 4 4)) ;Cada slot indica la candidad de un prdoucto
    (multislot precios (type FLOAT) (cardinality 4 4)) ;Los precios estan ordenados segun los productos, aka, primer numero indica el precio del primer producto
    (slot saldo (type FLOAT))
)

;Funciones 
(deffunction checkDispoPrecio (?maquina ?i) 
    (bind ?pro (fact-slot-value ?maquina productos))
    (bind ?pre (fact-slot-value ?maquina precios))
    (bind ?saldo (fact-slot-value ?maquina saldo))

    (if (= (nth$ ?i ?pro) 0) 
        then
            (return -1) ; ERROR, no hay productos disponibles
        else
            (if (> (nth$ ?i ?pro) ?saldo)
                then
                    (return -2) ;ERROR, saldo insuficinete
                else
                    (return 0)
            )
    )
)

(deffunction anadirSaldo(?maquina ?amount)
    (modify ?maquina (saldo ?amount))
)

(deffunction venderProducto (?maquina ?i)
    (bind ?pro (fact-slot-value ?maquina productos))
    (bind ?pre (fact-slot-value ?maquina precios))
    (bind ?saldo (fact-slot-value ?maquina saldo))

    (bind ?nPro (replace$ ?pro ?i ?i (- (nth$ ?i ?pro) 1)))
    (modify ?maquina (productos ?nPro) (saldo (- ?saldo (nth$ ?i ?pre))))
)

(deffunction devolverDinero (?maquina)
    (modify ?maquina (saldo 0.0))
)

;Hechos
(deffacts star-up "Maquina al inicio"
    (maquina
        (productos 0 2 3 4)
        (precios 0.9 1.2 0.5 2.3)
        (saldo 0.0)
    )
)

;Reglas
(defrule sinSaldo
    ?m <- (maquina (saldo ?s))
    (test (eq ?s 0.0))
=>
    (printout t "Binvenido! Indique la cantidad de dinero que va usar: " crlf)
    (bind ?s (float (read)))
    (if (> 0 ?s) then
        (while (> 0 ?s)
            do
                (printout t "No puedes tener un saldo negativo, inetalo de nuevo: " crlf)
                (bind ?s (float (read)))
        )
    )
    (anadirSaldo ?m ?s)
)

(defrule comprar
    ?m <- (maquina (saldo ?s))
    (test (> ?s 0.0))
=>
    (printout t "Indique que desea hacer: " crlf)
    (printout t "1. Comprar producto" crlf)
    (printout t "2. Devolver dinero" crlf)
    (bind ?aux (integer (read)))
    (if (= ?aux 1)
        then
            (printout t "Indique el numero del producto que desea comprar: " crlf)
            (bind ?i (integer (read)))
            (if (or (< ?i 1)(> ?i 4))
                then
                    (while (or (< ?i 1)(> ?i 4)) do
                        (printout t "No existe ese producto, indíquelo de nuevo" crlf)
                        (bind ?i (integer (read)))
                    )
                else
                    (bind ?act (checkDispoPrecio ?m ?i))
                    (if (neq ?act 0) 
                        then
                            (while (neq ?act 0) do
                                (if (= ?act -1)
                                    then
                                        (printout t "No hay existencias de ese producto, indique otro: " crlf)
                                        (bind ?i (integer (read)))
                                        (if (or (< ?i 1)(> ?i 4))
                                            then
                                                (while (or  (< ?i 1)(> ?i 4)) do
                                                    (printout t "No existe ese producto, indiquelo de nuevo" crlf)
                                                    (bind ?i (integer (read)))
                                                )
                                        ) 
                                        (bind ?act (checkDispoPrecio ?m ?i))
                                    else
                                        (if (= ?act -2)
                                            then
                                                (printout t "Saldo insuficiente, ¿qué desea hacer? : " crlf)
                                                (printout t "1. Añadir fondos" crlf)
                                                (printout t "2. Salir" crlf)
                                                (bind ?aux (integer (read)))
                                                (if (= ?aux 1)
                                                    then
                                                        (printout t "Indique el saldo a añadir: " crlf)
                                                        (bind ?s (float(read)))
                                                        (anadirSaldo ?m ?s)
                                                    else
                                                        (if (= ?aux 2) then
                                                            (printout t "Adiós, que tenga un buen día." crlf)
                                                            (devolverDinero ?m)
                                                            (halt)
                                                        )
                                                )
                                        )
                                )
                            )
                        else
                            (venderProducto ?m ?i)
                            (printout t "Compra realizada" crlf)
                    )
            )
        else
            (printout t "Adiós, que tenga un buen día." crlf)
            (devolverDinero ?m)
            (halt)
    )
)