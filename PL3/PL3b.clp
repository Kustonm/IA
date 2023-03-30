;1
; (defrule regla-sumar1 
; 	(declare (salience 10)) 
; 	?a <- (elemento ?x) 
; => 
; 	(assert (elemento (+ 1 ?x)))) 

; (defrule regla-parar 
; 	(declare (salience 20)) 
; 	(elemento ?x) 
; 	(test (> ?x 9)) 
; => 
; 	(halt)) 

; (deffacts hechos-iniciales 
; 	(elemento 1)) 
; ;2
; (defrule regla-sumar-elementos 
; 	(declare (salience 10)) 
; 	?z<-(elemento ?x) 
; 	(elemento ?y) 
; => 
; 	(assert (elemento (+ ?x ?y))) 
; 	(printout t (+ ?x ?y) crlf)
;     (retract ?z))
	
; (defrule regla-parar 
; 	(declare (salience 20)) 
; 	(elemento ?x) 
; 	(test (> ?x 9)) 
; => 
; 	(halt)) 
;3
; (deftemplate elemento 
; 	(slot valor (type INTEGER))) 

; (defrule regla1 
; 	(declare (salience 10)) 
; 	(elemento (valor ?x)) 
; => 
; 	(assert (valor ?x))) 
	
; (defrule regla2 
; 	(declare (salience 5)) 
; 	?a <- (valor ?x) 
; 	(valor ?y) 
; 	(test (< ?x ?y)) 
; => 
; 	(retract ?a)) 

; (defrule regla3 
; 	(declare (salience 1)) 
; 	?a <- (valor ?x) 
; => 
; 	(printout t "Resultado: valor " ?x crlf) 
; 	(retract ?a)) 

; (deffacts hechos-iniciales 
; 	(elemento (valor 1)) 
; 	(elemento (valor 8)) 
; 	(elemento (valor 5))) 
;4
; (defrule R1 
; 	(declare (salience 15)) 
; 	?a <- (numero ?x ?u) 
; 	?b <- (numero ?y ?v) 
; 	(test (> ?u ?v)) 
; => 
; 	(assert (numero (+ ?x ?y) (+ ?u 1))) 
; 	(retract ?b)) 

; (defrule R2 
; 	(declare (salience 5)) 
; 	?b <-(total ?x) 
; 	(test (> ?x 0)) 
; => 
; 	(assert (numero 0 1))) 

; (defrule R3 
; 	(declare (salience 5)) 
; 	?b <-(total ?x) 
; 	(test (> ?x 1)) 
; => 
; 	(assert (numero 1 2))) 

; (defrule R4 
; 	(declare (salience 20)) 
; 	(total ?a) 
; 	(numero ?x ?a) 
; => 
; 	(printout t "OK:" ?x crlf) 
; 	(halt)) 

; (defrule R5 
; 	(declare (salience 1)) 
; => 
; 	(printout t "ERROR" crlf)) 
;5

; (deftemplate persona
;   (slot nombre (type SYMBOL))
;   (slot ciudad (type SYMBOL))
; )

; (deftemplate actividad
;   (slot nombre (type SYMBOL))
;   (slot ciudad (type SYMBOL))
;   (slot duracion (type INTEGER))
; )

; (deffacts personas 
; 	(persona (nombre Juan) (ciudad Paris)) 
; 	(persona (nombre Ana) (ciudad Edimburgo))
; ) 

; (deffacts actividades 
; 	(actividad (nombre Torre_Eiffel) (ciudad Paris) (duracion 2)) 
; 	(actividad (nombre Castillo_de_Edimburgo) (ciudad Edimburgo) (duracion 5)) 
; 	(actividad (nombre Louvre) (ciudad Paris) (duracion 6)) 
; 	(actividad (nombre Montmartre) (ciudad Paris) (duracion 1)) 
; 	(actividad (nombre Royal_Mile) (ciudad Edimburgo) (duracion 3))
; ) 

; (defrule media
;   (persona (nombre ?nombre)(ciudad ?ciudad))
;  =>
;   (bind ?sumD 0)
;   (bind ?numA 0)
;   (do-for-all-facts ((?a actividad))(eq ?a:ciudad ?ciudad)
;     (if (> ?a:duracion 1) then
;       (bind ?sumD (+ ?sumD ?a:duracion))
;       (bind ?numA (+ ?numA 1))
;     )
;   )
;   (if (> ?numA 0) then
;     (bind ?med (/ ?sumD ?numA))
;     (printout t "La duracion media de las actividades de " ?nombre " fue " ?med crlf)
;   )
; )


