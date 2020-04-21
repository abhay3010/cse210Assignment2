load harness

@test "mytest-1" {
  check 'x := true ?  1 : 0' '{x → 1}'
}

@test "mytest-2" {
  check 'x := 1 * 9 ; x := 5 < x ?  2 - 2 : 9' '{x → 0}'
}

@test "mytest-3" {
  check 'x :=  x = 0 ∧ y < 4 ? 1  : 3' '{x → 1}'
}

@test "mytest-4" {
  check 'x :=  x = 0 ∧ 4 < 4 ? 1 : 3' '{x → 3}'
}

@test "mytest-5" {
  check 'x := 0 < x ∧ 4 = 4 ? 1 : 3' '{x → 3}'
}

@test "mytest-6" {
  check 'x := 0 < x ∧ 4 < y ? 1 : 3' '{x → 3}'
}

@test "mytest-7" {
  check 'x :=  x = 0 ∨ y < 4 ?  1 : 3' '{x → 1}'
}

@test "mytest-8" {
  check 'x := x = 0 ∨ 4 < 4 ? 1 : 3' '{x → 1}'
}

@test "mytest-9" {
  check 'x :=  0 < x ∨ 4 = 4 ? 1 : 3' '{x → 1}'
}

@test "mytest-10" {
  check 'x :=  0 < x ∨ 4 < y ? 1 : 3' '{x → 3}'
}
