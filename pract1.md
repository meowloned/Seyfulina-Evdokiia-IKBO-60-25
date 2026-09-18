# практическая 1

## Задание 1
```
grep -o '^[^:#][^:]*' passwd | sort
```

## Задание 2
```
grep -v '^#' protocols | sort -k2 -rn | head -n 5 | awk '{print $2, $1}'
```
