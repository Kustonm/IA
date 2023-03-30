;Ejercicio 1
(deffunction dentroDelRango (?a ?b)
    (while true
        (printout t "Introduzca un numero:" crlf)
        (bind ?c (read))
        (if (and (> ?c ?a) (< ?c ?b)) then
            (printout t "Esta dentro del rango" crlf)
            (return)
        ) 
    )
)
;Ejercicio 2
(deffunction mcd (?a ?b)
  (if (= ?a ?b)
    then (return ?a)
    else 
		(if (> ?a ?b)then 
			(return (mcd (- ?a ?b) ?b))
    else 
			(return (mcd ?a (- ?b ?a)))
    )
  )
)
;Ejercicio 3
(deffunction mcm (?a ?b)
    (return (/ (* ?a ?b) (mcd ?a ?b)))
)


;Ejercicio 4
;Función auxiliar para encontrar el mínimo de una lista
(deffunction find_min ($?lista)
  (bind ?min (nth$ 1 $?lista))
	(bind ?min_index 1)
  (loop-for-count (?i 2 (length$ $?lista))
      (if (< (nth$ ?i $?lista) ?min)then
        (bind ?min_index ?i)
      )
  ) 
	(return ?min_index)
)

(deffunction ascendente($?lista)
	(bind $?solution (create$))
	(while (!= (length$ $?lista) 0)
		(bind ?len (length$ $?solution))
		(bind ?min (find_min $?lista))
		(bind $?solution (insert$ $?solution (+ ?len 1) (nth$ ?min $?lista)))
		(bind $?lista (delete$ $?lista ?min ?min))
	)
	(return $?solution)
)

;Ejercicio 5
(deffunction ascendentePar ($?lista)
	(bind $?aux_list (create$))
	(progn$ (?elem $?lista)
		(if (= (mod ?elem 2) 0) then
			(bind ?len (length$ $?aux_list))
			(bind $?aux_list (insert$ $?aux_list (+ ?len 1) ?elem))
		)
	)
	
	(bind $?solution (ascendente $?aux_list))
	(return $?solution)
)

;Ejercicio 6
(deffunction diferencia (?lista1 $?lista2)
  (bind ?resultado (create$))
  (loop-for-count (?i 1 (length$ ?lista1))
		(bind ?len (length$ ?resultado))
			(bind ?elem (nth$ ?i ?lista1))
      (if (not (member$ ?elem $?lista2)) then
        (bind ?resultado (create$ ?resultado ?elem))
      )
  )
  (return ?resultado)
)

;Ejercicio 7
(deffunction concatenacion (?list1 $?list2)
    (return (create$ ?list1 $?list2))
)
;Ejercicio 8
(deffunction cartesiano(?list1 $?list2)
    (bind ?res (create$))
    (foreach ?c1 ?list1
        (foreach ?c2 ?list2
            (bind ?aux (create$ ?c1 ?c2))
            ;He probado con 'concatenacion' pero no me funcionaba
            (bind ?res (create$ ?res ?aux))
        )
    )
    (return ?res)
)

;Ejercicio 9

;Función auxiliar para darle la vuelta a un string
(deffunction delreves(?string)
	(bind ?reverse "")
	(loop-for-count (?i 1 (str-length ?string))
		(bind ?elem (sub-string ?i ?i ?string))
		(bind ?reverse (str-cat ?elem ?reverse))
	)
	(return ?reverse)
)

(deffunction es_primo (?num)
  (if (<= ?num 1) then
      (return FALSE)
	)
	(bind ?root (round (sqrt ?num)))
  (loop-for-count (?i 2 ?root)
    (if (= 0 (mod ?num ?i))then
      (return FALSE)
    )
  )
  (return TRUE)
)

(deffunction es_capicua (?num)
  (bind ?string (str-cat ?num))
  (bind ?len (str-length ?string))
  (bind ?mitad (round (/ ?len 2)))
	(bind ?mitadInf (sub-string 1 ?mitad ?string))
	(if (= (mod ?len 2) 1)then
		(bind ?mitadSup (sub-string ?mitad ?len ?string))
		else
			(bind ?mitadSup (sub-string (+ ?mitad 1) ?len ?string))
	)
	(bind ?mitadSup (delreves ?mitadSup))
	(bind ?capicua (str-compare ?mitadInf ?mitadSup))
	(if (= ?capicua 0) then
		(return TRUE)
	)
  (return FALSE)
)

(deffunction num_primos_y_capicua()
	(printout t "Introducir número: ")
	(bind ?num (read))
  (bind ?numeros (create$))
  (bind ?i 0)
  (while (< (length$ ?numeros) ?num)
      (if (and (es_primo ?i) (es_capicua ?i)) then
        (bind ?numeros (create$ ?i ?numeros))
      )
      (bind ?i (+ ?i 1))
  )
  (return ?numeros)
)

;Ejercicio 10
(deffunction esMedio(?num)
	(bind ?sumaInf 0)
	(bind ?sumaSup 0)
	(bind ?stop TRUE)
	(loop-for-count (?i 1 (- ?num 1))
		(bind ?sumaInf (+ ?sumaInf ?i))
	)
	(bind ?j (+ ?num 1))
	(while ?stop
		(bind ?sumaSup (+ ?sumaSup ?j))
		(if (= ?sumaInf ?sumaSup) then
			(return TRUE)
		)
		(if (> ?sumaSup ?sumaInf)then
			(return FALSE)
		)
		(bind ?j (+ ?j 1))
	)
)