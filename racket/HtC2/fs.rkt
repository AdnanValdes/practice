;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-abbr-reader.ss" "lang")((modname fs) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)

;; fs-starter.rkt (type comments and examples)

;; Data definitions:

(define-struct elt (name data subs))
;; Element is (make-elt String Integer ListOfElement)
;; interp. An element in the file system, with name, and EITHER data or subs.
;;         If data is 0, then subs is considered to be list of sub elements.
;;         If data is not 0, then subs is ignored.

;; ListOfElement is one of:
;;  - empty
;;  - (cons Element ListOfElement)
;; interp. A list of file system Elements

(define F1 (make-elt "F1" 1 empty))
(define F2 (make-elt "F2" 2 empty))
(define F3 (make-elt "F3" 3 empty))
(define D4 (make-elt "D4" 0 (list F1 F2)))
(define D5 (make-elt "D5" 0 (list F3)))
(define D6 (make-elt "D6" 0 (list D4 D5)))

(define (fn-for-element e)
  (... (elt-name e)                  ;String
       (elt-data e)                 ;Integer
       (fn-for-loe (elt-subs e))))  ;ListOfElement

(define (fn-for-loe loe)
  (cond [(empty? loe) (...)]
        [else
         (... (fn-for-element (first loe))
              (fn-for-loe (rest loe)))]))

;; Functions:

; *Design a function that consumes Element and produces the sum of all the file data in the tree*

;; Element -> Integer
;; ListOfElement -> Integer
; produce sum of all data in element (and its subs)
(check-expect (sum-data--element F1) 1)
(check-expect (sum-data--loe empty)  0)
(check-expect (sum-data--element D5) 3)
(check-expect (sum-data--element D4) (+ 1 2))
(check-expect (sum-data--element D6) (+ 1 2 3))


;(define (sum-data--element e) 0)
;(define (sum-data--loe loe)   0)


(define (sum-data--element e)
  (if (zero? (elt-data e))
      (sum-data--loe (elt-subs e))
      (elt-data e))) 


(define (sum-data--loe loe)
  (cond [(empty? loe) 0]
        [else
         (+ (sum-data--element (first loe))
            (sum-data--loe (rest loe)))]))

; *Design a function that consumes Element and produces a list of the names of all the elements in 
; the tree.*

;; Element -> ListOfString
;; ListOfElement -> ListOfString
;; produce list of names of all elements in tree
(check-expect (list-names--element F1) (list "F1"))
(check-expect (list-names--loe  empty) empty)
(check-expect (list-names--element D5) (list "D5" "F3"))
(check-expect (list-names--element D4) (list "D4" "F1" "F2"))
(check-expect (list-names--loe (list D4 D5)) (append (list "D4" "F1" "F2") (list "D5" "F3")))
(check-expect (list-names--element D6) (list "D6" "D4" "F1" "F2" "D5" "F3"))

;(define (list-names--element e) empty)
;(define (list-names--loe   loe) empty)


(define (list-names--element e)
  (cons (elt-name e)                
        (list-names--loe (elt-subs e)))) 

(define (list-names--loe loe)
  (cond [(empty? loe) empty]
        [else
         (append (list-names--element (first loe))
               (list-names--loe (rest loe)))]))
