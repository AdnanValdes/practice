(* This is a comment. *)

(* variable assignments and ints *)
val x = 34
val y = 17;
val w = (x + y) + (y+2);
val z = ~1


(* division of ints and reals *)
val p = 1 div 2;
val divi = 1.0 / 2.0;



(* Conditionals *)
val abs_of_z = if z < 0 then 0 - z else z;

(* Calling a function *)
(* note that the parenthesis don't matter *)
val abs_of_z_simpler = abs z;
val abs_of_z_simpler2 = abs(z);

(* shadowing *)

val a = 10
(* a:int, a -> 10 *)
val b = a * 2
(* b -> 20 *)
val a = 5
(* a -> 5, b -> 20 *)
val c = b
(* a -> 5, b -> 20, c -> 20 *)

(* functions *)
(* Note: correct only if y>=0 *)
fun pow (x : int, y : int ) = 
    if y=0
    then 1
    else x * pow(x,y-1)

fun cube(x : int) =
    pow(x,3)

val onetwentyfive = cube 5

(* pairs and tuples *)
fun swap (pr : int*bool) = 
    (#2 pr, #1 pr)

(* (int * int) * (int * int) -> int *)
fun sum_two_parts (pr1 : int * int, pr2 : int * int) = 
    (#1 pr1) + (#2 pr1) + (#1 pr2) + (#2 pr2)

(* int * int -> (int * int) *)
fun div_mod (x : int, y : int) = 
    (x div y, x mod y)

fun sort_pair(pr : int * int) = 
    if (#1 pr) < (#2 pr)
    then pr
    else (#2 pr, #1 pr)

fun sum_list (xs : int list) = 
    if null xs
    then 0
    else (hd xs) + sum_list(tl xs)

fun list_product (xs : int list) = 
    if null xs
    then 1
    else hd xs * list_product(tl xs)

(* int -> int list *)
(* consumes a number n and produces list [n, n-1,... n-n] *)
fun countdown (x : int) = 
    if x=0
    then []
    else x :: countdown(x-1)

fun append (xs : int list, ys : int list) = 
    if null xs
    then ys
    else (hd xs) :: append ((tl xs), ys)

(* functions over pairs of lists *)
fun sum_pair_list (xs : (int * int) list) =
    if null xs
    then 0
    else #1 (hd xs) + #2 (hd xs) + sum_pair_list(tl xs)

(* consumes a list of pairs and returns a list with the first element of each pair *)
fun firsts (xs : (int * int) list) =
    if null xs then []
    else #1 (hd xs) :: (firsts (tl xs))

