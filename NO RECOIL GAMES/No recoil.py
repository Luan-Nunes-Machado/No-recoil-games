import time
import win32api
import keyboard


estado_esquerda = win32api.GetKeyState(0x01)  # Botão esquerdo: Acima = 0 ou 1; Pressionado = -127 ou -128
estado_direita = win32api.GetKeyState(0x02)  # Botão direito: Acima = 0 ou 1; Pressionado = -127 ou -128
botao_toggle = '+'  # Botão de alternância

# Último estado do botão de alternância
ultimo_estado_toggle = False

# Define se o anti-recoil está ativado por padrão
ativado_anti_recoil = False

# Módulo para anti-recoil do m416
def m416(s_esquerda, s_direita, x):
    if x != s_direita:  # Ação: mirar
        recoilNum = 5  # ALTERE o valor aqui
        while x < 0:
            a = win32api.GetKeyState(0x01)  # Sempre verifica o estado do clique esquerdo
            if a != s_esquerda:
                if a < 0:
                    win32api.mouse_event(0x01, 0, recoilNum)
                    time.sleep(0.001)

            x = win32api.GetKeyState(0x02)  # Verifica o estado do botão direito

    a = win32api.GetKeyState(0x01)
    if a != s_esquerda:
        while a < 0:
            win32api.mouse_event(0x01, 0, 2)
            time.sleep(0.01)
            a = win32api.GetKeyState(0x01)  # Verifica o estado do botão

# Início do programa
print("Script anti-recoil do PUBG iniciado!")

while True:
    b = win32api.GetKeyState(0x02)

    # Verifica se houve mudança de estado para o botão de alternância
    botao_press_flat = keyboard.is_pressed(botao_toggle)

    # Execução do script
    if botao_press_flat != ultimo_estado_toggle:
        ultimo_estado_toggle = botao_press_flat
        if ultimo_estado_toggle:
            ativado_anti_recoil = not ativado_anti_recoil
            if ativado_anti_recoil:
                print("Anti-recoil m416 ATIVADO")
            else:
                print("Anti-recoil m416 DESATIVADO")

    if ativado_anti_recoil:
        m416(estado_esquerda, estado_direita, b)

    time.sleep(0.001)
