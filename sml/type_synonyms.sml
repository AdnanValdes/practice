datatype suit = Club | Diamond | Heart | Spade

datatype rank = Jack | Queen | King | Ace | Num of int

type card = suit * rank

type name_recors = {student_num : int option,
					first       : string,
					middle      : string option,
					last        : string }

fun is_Queen_Of_Spades (c : card) = 
	#1 c = Spade andalso #2 c = Queen

val c1 : card = (Diamond, Ace)
val c2 : suit * rank = (Heart, Ace)
val c3 = (Spade, Ace)

(* We can call is_Queen_Of_Spades with any of c1, c2, c3 *)
