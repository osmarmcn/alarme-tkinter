from tkinter import*
import datetime
import time
import winsound
from threading import*
import datetime
import time

def threading():
	t1 = Thread(target=alarm)
	t1.start()

def alarm():
	while True:
		definirAlarme = f'{hora.get()}:{minutos.get()}:{segundos.get()}'
		time.sleep(1)

		horaAtual = datetime.datetime.now().strftime('%H:%:M:%S')
		if definirAlarme == horaAtual:
			winsound.PlaySound('sound.wav', winsound.SND_ASYNC)
			print('hora de acordar')




janela = Tk()
janela.geometry('400x200')
texto_alarme = Label(janela, text='alarme', font='Helvetica 20 bold', fg='red')
texto_alarme.pack(pady=10)

set_hora = Label(janela, text='defina hora', font='Helvetica 15 bold')
set_hora.pack()

frame = Frame(janela)
frame.pack()
hora = StringVar(janela)

hours = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23', '24'
		)

hora.set(hours[0])
hrs = OptionMenu(frame, hora, *hours)
hrs.pack(side=LEFT)

minutos = StringVar(janela)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23',
		'24', '25', '26', '27', '28', '29', '30', '31',
		'32', '33', '34', '35', '36', '37', '38', '39',
		'40', '41', '42', '43', '44', '45', '46', '47',
		'48', '49', '50', '51', '52', '53', '54', '55',
		'56', '57', '58', '59', '60')
minutos.set(minutes[0])
min = OptionMenu(frame, minutos, *minutes)
min.pack(side=LEFT)

segundos = StringVar(janela)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23',
		'24', '25', '26', '27', '28', '29', '30', '31',
		'32', '33', '34', '35', '36', '37', '38', '39',
		'40', '41', '42', '43', '44', '45', '46', '47',
		'48', '49', '50', '51', '52', '53', '54', '55',
		'56', '57', '58', '59', '60')
segundos.set(seconds[0])
secs = OptionMenu(frame,segundos, *seconds)
secs.pack(side=LEFT)


btn = Button(janela, text='definir Alarme', font='Helvetica 15', command=alarm)
btn.pack(pady=20)

janela.mainloop()