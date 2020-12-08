.data
.balign 4	
Intro: 	 .asciz  "Raspberry Pi wiringPi blink test\n"
ErrMsg:	 .asciz	"Setup didn't work... Aborting...\n"
pin:	 .int	29
i:	 .int	0
delayMs: .int	500
OUTPUT	 =	1
.text
	.global main
	.extern printf
	.extern wiringPiSetup
	.extern delay
	.extern digitalWrite
	.extern pinMode
	
main:   push 	{ip, lr}	@ push return address + dummy register
				@ for alignment

	ldr	r0, =Intro	
        bl 	printf		

	bl	wiringPiSetup
	mov	r1,#-1
	cmp	r0, r1
	bne	init
	ldr	r0, =ErrMsg
	bl	printf
	b	done

init:
	ldr	r0, =pin
	ldr	r0, [r0]
	mov	r1, #OUTPUT
	bl	pinMode

	ldr	r4, =i
	ldr	r4, [r4]
	mov	r5, #10
forLoop:
	cmp	r4, r5
	bgt	done
	
	ldr	r0, =pin
	ldr	r0, [r0]
	mov	r1, #1
	bl 	digitalWrite
	

	ldr	r0, =delayMs
	ldr	r0, [r0]
	bl	delay


	ldr	r0, =pin
	ldr	r0, [r0]
	mov	r1, #0
	bl 	digitalWrite


	ldr	r0, =delayMs
	ldr	r0, [r0]
	bl	delay

	add	r4, #1
	b	forLoop
	
done:	
        pop 	{ip, pc}
