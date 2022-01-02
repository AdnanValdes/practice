;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname area) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
; Design a function called area that consumes the length of one side of a square
; and produces the area of the square

;; Number -> Number
; returns the area of a square by squaring the Number
(check-expect (area 2) 4)
(check-expect (area 3.2) (sqr 3.2))

(check-expect (area2 2) 4)
(check-expect (area2 3.2) (sqr 3.2))

(define (area s)
  (sqr s))

; alternative definition
(define (area2 s)
  (* s s))
