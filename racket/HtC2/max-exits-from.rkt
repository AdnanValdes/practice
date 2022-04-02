;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname max-exits-from-starter) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f () #f)))

;PROBLEM:
;
;Using the following data definition, design a function that produces the room with the most exits 
;(in the case of a tie you can produce any of the rooms in the tie).

;; Data Definitions: 

(define-struct room (name exits))
;; Room is (make-room String (listof Room))
;; interp. the room's name, and list of rooms that the exits lead to

(define H1 (make-room "A" (list (make-room "B" empty))))
(define H2 
  (shared ((-0- (make-room "A" (list (make-room "B" (list -0-))))))
    -0-)) 
(define H3
  (shared ((-A- (make-room "A" (list -B-)))
           (-B- (make-room "B" (list -C-)))
           (-C- (make-room "C" (list -A-))))
    -A-))
(define H4
  (shared ((-A- (make-room "A" (list -B- -D-)))
           (-B- (make-room "B" (list -C- -E-)))
           (-C- (make-room "C" (list -B-)))
           (-D- (make-room "D" (list -E-)))
           (-E- (make-room "E" (list -F- -A-)))
           (-F- (make-room "F" (list))))
    -A-))

;; template: structural recursion, encapsulate w/ local, tail-recursive w/ worklist, 
;;           context-preserving accumulator what rooms have we already visited

(define (fn-for-house r0)
  ;; todo is (listof Room); a worklist accumulator
  ;; visited is (listof String); context preserving accumulator, names of rooms already visited
  (local [(define (fn-for-room r todo visited) 
            (if (member (room-name r) visited)
                (fn-for-lor todo visited)
                (fn-for-lor (append (room-exits r) todo)
                            (cons (room-name r) visited)))) ; (... (room-name r))
          (define (fn-for-lor todo visited)
            (cond [(empty? todo) (...)]
                  [else
                   (fn-for-room (first todo) 
                                (rest todo)
                                visited)]))]
    (fn-for-room r0 empty empty))) 

;; =============================================================================================
;; Functions:
;; =============================================================================================

;; Room -> Room
;; produce room with most exits
(check-expect (max-exits-from H1) H1)
(check-expect (max-exits-from H2) H2)
(check-expect (max-exits-from (shared ((-A- (make-room "A" (list -B-)))
                                       (-B- (make-room "B" (list -C- -A-)))
                                       (-C- (make-room "C" (list -A-))))
                                -A-)) 
              (shared ((-A- (make-room "A" (list -B-)))
                       (-B- (make-room "B" (list -C- -A-)))
                       (-C- (make-room "C" (list -A-))))
                -B-))

; (define (max-exits-from r0) r0)

(define (max-exits-from r0)
  ;; todo is (listof Room); a worklist accumulator
  ;; visited is (listof String); context preserving accumulator, names of rooms already visited
  ;; rsf is Room ; name of room with most exits seen so far
  (local [(define (fn-for-room r todo visited rsf) 
            (if (member (room-name r) visited)
                (fn-for-lor todo visited rsf)
                (fn-for-lor (append (room-exits r) todo)
                            (cons (room-name r) visited)
                            (check-exits r rsf)))) ; (... (room-name r))
          (define (fn-for-lor todo visited rsf)
            (cond [(empty? todo) rsf]
                  [else
                   (fn-for-room (first todo) 
                                (rest todo)
                                visited
                                rsf)]))
          (define (check-exits r rsf)
            (if (>= (length (room-exits rsf)) (length (room-exits r)))
                rsf
                r))]
    (fn-for-room r0 empty empty r0))) 