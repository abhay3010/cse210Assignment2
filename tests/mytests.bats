load harness

@test "mytest-1" {
  check 'if true ∨ false then x := x+1 else skip' '⇒ x := (x+1), {}
⇒ skip, {x → 1}'
}

@test "mytest-2" {
  check 'x<5 do x := x+1' '⇒ x := (x+1); while (x<5) do { x := (x+1) }, {}
⇒ skip; while (x<5) do { x := (x+1) }, {x → 1}
⇒ while (x<5) do { x := (x+1) }, {x → 1}
⇒ x := (x+1); while (x<5) do { x := (x+1) }, {x → 1}
⇒ skip; while (x<5) do { x := (x+1) }, {x → 2}
⇒ while (x<5) do { x := (x+1) }, {x → 2}
⇒ x := (x+1); while (x<5) do { x := (x+1) }, {x → 2}
⇒ skip; while (x<5) do { x := (x+1) }, {x → 3}
⇒ while (x<5) do { x := (x+1) }, {x → 3}
⇒ x := (x+1); while (x<5) do { x := (x+1) }, {x → 3}
⇒ skip; while (x<5) do { x := (x+1) }, {x → 4}
⇒ while (x<5) do { x := (x+1) }, {x → 4}
⇒ x := (x+1); while (x<5) do { x := (x+1) }, {x → 4}
⇒ skip; while (x<5) do { x := (x+1) }, {x → 5}
⇒ while (x<5) do { x := (x+1) }, {x → 5}
⇒ skip, {x → 5}'
}

@test "mytest-3" {
  check 'while x<-5 do x := x + 1' '⇒ skip, {}
if ¬ (x<5) then y := 10 else y := -10
⇒ y := -10, {}
⇒ skip, {y → -10}'
}

@test "mytest-4" {
  check 'y := 1; x := 1; while x < 7 do { y := y * x; x := x + 1 }' '⇒ skip; x := 1; while (x<7) do { y := (y*x); x := (x+1) }, {y → 1}
⇒ x := 1; while (x<7) do { y := (y*x); x := (x+1) }, {y → 1}
⇒ skip; while (x<7) do { y := (y*x); x := (x+1) }, {x → 1, y → 1}
⇒ while (x<7) do { y := (y*x); x := (x+1) }, {x → 1, y → 1}
⇒ y := (y*x); x := (x+1); while (x<7) do { y := (y*x); x := (x+1) }, {x → 1, y → 1}
⇒ skip; x := (x+1); while (x<7) do { y := (y*x); x := (x+1) }, {x → 1, y → 1}
⇒ x := (x+1); while (x<7) do { y := (y*x); x := (x+1) }, {x → 1, y → 1}
⇒ skip; while (x<7) do { y := (y*x); x := (x+1) }, {x → 2, y → 1}
⇒ while (x<7) do { y := (y*x); x := (x+1) }, {x → 2, y → 1}
⇒ y := (y*x); x := (x+1); while (x<7) do { y := (y*x); x := (x+1) }, {x → 2, y → 1}
⇒ skip; x := (x+1); while (x<7) do { y := (y*x); x := (x+1) }, {x → 2, y → 2}
⇒ x := (x+1); while (x<7) do { y := (y*x); x := (x+1) }, {x → 2, y → 2}
⇒ skip; while (x<7) do { y := (y*x); x := (x+1) }, {x → 3, y → 2}
⇒ while (x<7) do { y := (y*x); x := (x+1) }, {x → 3, y → 2}
⇒ y := (y*x); x := (x+1); while (x<7) do { y := (y*x); x := (x+1) }, {x → 3, y → 2}
⇒ skip; x := (x+1); while (x<7) do { y := (y*x); x := (x+1) }, {x → 3, y → 6}
⇒ x := (x+1); while (x<7) do { y := (y*x); x := (x+1) }, {x → 3, y → 6}
⇒ skip; while (x<7) do { y := (y*x); x := (x+1) }, {x → 4, y → 6}
⇒ while (x<7) do { y := (y*x); x := (x+1) }, {x → 4, y → 6}
⇒ y := (y*x); x := (x+1); while (x<7) do { y := (y*x); x := (x+1) }, {x → 4, y → 6}
⇒ skip; x := (x+1); while (x<7) do { y := (y*x); x := (x+1) }, {x → 4, y → 24}
⇒ x := (x+1); while (x<7) do { y := (y*x); x := (x+1) }, {x → 4, y → 24}
⇒ skip; while (x<7) do { y := (y*x); x := (x+1) }, {x → 5, y → 24}
⇒ while (x<7) do { y := (y*x); x := (x+1) }, {x → 5, y → 24}
⇒ y := (y*x); x := (x+1); while (x<7) do { y := (y*x); x := (x+1) }, {x → 5, y → 24}
⇒ skip; x := (x+1); while (x<7) do { y := (y*x); x := (x+1) }, {x → 5, y → 120}
⇒ x := (x+1); while (x<7) do { y := (y*x); x := (x+1) }, {x → 5, y → 120}
⇒ skip; while (x<7) do { y := (y*x); x := (x+1) }, {x → 6, y → 120}
⇒ while (x<7) do { y := (y*x); x := (x+1) }, {x → 6, y → 120}
⇒ y := (y*x); x := (x+1); while (x<7) do { y := (y*x); x := (x+1) }, {x → 6, y → 120}
⇒ skip; x := (x+1); while (x<7) do { y := (y*x); x := (x+1) }, {x → 6, y → 720}
⇒ x := (x+1); while (x<7) do { y := (y*x); x := (x+1) }, {x → 6, y → 720}
⇒ skip; while (x<7) do { y := (y*x); x := (x+1) }, {x → 7, y → 720}
⇒ while (x<7) do { y := (y*x); x := (x+1) }, {x → 7, y → 720}
⇒ skip, {x → 7, y → 720}
'
}

@test "mytest-5" {
  check 'x := 10; y := 5; t := x; x := y; y := t' '⇒ skip; y := 5; t := x; x := y; y := t, {x → 10}
⇒ y := 5; t := x; x := y; y := t, {x → 10}
⇒ skip; t := x; x := y; y := t, {x → 10, y → 5}
⇒ t := x; x := y; y := t, {x → 10, y → 5}
⇒ skip; x := y; y := t, {t → 10, x → 10, y → 5}
⇒ x := y; y := t, {t → 10, x → 10, y → 5}
⇒ skip; y := t, {t → 10, x → 5, y → 5}
⇒ y := t, {t → 10, x → 5, y → 5}
⇒ skip, {t → 10, x → 5, y → 10}'
}

@test "mytest-6" {
  check 'x := 10; y := 5; t := y<x ? x : y' '⇒ skip; y := 5; t := (y<x) ? x : y, {x → 10}
⇒ y := 5; t := (y<x) ? x : y, {x → 10}
⇒ skip; t := (y<x) ? x : y, {x → 10, y → 5}
⇒ t := (y<x) ? x : y, {x → 10, y → 5}
⇒ skip, {t → 10, x → 10, y → 5}'
}
