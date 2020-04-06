Require Import Coq.Arith.EqNat.

(*Models becomedebater*)
Definition twoQueue(p:nat * nat)(x:nat) : nat * nat :=
match Nat.eqb (snd p) x with
  |true => p
  |false => (snd p, x)
end.

(*Debater 2 is always the most recent*)
Theorem twoQproperty1 : forall p:nat * nat, forall x:nat, (snd (twoQueue p x)) = x.
intros.
destruct p as [a b].
unfold twoQueue.
destruct (Nat.eqb (snd (a, b)) x) eqn:E.
simpl in *.
apply (beq_nat_true _ _ E).
cbv; easy.
Defined.

(*The two most recent debators are always among the current debaters.*)
Theorem twoQproperty2 : forall p:nat * nat, forall x y:nat, (((fst (twoQueue (twoQueue p x) y)) = x) + ((snd (twoQueue (twoQueue p x) y)) = x)) * (((fst (twoQueue (twoQueue p x) y)) = y) + ((snd (twoQueue (twoQueue p x) y)) = y)).
Proof with simpl in *; try easy.
intros.
destruct p as [a b].
unfold twoQueue...
destruct (Nat.eqb b x) eqn:Ebx...
all: destruct (Nat.eqb b y) eqn:Eby...
3: destruct (Nat.eqb x y) eqn:Exy...
5: destruct (Nat.eqb x y) eqn:Exy...
all: split...
all: try ((constructor 1; easy) + (constructor 2; easy)).
all: try (rewrite (beq_nat_true _ _ Ebx)).
all: try (rewrite (beq_nat_true _ _ Eby)).
all: try (rewrite (beq_nat_true _ _ Exy)).
all: try ((constructor 1; easy) + (constructor 2; easy)).
constructor 2.
transitivity b.
1: try (rewrite (beq_nat_true _ _ Ebx)).
trivial.
try (rewrite <- (beq_nat_true _ _ Eby)).
trivial.
Defined.

(*If the debaters weren't the same, they cannot become the same later.*)
Theorem twoQproperty3 : forall p:nat * nat, forall x y:nat, (Nat.eqb (fst p) (snd p) = false) -> (Nat.eqb (fst (twoQueue p x)) (snd (twoQueue p x)) = false).
Proof with simpl in *; try easy.
intros.
destruct p as [a b].
unfold twoQueue...
destruct (Nat.eqb b x) eqn:Ebx...
Defined.
