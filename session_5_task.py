# A = {2,4,6,8,10,12}
# B = {3,6,9,12,15}
# C = {1,4,7,10,13,16}

# # # (i) A ∪ B
# # Aub = A.union(B)
# # print(Aub)

# # # (ii) A ∩ B
# # AnB = A.intersection(B)
# # print(AnB)

# # A.intersection_update(B)
# # print(A)

# # # (iii) B ∩ A
# # B.intersection_update(A)
# # print(B)

# # # (iv) B ∪ A
# # BuA = B.union(A)
# # print(BuA)

# # (v) B ∪ C
# BuC = B.union(C)
# print(BuC)

# # (vi) Is A ∪ B = B ∪ A? - Yes

# # (vii) Is B ∩ C = B ∪ C? - No 
# B.intersection_update(C)
# print(B)

# -------------------------------------------------------------------

# 2. If
# A = {1, 3, 7, 9, 10}
# B = {2, 5, 7, 8, 9, 10}
# C = {0, 1, 3, 10}
# D = {2, 4, 6, 8, 10}
# E = {-1,-2,-3,-4,-5}
# F = {0}
# # Find:
# # (i) A ∪ B
# AuB = A.union(B)
# print(AuB)

# # # (ii) E ∪ D
# # EuD = E.union(D)
# # print(EuD)

# # # (iii) C ∪ F
# # CuF = C.union(F)
# # print(CuF)

# # # (iv) C ∪ D
# # CuD = C.union(D)
# # print(CuD)

# # # (v) B ∪ F
# # BuF = B.union(F)
# # print(BuF)

# # (vi) A ∩ B
# AnB = A.intersection(B)
# print(AnB)

# # # (vii) C ∩ D
# # C.intersection_update(D)
# # print(C)

# # # (viii) E ∩ D
# # E.intersection_update(D)
# # print(E)

# # # (ix) C ∩ F
# # C.intersection_update(F)
# # print(C)

# # # (x) B ∩ F
# # B.intersection_update(F)
# # print(B)

# # (xi) (A ∪ B) ∪ (A ∩ B)
# AuB = A.union(B)
# AnB = A.intersection(B)
# AuB.union(AnB)
# print(AuB)

# # (xii) (A ∪ B) ∩ (A ∩ B)
# AuB.intersection_update(AnB)
# print(AuB)

# 3. There are a total number of 200 students in Class XI.
# Among them, 120 students study science, 50 students mathematics,
# and 30 students study both science and mathematics.
# Find the number of students who :
# Study science but not mathematics
# Study mathematics but not science
# Study science or mathematics