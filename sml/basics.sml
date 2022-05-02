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

(* let expressions *)
fun silly1 (z : int) = 
    let
        val x = if z > 1 then z else 34
        val y = x + z + 9
    in
        if x = y then x * 2 else y * y
    end

fun silly2 () =
    let 
        val x = 1
    in 
        (let val x = 2 in x+1 end) + (let val y = x+2 in y+1 end)
    end

(* nested functions *)
fun countup_from1 (x : int) =
    let
        fun count (from : int) =
            if from=x
            then x :: []
            else from :: count(from+1)
    in
        count(1)
    end

(* fn : int list -> int option *)
fun max1 (xs : int list) =
    if null xs then NONE
    else
        let val tl_ans = max1(tl xs)
    in if isSome tl_ans andalso valOf tl_ans > hd xs
        then tl_ans
        else SOME (hd xs)
    end

fun max2 (xs : int list) = 
    if null xs then NONE
    else let
        fun max_nonempty (xs : int list) =
            if null (tl xs) (* inner xs will always be nonempty, given local
            scope *)
            then hd xs
            else let val tl_ans = max_nonempty(tl xs)
                in
                    if hd xs > tl_ans
                    then hd xs
                    else tl_ans
                end
    in
        SOME (max_nonempty xs)
    end

(* records and compound types *)
val x1 = {first=(1+2, true andalso true), second=3+4, third=(false, 9)}

(* datatypes *)
datatype testtype = TwoInts of int * int
                    | Str of string
                    | Pizza

val a_datatype = Str "hi"
val b_datatype = Str
val c_datatype = Pizza
val d_datatype = TwoInts(1+2,3+4)
val e_datatype = a_datatype

(* f has type testtype -> int *)
fun f x_type = 
    case x_type of
         Pizza => 3
        |Str s => 8
        |TwoInts(i1,i2) => i1+i2



