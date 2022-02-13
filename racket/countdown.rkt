;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname countdown) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;; Design a system for controlling a NYE display. Design a data definition to represent the current state of the countdown
;; which falls into one of three categories:

;; - not yet started
;; - from 10 to 1 seconds before midnight
;; - complete (happy new year!)

;; Countdown is one of:
;; - Natural[10, 1]
;; - false
;; - "complete"
;; interp.
;;    Natural is seconds left until NYE.
;;    false is countdown has not started
;;    "complete" is the countdown has finished

(define CD1 false)
(define CD2 3)
(define CD3 "complete")

#;
(define (fn-for-countdown cd)
 (cond [(boolean? cd)   (... cd)]
       [(and (number? cd) (<= 1 cd) (<= cd 10) (... cd))] ; Add number to guard against this line being called when `cd` == "complete"
       [(string=? cd "complete") (...)]))

#; ; Alternative definition. Note that the second case is the only situation where countdown is number.
(define (fn-for-countdown cd)
 (cond [(boolean? cd)   (... cd)]
       [(number? cd) (... cd)]
       [(string=? cd "complete") (...)]))

;; Templates used:
;; - One of itemization with: 3 cases
;; - Atomic non-distinct: bool false
;; - Atomic non-distinct: interval Natural[10, 1]
;; - Atomic distinct: String "complete"