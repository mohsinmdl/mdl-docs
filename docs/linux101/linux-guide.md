

## Create file in linux

```
cat > docs/linux101/linux-guide.md
```


## Create file and directory in linux

```
mkdir docs/linux101/ && cat > docs/linux101/linux-guide.md
```


## Copy linux files 

```
cp -Rv ../simpledoc/docs/ ./
```

```
You can do this using -T option in cp.
See Man page for cp.

-T, --no-target-directory
    treat DEST as a normal file
So as per your example, following is the file structure.

$ tree test
test
|-- bar
|   |-- a
|   `-- b
`-- foo
    |-- a
    `-- b
2 directories, 4 files
You can see the clear difference when you use -v for Verbose.
When you use just -R option.

$ cp -Rv foo/ bar/
`foo/' -> `bar/foo'
`foo/b' -> `bar/foo/b'
`foo/a' -> `bar/foo/a'
 $ tree
 |-- bar
 |   |-- a
 |   |-- b
 |   `-- foo
 |       |-- a
 |       `-- b
 `-- foo
     |-- a
     `-- b
3 directories, 6 files
When you use the option -T it overwrites the contents, treating the destination like a normal file and not directory.

$ cp -TRv foo/ bar/
`foo/b' -> `bar/b'
`foo/a' -> `bar/a'

$ tree
|-- bar
|   |-- a
|   `-- b
`-- foo
    |-- a
    `-- b
2 directories, 4 files
This should solve your problem.
```