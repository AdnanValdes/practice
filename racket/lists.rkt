;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname lists) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;; ListOfNumber is one of:
;; - empty
;; - (cons Number ListOfNumber)
;; interp. a list of numbers
(define LON1 empty)
(define LON2 (cons 1 empty))
(define LON3 (cons 2 (cons 1 empty)))

#;
(define (fn-for-lon lon)
  (cond [(empty? lon) (...) ]
        [else
         (... (first lon)
              (fn-for-lon (rest lon)))]))

;; Templates used:
;; - one of: 2 cases
;; - atomic distinct: empty
;; - compound (cons Number ListOfNumbers)


;; ListOfNumber -> Boolean
;; produce true if LoN contains negative number
(check-expect (contains-negative? empty) false)
(check-expect (contains-negative? (cons 1 empty)) false)
(check-expect (contains-negative? (cons 1 (cons -4 empty))) true)
(check-expect (contains-negative? (cons -100 (cons 6 empty))) true)

#;
(define (contains-negative? los) false) ;stub

;; template from ListOfNumber

(define (contains-negative? lon)
  (cond [(empty? lon) false ]
        [else
         (if (negative? (first lon)) true
              (contains-negative? (rest lon)))]))