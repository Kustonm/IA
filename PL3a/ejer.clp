(deffunction dentroDelRango (?a ?b)
    (bind ?c (read))
    (if (integerp ?c) then
        (while ((< ?c ?a) and (> ?c ?b))
            (printout "Introduze un numero")
            (bind ?c (read))
        )
    else 
        (printout "Introduze un numero")
        (bind ?c (read))
    )

)