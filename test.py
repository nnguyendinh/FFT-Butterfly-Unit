#To Do: #Input values for Testing

a_real = float(49)
a_imag = float(65)
b_real = float(18)
b_imag = float(146)

for i in range(4):
    if i == 0:    
        w_real = 1
        w_imag = 0
    elif i==1:
        w_real = 0
        w_imag = -1
    elif i==2:
        w_real = -1
        w_imag = 0
    elif i==3:
        w_real = 0
        w_imag = 1

    mult_out_real = b_real * w_real - b_imag * w_imag
    mult_out_imag = b_imag * w_real + b_real * w_imag

    f0_real = a_real + mult_out_real
    f0_imag = a_imag + mult_out_imag
    f1_real = a_real - mult_out_real
    f1_imag = a_imag - mult_out_imag

    print("When w = " + str(w_real) + " " + str(w_imag))
    print("f0 = " + str(f0_real) + " " + str(f0_imag))
    print("f1 = " + str(f1_real) + " " + str(f1_imag))
    print("")