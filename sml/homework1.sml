(* Write a fntion is_older that takes two dates and evaluates to true or false. It evaluates to true if the first argument is a date that comes before the second argument. (If the two dates are the same, the result is false.) *)

(* (int*int*int) -> bool *)
(* produce true if the first date is earlier than the second date, else false. *)
(* Two equal dates produces false *)

fun is_older (dt1 : int* int* int, dt2 : int * int * int) =
    #1 dt1 < #1 dt2 orelse
    (#2 dt1 < #2 dt2 andalso #1 dt1 = #1 dt2) orelse
    (#3 dt1 < #3 dt1 andalso #2 dt1 = #2 dt1 andalso #1 dt1 = #1 dt1)

(* (int * int * int) list, int -> int *)
(* consumes a list of dates and a month (i.e., an int) and returns how many 
* dates in the list are in the given month *)

fun number_in_month (lod : (int * int * int) list, month : int) =
    if null lod then 0
    else
        if (#2 (hd lod)) = month
        then number_in_month(tl lod, month) + 1
        else number_in_month(tl lod, month)

(* (int * int * int) list, int list -> int *)
(* consumes a list of dates and a list of months (e.g an int list) and returns
* the number of dates in the list of dates that are in any of the months in the
* list of months *)

fun number_in_months (lod : (int * int * int) list, lom : int list) = 
    if null lom orelse null lod then 0
    else number_in_month(lod, hd lom) + number_in_months (lod, tl lom)

(* (int * int * int) list, int -> (int * int * int) list *)
(* consumes a list of dates and a month and returns a filtered list of dates
* containing only those that are in the month *)

fun dates_in_month (lod : (int * int * int) list, month : int) =
    if null lod then []
    else
        if #2 (hd lod) = month then hd lod :: dates_in_month(tl lod, month)
        else dates_in_month(tl lod, month)

(* (int * int * int) list, int list -> (int * int * int) list) *)
(* consumes a list of dates and a list of months and returns a list of dates
* that are in any of the months in the list of months *)
(* assume the list of months has no number repeated *)

fun dates_in_months(lod : (int * int * int) list, lom : int list) = 
    if null lom then []
    else dates_in_month(lod, hd lom) @ dates_in_months(lod, tl lom)

(* string list, int -> string *)
(* consumes a list of strings and an int n, and produces the string located at
* the nth position of the list *)

fun get_nth (los : string list, n : int) = 
    if n = 1 then hd los
    else get_nth (tl los, (n - 1))


(* int * int * int -> string *)
(* consumes a date and returns a string in the form January 20, 2013. *)

fun date_to_string (date : int * int * int) = 
    let
        val months = [ "January", "February", "March", "April",
                       "May", "June", "July", "August", 
                       "September", "October", "November", "December"]
    in
        get_nth(months, #2 date) 
        ^ " " ^ Int.toString (#3 date) 
        ^ ", " ^ Int.toString (#1 date)
    end

(* int, int list -> int *)
(* consumes an int called sum and a list of ints and returns an int n such that the first n
* elements of the list add to less than sum but the first n+1 elements add to >
* sum *)
(* assume entire list sums to more than sum *)

fun number_before_reaching_sum (sum : int, loi : int list) =
    let 
        fun fn_for_loi (loi0 : int list, acc : int, n : int) = 
            if acc + hd loi0 >= sum then n
            else
                fn_for_loi(tl loi0, acc + hd loi0, n+1)
    in
        fn_for_loi(loi, 0, 0)
    end

(* int -> int *)
(* consumes a day of the year int[1:365] and returns what month int[1:12] the
* day is in, ignoring leap years *)

fun what_month(day : int) = 
    let
        val days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    in
        number_before_reaching_sum(day, days_per_month) + 1
    end


(* int, int -> int list *)
(* consumes two days of the year day1[1:365] day2[1:365] and returns an int list
* [m1, m2, ..., mn] where m1 is the month of day1, m2 is the month of day1+1,
* etc.*)

fun month_range(day1 : int, day2 : int) = 
    if day1 > day2 then []
    else what_month(day1) :: month_range(day1+1, day2)


(* (int * int * int) list -> (int * int * int) option *)
(* consumes a list of dates and returns NONE if the list has no dates, else SOME
* d if the date d is the oldest date in the list *)

fun oldest (dates : (int * int * int) list) = 
    if null dates then NONE
    else
        let val tl_ans = oldest(tl dates)
        in 
            if isSome tl_ans andalso is_older(valOf tl_ans, hd dates)
                then tl_ans
                else SOME (hd dates)
        end
