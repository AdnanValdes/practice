;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname define-natural) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;; NATURAL is one of:
;; - empty
;; - (cons "!" NATURAL)
;; interp. a natural number, the number of "!" in the list is the number
(define N0 empty)         ;0
(define N1 (cons "!" N0)) ;1
(define N2 (cons "!" N1)) ;2
(define N3 (cons "!" N2)) ;...
(define N4 (cons "!" N3)) 
(define N5 (cons "!" N4)) 
(define N6 (cons "!" N5)) 
(define N7 (cons "!" N6)) 
(define N8 (cons "!" N7)) 
(define N9 (cons "!" N8))

;; These are the primitives that operate NATURAL:
(define (ZERO? n) (empty? n))  ; Any         -> Boolean
(define (ADD1 n) (cons "!" n)) ; NATURAL     -> NATURAL
(define (SUB1 n) (rest n))     ; NATURAL[>0] -> NATURAL

(define (fn-for-NATURAL n)
	(cond [(ZERO? n) (...)]
		  [else
			  (... n
				  (fn-for-NATURAL (SUB1 n)))]))

;; NATURAL NATURAL -> NATURAL
;; produce a + b
(check-expect (ADD N2 N0) N2)
(check-expect (ADD N0 N3) N3)
(check-expect (ADD N3 N4) N7)

;(define (ADD a b) N0) ; stub


(define (ADD a b)
	(cond [(ZERO? b) a]
		  [else
			(ADD (ADD1 a) (SUB1 b))]))

;; NATURAL NATURAL -> NATURAL
;; produce a - b
(check-expect (SUB N3 N0) N3)
(check-expect (SUB N4 N1) N3)
(check-expect (SUB N8 N5) N3)

#;
(define (SUB a b) N0)

(define (SUB a b)
	(cond [(ZERO? b) a]
		  [else
			  (SUB (SUB1 a) (SUB1 b))]))


