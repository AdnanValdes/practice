;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname movie) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))


; ===============
; Data definitions:

;PROBLEM A:

;Design a data definition to represent a movie, including  
;title, budget, and year released.

;To help you to create some examples, find some interesting movie facts below: 
;"Titanic" - budget: 200000000 released: 1997
;"Avatar" - budget: 237000000 released: 2009
;"The Avengers" - budget: 220000000 released: 2012

;However, feel free to resarch more on your own!

(define-struct actor (fn ln))
;; Actor is (make-actor (fn ln))
;; interp. (make-actor (fn ln)) is a movie actor with
;;         fn is the first name
;;         ln is the last name

(define A0 (make-actor "Leonardo" "DiCaprio"))
(define A1 (make-actor "Stephen" "Fry"))

(define (fn-for-actor a)
    (... (actor-fn p) ; String
         (actor-ln p) ; String
    ))

;; Template rules used:
;; - Compound rules: two fields

(define-struct movie (title budget released Actor))
;; Movie is (make-movie (String Natural Natural Actor))
;; interp. (make-movie title budget released lead-actor) is a movie with
;;          title is the title of the movie
;;          budget is the movie's budget in millions USD
;;          released is the movie's release year
;;          Actor is Actor lead in the movie

(define M0 (make-movie "Titanic" 200 1997 A0))
(define M1 (make-movie "Avatar" 237 2009 (make-actor "Sam" "Worthington")))

(define (fn-for-movie m)
  (... (movie-title m)                      ; String
       (movie-budget m)                     ; Natural
       (movie-released m)                   ; Natural
       (fn-for-actor (movie-Actor m))))     ; Actor

;; Template rules used:
;; - Compound rules: 4 fields
;; - Non-primitive reference: Actor


; ================

; Functions

;PROBLEM B:

;You have a list of movies you want to watch, but you like to watch your 
;rentals in chronological order. Design a function that consumes two movies 
;and produces the title of the most recently released movie.

;Note that the rule for templating a function that consumes two compound data 
;parameters is for the template to include all the selectors for both 
;parameters.

;; Movie Movie -> Movie
;; consumes two Movie objects and produces the title of the most recent one.
(check-expect (most-recent? (make-movie "Titanic" 200 1997 A0) (make-movie "Avatar" 237 2009 A1)) "Avatar")
(check-expect (most-recent? M0 M1) "Avatar")
(check-expect (most-recent? (make-movie "A" 200 2022 A0) (make-movie "B" 200 2022 A0)) "A")

#;
(define (most-recent? m1 m2) 0) ; Stub

(define (most-recent? m1 m2)
  (cond [(< (movie-released m1) (movie-released m2)) (movie-title m2)]
        [else (movie-title m1)]))
