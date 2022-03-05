;; ListOfNumber -> ListOfNumber
;; sort the numbers in lon in increasing order
(check-expect (sort empty) empty)
(check-expect (sort (list 1)) (list 1))
(check-expect (sort (list 1 2 3)) (list 1 2 3))
(check-expect (sort (list 2 1 3)) (list 1 2 3))
(check-expect (sort (list 3 2 1)) (list 1 2 3))


(define (sort lon)
  (local [(define (sort-lon lon)
              (cond [(empty? lon) empty]
                    [else
                        (insert (first lon)
                                (sort-lon (rest lon)))]))
                 
        (define (insert n lon)
                (cond [(empty? lon) (cons n empty)]
                      [else
                         (if (> (first lon) n)
                                (cons n lon)
                            (cons (first lon) (insert n (rest lon))))]))]
    (sort-lon lon)))
