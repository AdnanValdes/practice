;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-abbr-reader.ss" "lang")((modname hp-tree) (read-case-sensitive #t) (teachpacks ((lib "batch-io.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "batch-io.rkt" "teachpack" "2htdp")) #f)))
;In this problem set you will represent information about descendant family 
;trees from Harry Potter and design functions that operate on those trees

;To make your task much easier we suggest two things:
;- you only need a DESCENDANT family tree
;- read through this entire problem set carefully to see what information 
;the functions below are going to need. Design your data definitions to
;only represent that information.
;- you can find all the information you need by looking at the individual 
;character pages like the one we point you to for Arthur Weasley.

(require test-engine/racket-tests)

;PROBLEM 1:
;========================================

;Design a data definition that represents a family tree from the Harry Potter 
;wiki, which contains all necessary information for the other problems.  You 
;will use this data definition throughout the rest of the homework.

(define-struct wizard (name wand patronus children))
;; Wizard is (make-ft String String String ListOfFamilyTree)
;; interp. a wizard is a person with name, a wand material, a patronus, and children
;;          If wand construction is unknown, wand is ""
;;          If patronus is unknown, patronus is ""

;; ListOfWizard is one of:
;; - empty
;; - (cons Wizard ListOfWizard)



(define (fn-for-wizard n)
  (... (wizard-name n)
       (wizard-wand n)
       (wizard-patronus n)
       (fn-for-low (wizard-children n))))

(define (fn-for-low loft)
  (cond [(empty? loft) (...)]
        [else
         (... (fn-for-wizard (first loft))
              (fn-for-low (rest loft)))])) 

;PROBLEM 2: 
;========================================

;Define a constant named ARTHUR that represents the descendant family tree for 
;Arthur Weasley. You can find all the infomation you need by starting 
;at: http://harrypotter.wikia.com/wiki/Arthur_Weasley.

;You must include all of Arthur's children and these grandchildren: Lily, 
;Victoire, Albus, James.


;Note that on the Potter wiki you will find a lot of information. But for some 
;people some of the information may be missing. Enter that information with a 
;special value of "" (the empty string) meaning it is not present. Don't forget
;this special value when writing your interp.

(define ARTHUR (make-wizard "Arthur" "" "Weasel"
                            (list (make-wizard "Bill" "" "" (list (make-wizard "Victoire"  "" "" empty)
                                                                  (make-wizard "Dominique" "" "" empty)
                                                                  (make-wizard "Louis"     "" "" empty)))
                                  (make-wizard "Charlie" "Ash" "" empty)
                                  (make-wizard "Percy" "" "" (list (make-wizard "Molly" "" "" empty)
                                                                   (make-wizard "Lucy"  "" "" empty)))
                                  (make-wizard "Fred" "" "Magpie" empty)
                                  (make-wizard "George" "" "Magpie" (list (make-wizard "Fred" "" "" empty)
                                                                          (make-wizard "Roxanne" "" "" empty)))
                                  (make-wizard "Ron" "Ash" "Jack Russell Terrier" (list (make-wizard "Rose" "" "" empty)
                                                                                       (make-wizard "Hugo" "" "" empty)))
                                  (make-wizard "Ginny" "Yew" "Horse" (list (make-wizard "James" "" "" empty)
                                                                           (make-wizard "Albus" "" "" empty)
                                                                           (make-wizard "Lily" "" "" empty))))))


;PROBLEM 3:
;========================================

;Design a function that produces a pair list (i.e. list of two-element lists)
;of every person in the tree and his or her patronus. For example, assuming 
;that HARRY is a tree representing Harry Potter and that he has no children
;(even though we know he does) the result would be: (list (list "Harry" "Stag")).

;You must use ARTHUR as one of your examples.

; Wizard -> List 
; ListOfWizard -> List
; produce a list of two-element lists with a wizard's name and ther patronus. 
(check-expect (list-patronus--low empty) empty)
(check-expect (list-patronus--wizard (make-wizard "Lily" "" "" empty)) (list (list "Lily" "")))
(check-expect (list-patronus--wizard (make-wizard "Ron" "Ash" "Jack Russell Terrier" (list (make-wizard "Rose" "" "" empty)
                                                                                          (make-wizard "Hugo" "" "" empty))))
                                     (list (list "Ron" "Jack Russell Terrier") 
                                           (list "Rose" "") 
                                           (list "Hugo" "")))
(check-expect (list-patronus--wizard ARTHUR) (list
                                               (list "Arthur" "Weasel")
                                               (list "Bill" "")
                                               (list "Victoire" "")
                                               (list "Dominique" "")
                                               (list "Louis" "")
                                               (list "Charlie" "")
                                               (list "Percy" "")
                                               (list "Molly" "")
                                               (list "Lucy" "")
                                               (list "Fred" "Magpie")
                                               (list "George" "Magpie")
                                               (list "Fred" "")
                                               (list "Roxanne" "")
                                               (list "Ron" "Jack Russell Terrier")
                                               (list "Rose" "")
                                               (list "Hugo" "")
                                               (list "Ginny" "Horse")
                                               (list "James" "")
                                               (list "Albus" "")
                                               (list "Lily" "")))
                                
;(define (list-patronus--wizard w) empty)
;(define (list-patronus--low low) empty)

; <template from Wizard and ListOfWizard
(define (list-patronus--wizard n)
  (cons (list (wizard-name n)
              (wizard-patronus n))
        (list-patronus--low (wizard-children n))))

(define (list-patronus--low loft)
  (cond [(empty? loft) empty]
        [else
         (append (list-patronus--wizard (first loft))
              (list-patronus--low (rest loft)))])) 
;PROBLEM 4:
;========================================

; Design a function that produces the names of every person in a given tree 
; whose wands are made of a given material. 

; You must use ARTHUR as one of your examples.

; String Wizard -> ListOFString or empty
; String ListOfWizard -> ListOfString or empty ???
; search a given family tree for wizards with a given wand type. Produce list of their names, false otherwise.
(check-expect (wands--low "Ash" empty) empty)
(check-expect (wands--wizard "Ash" (make-wizard "James" "" "" empty)) empty)
(check-expect (wands--wizard "Yew" (make-wizard "Ginny" "Yew" "Horse" (list (make-wizard "James" "" "" empty)
                                                                            (make-wizard "Albus" "" "" empty)
                                                                            (make-wizard "Lily" "" "" empty))))
              (list "Ginny"))
(check-expect (wands--wizard "Ash" ARTHUR)
              (list "Charlie" "Ron"))

;(define (wands--wizard t w) empty)
;(define (wands--low t low)  empty)


(define (wands--wizard t w)
  (if (string=? (wizard-wand w) t) 
       (list (wizard-name w))
       (wands--low t (wizard-children w))))

(define (wands--low t loft)
  (cond [(empty? loft) empty]
        [else
         (append (wands--wizard t (first loft))
              (wands--low t (rest loft)))])) 




(test)
