;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-reader.ss" "lang")((modname fractals1) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))

(require 2htdp/image)

;; fractals-starter.rkt

;; =================================================================
;PROBLEM: 
;
;Design a function that consumes a number and produces a Sierpinski
;triangle of that size. Your function should use generative recursion.
;
;One way to draw a Sierpinski triangle is to:
;
; - start with an equilateral triangle with side length s
;     
; - inside that triangle are three more Sierpinski triangles
;     
; - and inside each of those... and so on
;; =================================================================
(define CUTOFF 2)

;; Number -> Image
;; produce a Sierpinski Triangle of the given size
(check-expect (stri CUTOFF) (triangle CUTOFF "outline" "red"))
(check-expect (stri (* CUTOFF 2))
              (overlay (triangle (* 2 CUTOFF) "outline" "red")
                       (local [(define sub (triangle CUTOFF "outline" "red"))]
                         (above sub
                                (beside sub sub)))))


(define (stri s)
  (cond [(<= s CUTOFF) 
         (triangle s "outline" "red")]
        [else
         (overlay (triangle s "outline" "red")
                  (local [(define sub (stri (/ s 2)))]
                    (above sub
                           (beside sub sub))))]))

;; =================================================================
;PROBLEM:

;Design a function to produce a Sierpinski carpet of size s.

;; A large square with 8 smaller squares along the edges and one big square in the middle
;; Each square can be divided into 9 sections; the middle section is the larger square.
;; Inside one large square of size s, place 8 squares of size s/3
;; =================================================================

;(define CUTOFF 2)

;; Number -> Image
;; produce a Sierpinski carpet of size s
(check-expect (carpet CUTOFF) (square CUTOFF "outline" "red"))
(check-expect (carpet (* CUTOFF 3)) (overlay (square (* CUTOFF 3) "outline" "red")
                                             (local [(define sub (square CUTOFF "outline" "red"))]
                                               (above (beside sub sub sub)
                                                      (beside sub (square CUTOFF "solid" "black") sub)
                                                      (beside sub sub sub)))))


;(define (carpet s) (square 0 "solid" "black")) ; stub

(define (carpet s)
  (cond [(<= s CUTOFF) (square s "outline" "red")]
        [else
         (overlay (square s "outline" "red")
                  (local [(define sub (carpet (/ s 3)))]
                    (above (beside sub sub sub)
                           (beside sub (square (/ s 3) "solid" "black") sub)
                           (beside sub sub sub))))]))