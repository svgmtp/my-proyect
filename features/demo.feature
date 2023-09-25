Feature: showing off behave

 Scenario: hacer simple alert
   Given acceder a la pagina
   When pulsa en jsalert
   And acepta alert
   Then se muestra el resultado
