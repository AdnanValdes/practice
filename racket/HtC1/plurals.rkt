; Design a function that pluralizes a given word. Simply add "s" to the end.

; String -> String
; Append "s" to given string
; (define (pluralize s) "words")

(check-expect (pluralize "test") "tests")
(check-expect (pluralize "cat") "cats")

(define (pluralize s)
  (string-append s "s"))
