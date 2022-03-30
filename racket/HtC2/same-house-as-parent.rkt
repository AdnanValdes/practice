;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname same-house-as-parent) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))

;; same-house-as-parent-v1.rkt
(require test-engine/racket-tests)
;; =========================================================================
;PROBLEM:
;
;In the Harry Potter movies, it is very important which of the four houses a
;wizard is placed in when they are at Hogwarts. This is so important that in 
;most families multiple generations of wizards are all placed in the same family. 
;
;Design a representation of wizard family trees that includes, for each wizard,
;their name, the house they were placed in at Hogwarts and their children. We
;encourage you to get real information for wizard families from: 
;   http://harrypotter.wikia.com/wiki/Main_Page
;
;The reason we do this is that designing programs often involves collection
;domain information from a variety of sources and representing it in the program
;as constants of some form. So this problem illustrates a fairly common scenario.
;
;That said, for reasons having to do entirely with making things fit on the
;screen in later videos, we are going to use the following wizard family tree,
;in which wizards and houses both have 1 letter names. (Sigh)
;; =========================================================================

(define-struct wizard (name house children))
;; Wizard is (make-wizard String String ListOfWizard)
;; interp. a wizard is a person with name, a house, and children
;;         House is:
;;         - G for Gryffindor
;;         - S for Slytherin
;;         - R for Ravenclaw
;;         - H for Hufflepuff

(define Wa (make-wizard "A" "S" empty))
(define Wb (make-wizard "B" "G" empty))
(define Wc (make-wizard "C" "R" empty))
(define Wd (make-wizard "D" "H" empty))
(define We (make-wizard "E" "R" empty))
(define Wf (make-wizard "F" "R" (list Wb)))
(define Wg (make-wizard "G" "S" (list Wa)))
(define Wh (make-wizard "H" "S" (list Wc Wd)))
(define Wi (make-wizard "I" "H" empty))
(define Wj (make-wizard "J" "R" (list We Wf Wg)))
(define Wk (make-wizard "K" "G" (list Wh Wi Wj)))

#;
(define (fn-for-wizard w)
  (local [(define (fn-for-wizard w)
            (... (wizard-name w)
                 (wizard-house w)
                 (fn-for-low (wizard-children w))))
          (define (fn-for-low low)
            (cond [(empty? low) (...)]
                  [else
                   (... (fn-for-wizard (first low))
                        (fn-for-low (rest low)))]))]
    (fn-for-wizard w)))


;; =========================================================================
;PROBLEM:
;
;Design a function that consumes a wizard and produces the names of every 
;wizard in the tree that was placed in the same house as their immediate
;parent. 
;; =========================================================================
;; Wizard -> ListOfWizard
;; produce a list of wizards who are in the same house as their immediate parent
(check-expect (same-house-as-parent We) empty)
(check-expect (same-house-as-parent Wh) empty)
(check-expect (same-house-as-parent Wg) (list "A"))
(check-expect (same-house-as-parent Wk) (list "E" "F" "A"))

;template from Wizard plus lost context accumulator
#;
(define (same-house-as-parent w)
  ;; parent-house is String; the name of this wizard's immediate parent's house
  ;; (same-house-as-parent Wk)
  ;; (fn-for-wizard Wk  "")???)
  ;; (fn-for-wizard Wh "G") ???)
  ;; (fn-for-wizard Wc "S") ???)
  ;; (fn-for-wizard Wd "S") ???)
  ;; (fn-for-wizard Wi "G") ???)
  ;; (fn-for-wizard Wj "R") ???)
  (local [(define (fn-for-wizard w parent-house)
            (if (string=? parent-house (wizard-house w))
                (cons (wizard-name w) (fn-for-low (wizard-children w) (wizard-house w)))
                (fn-for-low (wizard-children w)
                            (wizard-house w))))

          (define (fn-for-low low parent-house)
            (cond [(empty? low) empty]
                  [else
                   (append 
                    (fn-for-wizard (first low)
                                   parent-house)
                    (fn-for-low (rest low)
                                parent-house))]))]
    (fn-for-wizard w "")))

;; =========================================================================
;PROBLEM:
;
;Design a new function definition for same-house-as-parent that is tail 
;recursive. You will need a worklist accumulator.
;; =========================================================================

; template from Wizard, plus worklist accumulator
; the worklist needs to include the parent for each wizard in the worklist
; instead of just adding wizards, we must add (wizard, parent house)


(define (fn-for-wizard w)
  (local [(define (fn-for-wizard w)
            (... (wizard-name w)
                 (wizard-house w)
                 (fn-for-low (wizard-children w))))
          (define (fn-for-low low)
            (cond [(empty? low) (...)]
                  [else
                   (... (fn-for-wizard (first low))
                        (fn-for-low (rest low)))]))]
    (fn-for-wizard w)))

;; =========================================================================
;PROBLEM:
;
;Design a function that consumes a wizard and produces the number of wizards 
;in that tree (including the root). Your function should be tail recursive.
;; =========================================================================
;; Wizard -> Natural
;; produces the total number of wizards in given tree including root
(check-expect (count-wizards We)  1)
(check-expect (count-wizards Wh) 3)


;(define (count-wizards w) 0)


;; Works, but not tail recursive.
#;
(define (count-wizards w)
  ;; acc Natural; the number of wizards in the tree so far
  ;; (count-wizards Wh)
  ;; (fn-for-wizard Wh 0)   1) 
  ;; (fn-for-wizard Wc 1)   2) 
  ;; (fn-for-wizard Wd 2)   3)

  (local [(define (fn-for-wizard w acc)
            (fn-for-low (wizard-children w)
                        (+ 1 acc)))
          (define (fn-for-low low acc)
            (cond [(empty? low) acc]
                  [else
                   ;(... acc 
                   ;     (fn-for-wizard (first low) 
                   ;                        acc)
                   (fn-for-low (rest low)
                               (fn-for-wizard (first low) acc))]))] ; this function not in tail pos.
    (fn-for-wizard w 0)))

(define (count-wizards w)
  ;; acc Natural; the number of wizards in the tree so far
  ;; (count-wizards Wh)
  ;; (fn-for-wizard Wh 0)   1) 
  ;; (fn-for-wizard Wc 1)   2) 
  ;; (fn-for-wizard Wd 2)   3)

  (local [(define (fn-for-wizard w todo acc) ; todo is (listof Wizard) ;  wizards remaining to see
            (fn-for-low (append (wizard-children w) todo)
                        (+ 1 acc)))
          (define (fn-for-low todo acc)
            (cond [(empty? todo) acc]
                  [else
                      (fn-for-wizard (first todo) (rest todo) acc)]))]
    (fn-for-wizard w empty 0)))



























(test)
