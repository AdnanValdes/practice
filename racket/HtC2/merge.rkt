;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-abbr-reader.ss" "lang")((modname merge) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
; Problem:

; Design the function merge. It consumes two lists of numbers, which it assumes are
; each sorted in ascending order. It produces a single list of all the numbers,
; also sorted in ascending order.
;
; Your solution should explicitly show the cross product of type comments table,
; filled in with the values in each case. Your final function should have a cond
; with 3 cases. You can do this simplification using the cross product table by
; recognizing that there are subtly equal answers.
;
; Hint: Think carefully about the values of both lists. You might see a way to
; change a cell content so that 2 cells have the same value.

;; ListOfNumber is one of:
;; - empty
;; - (cons Number ListOfNumber)
;; interpt. a sorted list of numbers

(define L1 (list 1 2 3))
(define L2 (list 4 5 6))
(define L3 (list 10 20 30))
(define L4 (list 20 25 30 35))

(define (fn-for-lon lon)
  (cond [(empty? lon) (...)]
        [else
         (... (first lon)
              (fn-for-lon (rest lon)))]))

;; Functions

;; ListOfNumber ListOfNumber -> ListOfNumber
;; produce a list of all numbers sorted in ascending order
(check-expect (merge empty empty) empty)
(check-expect (merge empty (list 1 2 3)) (list 1 2 3))
(check-expect (merge (list 4 8 12) empty) (list 4 8 12))
(check-expect (merge (list 1 2 3) (list 4 5 6)) (list 1 2 3 4 5 6))
(check-expect (merge (list 4 8 12) (list 1 2 3)) (list 1 2 3 4 8 12))
(check-expect (merge (list 1) (list 2 3)) (list 1 2 3))

; (define (merge lsta lstb) empty)

(define (merge lsta lstb)
  (cond [(empty? lsta) lstb]
        [(empty? lstb) lsta]
        [else
         (if (<= (first lsta) (first lstb))
             (cons (first lsta)
                   (merge (rest lsta) lstb))
             (cons (first lstb)
                   (merge lsta (rest lstb))))]))
