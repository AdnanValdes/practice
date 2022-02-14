;; ================
;; Data definitions:

;Design a data definition to help a teacher organize their next field trip. 
;On the trip, lunch must be provided for all students. For each student, track 
;their name, their grade (from 1 to 12), and whether or not they have allergies.

(define-struct student (name grade allergies?))
;; Student is (make-student (String Number[1,12] Bool))
;; interp. (make-student name grade allergies?) is a student with
;;          name is their name
;;          grade is the grade they are in, between 1 and 12 incl.
;;          allergies? is whether they have allergies or not

(define S0 (make-student "Corey" 6 false))
(define S1 (make-student "Dylan" 2 true))

(define (fn-for-student s)
  (... (student-name s)         ; String
       (student-grade s)        ; Number[1,12]
       (student-allergies? s))) ; Bool

;; Templates used:
;; Compund rules: three fields


;; ===============
;; Functions

;To plan for the field trip, if students are in grade 6 or below, the teacher 
;is responsible for keeping track of their allergies. If a student has allergies, 
;and is in a qualifying grade, their name should be added to a special list. 
;Design a function to produce true if a student name should be added to this list.

;; Student -> Bool
;; consumes a Student and returns true if grade <= 6 and allergies? = true
(check-expect (add-tolist? (make-student "Corey" 6 true)) true)
(check-expect (add-tolist? (make-student "Corey" 6 false)) false)
(check-expect (add-tolist? (make-student "Corey" 2 true)) true)
(check-expect (add-tolist? (make-student "Corey" 2 false)) false)
(check-expect (add-tolist? (make-student "Corey" 11 false)) false)
(check-expect (add-tolist? (make-student "Corey" 7 true)) false)

#;
(define (add-tolist? s) 0)

;;<use template from Student>

(define (add-tolist? s)
  (and (>= 6 (student-grade s)) (student-allergies? s)))
