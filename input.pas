program FullTest;
var
    i, j, k: integer;
    c: char;
    flag: boolean;
    arr: array [1..5] of integer;
    bArr: array [0..2] of boolean;
    chArr: array ['a'..'c'] of char;

function Max(a, b: integer): integer;
begin
    if a > b then
        Max := a
    else
        Max := b;
end;

function IsEven(n: integer): boolean;
begin
    IsEven := (n mod 2) = 0;
end;

procedure PrintPrimes(limit: integer);
var
    i, j: integer;
    isPrime: boolean;
begin
    for i := 2 to limit do
    begin
        isPrime := true;
        j := 2;
        while (j * j <= i) and isPrime do
        begin
            if i mod j = 0 then
                isPrime := false;
            Inc(j);
        end;

        if isPrime then
            WriteLn('Prime: ', i);
    end;
end;

begin
    // Тест базовых типов и операций
    c := 'A';
    flag := true;
    WriteLn('Char: ', c, ' Boolean: ', flag);

    // Тест арифметических операций
    i := 10;
    j := 3;
    WriteLn(i, ' + ', j, ' = ', i + j);
    WriteLn(i, ' - ', j, ' = ', i - j);
    WriteLn(i, ' * ', j, ' = ', i * j);
    WriteLn(i, ' / ', j, ' = ', i / j);  // Должно работать как div
    WriteLn(i, ' div ', j, ' = ', i div j);
    WriteLn(i, ' mod ', j, ' = ', i mod j);

    // Тест операций сравнения
    WriteLn(i, ' > ', j, ' = ', i > j);
    WriteLn(i, ' < ', j, ' = ', i < j);
    WriteLn(i, ' = ', j, ' = ', i = j);
    WriteLn(i, ' <> ', j, ' = ', i <> j);
    WriteLn(i, ' >= ', j, ' = ', i >= j);
    WriteLn(i, ' <= ', j, ' = ', i <= j);

    // Тест логических операций
    WriteLn('not ', flag, ' = ', not flag);
    WriteLn(flag, ' and false = ', flag and false);
    WriteLn(flag, ' or false = ', flag or false);

    // Тест массивов
    for i := 1 to 5 do
        arr[i] := i * 10;

    bArr[0] := true;
    bArr[1] := false;
    bArr[2] := bArr[0] and bArr[1];

    chArr['a'] := 'x';
    chArr['b'] := 'y';
    chArr['c'] := 'z';

    // Тест функций
    WriteLn('Max(', i, ', ', j, ') = ', Max(i, j));
    WriteLn('IsEven(', i, ') = ', IsEven(i));

    // Тест процедур
    PrintPrimes(20);

    // Тест Inc, Dec, Abs
    k := 5;
    Inc(k);
    WriteLn('After Inc: ', k);
    Dec(k, 2);
    WriteLn('After Dec: ', k);
    WriteLn('Abs(-', k, ') = ', Abs(-k));

    // Тест ввода
    Write('Enter an integer: ');
    ReadLn(i);
    WriteLn('You entered: ', i);

    // Тест do-while эмуляция
    repeat
        Write('Enter 0 to exit: ');
        ReadLn(j);
    until j = 0;

    WriteLn('All tests completed!');
end.