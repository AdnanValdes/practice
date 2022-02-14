;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname is_larger) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;; Design a function that consumes two images and produces true if the first image is larger than the second

;; Img, Img -> Bool
;; Checks image dimensions and returns true if first image is larger than second on any dimension

(require 2htdp/image)

(define img1 (rectangle 30 20 "solid" "red"))
(define img2 (rectangle 20 30 "solid" "blue"))

(check-expect (is_larger? img1 img2) true)
(check-expect (is_larger? img2 img1) true)
(check-expect (is_larger? img1 img1) false)

(define (is_larger? img1 img2)
  (or (> (image-height img1) (image-height img2)) (> (image-width img1) (image-width img2))
  ))