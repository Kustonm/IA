;PLANTILLAS
(deffacts 
)


(deftemplate partida
    ;(multislot jugadores (type STRING)(cardinality 2 2)) ; (Nombre, tipoF, Puntos) Igual no hace falta
    (multislot dados (type INTEGER)(cardinality 2 2))
    (slot turno (type SYMBOL)(allowed-values W B)) ;Mejor que esto determine al jugador
    (multislot punuacion (type INTEGER)(cardinality 2 2)) ;El primer numero es la puntuacion de W y el segundo de B
)

;HECHOS
(deffacts inicioPartida
    (partida
        (dados 0 0)
        (fichas
            (0 2 0) (11 5 0) (16 3 0) (18 5 0)  ; fichas blancas
            (5 0 5) (7 0 3) (12 0 5) (23 0 2); fichas negras
        )
        (puntuacion 0 0)
    )
)
;REGLAS
(defrule winW
   (fichas (24 15 ?))
=>
    (printout "Gana las fichas blanca." crlf)
)

(defrule winB
   (fichas (24 ? 15))
=>
    (printout "Gana las fichas negras." crlf)
)

(defrule tiradaInicial
    ?p0 <- (partida (dados 0 0))
=>
    (printout t "Re tiran los dados para decidir quien empieza..." crlf)
    (tirarDados ?p$dados)
    (if (> (nth$ 1 ?p$dados) (nth$ 1 ?p$dados)) then
        (modify ?p (turno B))
        (printout "Empiezan las fichas negras (B)." crlf)
    else 
        (modify ?p (turno W))
        (printout "Empiezan las fichas blancas (W)." crlf)
    )
)

(defrule cambiarT
    ?p <- (partida (turno ?turno))
=>
    (modify ?p (turno (if (eq ?turno W) then Belse W)))
)
;FUNCIONES
(deffunction tirarDados(?partida$dados) 
    (foreach (?d ?partida$dados)
        (modify ?d (random 1 6))
    )
)


(deffunction checkLegalMove(?casillaO ?numM ?partida)
    (foreach (?v ?casillaO)
        (bind ?idO (nth$ 1 ?v))
        (bind ?nWO (nth$ 2 ?v))
        (bind ?nB= (nth$ 2 ?v))
    )
    ( if (eq (fact-slot-value ?partida turno) W) then 
        (bind ?casillaD (find (+ ?idO ?numM)?fichas))
        else (bind ?casillaD (find (- ?idO ?numM)?fichas))
    )
    (foreach (?v ?casillaO)
        (bind ?idD (nth$ 1 ?v))
        (bind ?nWD (nth$ 2 ?v))
        (bind ?nBD (nth$ 2 ?v))
    )

    (if (eq (fact-slot-value ?partida turno) W) then 
    ;turno blanco
        (if (> ?nBD 1) then 

        )
    [else ()])
)


