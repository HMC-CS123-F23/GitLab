# Quiz questions

This is only a "quiz" in the loosest sense that it's asking questions whose
answers will be part of your grade. Please use *any resources you want*, as
long as you list those resources (e.g. peers, websites, etc.)

## Navigating logs

1. What is the SHA for the last commit made by Prof. Xanda on the branch
xanda_0000_movie_processing?
(For this and future questions, the first 5 characters is plenty - neither
Git nor I need the whole SHA.)
Answer: 9b2571f9

2. What is the SHA for the last commit associated with line 9 of this file?
Answer: b2ed3

3. What did line 12 of this file say in commit d1d83?
Answer: 2. I should really finish writing this.

4. What changed between commit e474c and 82045?
Answer: The following changes to the code occured:
```
-    gross_sort = lambda x : x["Gross"]
+    gross_sort = lambda x : int(x["Gross"])
     rows.sort(key=gross_sort)
-    top_five = rows[:-5:-1]
+    top_five = rows[:-6:-1]
```"


## Predicting merges

Assume at the start of each of these three questions that your
branch for switching to a top-10 list was called `top_ten`
and your branch generalizing to any number of movies was called `top_N`.
Predict the behavior of these three possible operations - you don't
have to provide a full `diff` but you should describe at a high level
what changes would happen.

These questions are supposed to be separate paths, not cumulative;
for example, you should *not* assume that the operations of 5 were run
before 6. When testing outcomes later in the lab, you should make sure to
revert back to the state of the branch before you started these questions.

5. What do you think would happen if you ran the following commands?
What branches would change, and how?
```
git checkout test
git merge top_N
```
Answer: This sequence of commands indicate the we will first switch to the `test` branch. Then, we will merge the `top_N` branch into it meaning that the `test` branch would be updated with any change from the `top_N` branch that aren't already on `test`

6. What do you think would happen if you ran the following commands?
What branches would change, and how?
```
git checkout top_ten
git merge test
```
Answer: This sequence of commands indicate the we will first switch to the `top_ten` branch. Then, we will merge the `test` branch into it meaning that the `test` branch would be updated with any change from the `top_N` branch that aren't already on `test`

7. What do you think would happen if you ran the following commands?
What branches would change, and how?
```
git checkout test
git rebase top_ten
git rebase top_N
```
Answer: This sequence of commands indicate the we will first switch to the `test` branch. Then, we will replay the change that were made on the `test` branch on top of `top_ten` meaning that we will be essentially rewriting the history of the `test` branch such that it would seem as if we just branch off from the latest version of `top_ten` and made our changes from there. Similary, we do the same with the `top_N` branch meaning that we will replay the changes taht were made on the `test` branch (including the ones rebased from `top_ten`) on top of `top_N`