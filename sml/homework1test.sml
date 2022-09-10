(* Homework1 Simple Test *)
(* These are basic test cases. Passing these tests does not guarantee that your code will pass the actual homework grader *)
(* To run the test, add a new line to the top of this file: use "homeworkname.sml"; *)
(* All the tests should evaluate to true. For example, the REPL should say: val test1 = true : bool *)
use "homework1.sml";

val test1  = is_older ((1,2,3),(2,3,4)) = true
val test1_1 = is_older ((4,5,6), (2,8,31)) = false
val test1_2 = is_older ((5,5,5), (6,1,1)) = true

val test2 = number_in_month ([(2012,2,28), (2013,12,1)], 2) = 1
val test2_1 = number_in_month ([], 1) = 0
val test2_2 = number_in_month ([(2000, 2, 29), (200, 2, 21), (4000, 1, 29), (4000, 1, 29)], 2) = 2

val test3 = number_in_months ([(2012,2,28),(2013,12,1),(2011,3,31),(2011,4,28)],[2,3,4]) = 3
val test3_0 = number_in_months ([],[2,3,4]) = 0
val test3_1 = number_in_months ([(2012,2,28),(2013,12,1),(2011,3,31),(2011,4,28)],[]) = 0
val test3_2 = number_in_months ([(2012,2,28)],[2]) = 1
val test3_3 = number_in_months ([(2012,2,28),(2013,2,1),(2011,3,31),(2011,4,28)],[2,3,4]) = 4 

val test4 = dates_in_month ([(2012,2,28),(2013,12,1)],2) = [(2012,2,28)]
val test4_0 = dates_in_month ([], 0) = []
val test4_1 = dates_in_month ([(2012,2,28),(2013,12,1), (1492,2,1)],2) = [(2012,2,28), (1492,2,1)]

val test5 = dates_in_months ([(2012,2,28),(2013,12,1),(2011,3,31),(2011,4,28)],[2,3,4]) = [(2012,2,28),(2011,3,31),(2011,4,28)]

val test6 = get_nth (["hi", "there", "how", "are", "you"], 2) = "there"
val test6_1 = get_nth (["hello"], 1) = "hello"
val test6_2 = get_nth (["hello", "meow"], 2) = "meow"
val test6_3 = get_nth (["hello", "meow"], 1) = "hello"


val test7 = date_to_string (2013, 6, 1) = "June 1, 2013"

val test8 = number_before_reaching_sum (10, [1,2,3,4,5]) = 3

val test9 = what_month 70 = 3

val test10 = month_range (31, 34) = [1,2,2,2]

val test11 = oldest([(2012,2,28),(2011,3,31),(2011,4,28)]) = SOME (2011,3,31)
