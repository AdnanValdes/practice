;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname grades) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;; As part of designing a system to keep track of students, you are asked to design a data
;; definition to represent the letter grade in a course, which is one of A, B, or C.

;; LetterGrade is one of:
;; - "A"
;; - "B"
;; - "C"
;; interp. the letter grade

(define (fn-for-letter-grade lg)
 (cond[(string=? lg "A") (...) ]
      [(string=? lg "B") (...) ]
      [(string=? lg "C") (...) ])
  )

;; Templates used:
;; - one of: 3 cases
;; - atomic distinct: "A"
;; - atomic distinct: "B"
;; - atomic distinct: "C"