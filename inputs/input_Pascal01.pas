program teste; {programa exemplo}
var 
	valor1, valor3, valor4: integer;
	valor2: real;
procedure myProcedure(argum1, argum2: integer; argum3: real);
var
	myVar1, myVar2: integer;
	myVar3: boolean;
begin
	myVar1 := 10;
	myVar2 := myVar1 + 2;
	myVar3 := true
end
begin % @
	valor1 := 10;
	myProcedure();
	{valor5 := 10.2;
	valor3 := .234;
	valor9 := 12.;
	valor1 >= valor2;
	valor2 < valor3;
	valor1 = valor2;
	valor3 <> valor1;}
	if (valor1 >= 20) and (valor1 <=90) then
      valor1 := 10 * 3   
    else valor1 := 10 / 3
	{valor3 <> # valor1;
	valor2 or $ valor1;
	valor3 and valor2;}
	while (valor1 <= 5) do
    begin
      valor2 := valor1+1;
      valor1 := valor2-1;
      valor1 := valor1 + valor2;
      valor1 := valor1 + 1
    end
	valor1 := valor1 + valor2
end.