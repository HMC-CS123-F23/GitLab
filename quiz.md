# Quiz questions

This is only a "quiz" in the loosest sense that it's asking questions whose
answers will be part of your grade. Please use *any resources you want*, as
long as you list those resources (e.g. peers, websites, etc.)

## Navigating logs

1. What is the SHA for the last commit made by Prof. Xanda on the branch
xanda_0000_movie_processing?
(For this and future questions, the first 5 characters is plenty - neither
Git nor I need the whole SHA.)

2. What is the SHA for the last commit associated with line 9 of this file?

3. What did line 12 of this file say in commit d1d83?

4. What changed between commit e474c and 82045?

## Predicting merges

Suppose that your branch for switching to a top-10 list was called `top_ten`
and your branch generalizing to any number of movies was called `top_N`.

5. What do you think would happen if you ran the following commands?
```
git checkout dev
git merge top_N
```

6. What do you think would happen if you ran the following commands?
```
git checkout top_ten
git merge dev
```

7. What do you think would happen if you ran the following commands?
```
git checkout dev
git rebase top_ten
git rebase top_N
```
