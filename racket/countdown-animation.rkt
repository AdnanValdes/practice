;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname countdown-animation) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)
(require 2htdp/universe)


;PROBLEM:

;Design an animation of a simple countdown. 

;Your program should display a simple countdown, that starts at ten, and
;decreases by one each clock tick until it reaches zero, and stays there.

;To make your countdown progress at a reasonable speed, you can use the 
;rate option to on-tick. If you say, for example, 
;(on-tick advance-countdown 1) then big-bang will wait 1 second between 
;calls to advance-countdown.

;Remember to follow the HtDW recipe! Be sure to do a proper domain 
;analysis before starting to work on the code file.

;Once you are finished the simple version of the program, you can improve
;it by reseting the countdown to ten when you press the spacebar.

;; ================

;; Countdown animation

;; ================
;; Constants

; Background
(define WIDTH 600)
(define HEIGHT 400)
(define MTS (empty-scene WIDTH HEIGHT))


; Position for display
(define CTR-Y (/ HEIGHT 2))
(define CTR-X (/ WIDTH 2))


; Number styling
(define SIZE 36)
(define BLACK "black")

; Starting value
(define START 10)

;; ===============
;; Data definitions

;; Value is Number
;; interp. the value displayed on the countdown
(define C0 10) ; Countdown at start
(define C1  5) ; Countdown in middle
(define C3  0) ; End of countdown

(define (fn-for-value v)
  (... v))

;; Template rules used:
;; - atomic non-distinct: Number

;; =============
;; Functions


;; V -> V
;; start the world with (main V), where V is the starting value for countdown
;;
(define (main START)
  (big-bang START                   ; V
            (on-tick countdown 1)     ; V -> V
            (to-draw render)        ; V -> Image
            (on-key  handle-key)    ; V KeyEvent -> V
            (stop-when done)         ; V -> Boolean
            ))

;; V -> V
;; produce the next value by subtracting 1 from current V
(check-expect (countdown 10) 9)
(check-expect (countdown  1) 0)
(check-expect (countdown 100) (- 100 1))

;(define (countdown v) ...) ;stub

;<use template from Value>

(define (countdown v)
  (- v 1))

;; V -> Image
;; render an image based on current countdown value
(check-expect (render 5) (place-image (text (number->string 5) SIZE BLACK) CTR-X CTR-Y MTS))

;<use template from Value>

(define (render v) 
  (place-image (text (number->string v) SIZE BLACK) CTR-X CTR-Y MTS))

;; V KeyEvent -> V
;; reset countdown to 10 when space is pressed
(check-expect (handle-key 5 " ")  START)
(check-expect (handle-key 10 " ") START)
(check-expect (handle-key 5 "a")  5)
(check-expect (handle-key 2 "l")  2)

(define (handle-key v ke) 
  (cond [(key=? ke " ") START]
        [else v]))

;; V -> Boolean
;; shutdown program when countdown reaches 0
(check-expect (done 0) true)
(check-expect (done 1) false)

; (define (done v) true)

(define (done v)
  (equal? v 0))


