# Hanoi_Stack

Hanoi_Stack is an three-stacks-machine language written in 2-bytes binary representation.
Here is the details of it.

## Input
Input string is contained in 00-stack,top of whitch is 4-bytes value of string length.

## Operator instruction

Calculate top of two stacks.

0b001 XXX YY Z NN 00000

XXX is an operator specifer.Here is the table of it.

|bin |operator
|----|-----
|000 |Add(+)
|001 |Sub(-)
|010 |Mul(\*)
|011 |Div(/)
|100 |Mod(%)
|101 |Or(\|)
|110 |And(&)
|111 |Xor(^)

YY and Z are stack specifer. Hanoi_Stack has three stacks, so YY is either of 00-10. and Z specifies one from rest of two.

NN is a bytes specifer to operate, which means (1<<NN)-bytes calculation.

## Copy instruction

Copy top of stack data to other stack.

0b0001 XX Y NN 0000000

XX and Y are stack specifer same as Operator instruction, and NN is a bytes specifer.

## Push instruction

Push one byte immediate value.

0b01 XX VVVVVVVV 0000

XX is a stack specifer and VVVVVVVV is immediate value.

## Print instruction

Print one byte top of stack as char code.

0b00001 XX 000000000

XX is a stack specifer.

## Pop instruction
Delete top of stack value.

0b000000 XX NN 000000

XX is a stac specifer and NN is a bytes specifer.

## Jmp instruction
Change ip to the offset. Current ip points next instruction.

0b1 S VVVVVVVVVVVVVV

S is a sign flag. if S is 1, then next offset is treated as minus value.

VVVVVVVVVVVVVV is an offset. ip changes to ip+VVVVVVVVVVVVVV(or ip-VVVVVVVVVVVVVV if S is 1).

## Is-zero instruction
if top of stack value is zero, then next instruction is skipped.

0b000001 XX NN 000000

XX is stack specifer,and NN is bytes specifer.
