import discord
from discord.ext import commands, tasks
from webserver import keep_alive
import datetime
import asyncio
from urllib import parse, request
import re

intents = discord.Intents.default()
intents.message_content = True  # Activar este intent si planeas trabajar con contenido de mensajes

bot = commands.Bot(command_prefix="+", help_command=None, intents=intents)


@bot.event
async def on_ready():
  print('bot is ready')


@tasks.loop(seconds=10)
async def change_status():
  await bot.change_presence(activity=discord.Game(
      name="In" + str(len(bot.guilds)) + "servers prefix +"))


@bot.command(name='help')
async def help(ctx):
  embed = discord.Embed(
      title='Comandos',
      description=
      'Puedes encontrar los comandos que se me fueron otorgados para que tu experiencia en el discord y en el server de minecraft sean totalmente innovadores',
      color=discord.Color.purple())
  embed.add_field(name='`+ip`',
                  value='Para saber la ip del server',
                  inline=False)
  embed.add_field(
      name='`+normas`',
      value=
      'Las normas del server de minecraft se clasifican en graves, leves, juicio y staff.',
      inline=False)
  embed.add_field(name='`+leves`',
                  value='Encontraras las normas leves.',
                  inline=False)
  embed.add_field(name='`+graves`',
                  value='Encontraras las normas graves.',
                  inline=False)
  embed.add_field(name='`+juicio`',
                  value='las normas que se usan en el juicio.',
                  inline=False)
  embed.add_field(name='`+staff`',
                  value='Podras saber las normas del staff de minecraft.',
                  inline=False)
  embed.add_field(name='`+clanes`',
                  value='Hallaras las reglas para los clanes.',
                  inline=False)
  embed.add_field(
      name='`+comandos`',
      value='Encontraras los comandos que puedes usar en el server.',
      inline=False)
  embed.add_field(name='`+tienda`',
                  value='Podras donarnos y ver los rangos en nuestra pagina.',
                  inline=False)
  embed.add_field(
      name='Emergencia',
      value=
      'En caso de un bug o algo relacionado con OlympusBot hablar con mi creadora Paulidex.',
      inline=False)
  embed.set_footer(text='Contrataciones al dm Paulidex#9510.')
  await ctx.send(embed=embed)


@bot.command(name='f')
async def f(ctx):
  embed = discord.Embed(title='Timer',
                        description='`ip`: olympus.zyx ',
                        color=discord.Color.purple())
  embed.add_field(name='version', value='`1,16`: Paulidex')
  await ctx.send(embed=embed)


@bot.command()
async def a(ctx):
  await ctx.send(
      'Recordatorio de que el final del paraiso es una pesima telenovela y esos 90 capitulos fue una perdida de tiempo'
  )


@bot.command()
async def tienda(ctx):
  await ctx.send(
      'Ingresa para ver nuestros rangos y tambien nos puedes donar ^.^ `https://olympusland.tebex.io`'
  )


@bot.command()
async def ip(ctx):
  embed = discord.Embed(
      title='Server Minecraft Java',
      description='Version 1.16.5 - 1.17.1: play.olympusland.xyz',
      color=discord.Color.purple())
  embed.set_footer(text='Para ver que mas comandos ocupo escribe +help')
  await ctx.send(embed=embed)


@bot.command()
async def normas(ctx):
  await ctx.send(
      'Se clasifican en graves, leves, staff y juicio para poder verlas escribe `+graves` `+leves` `+staff` `+juicio` `+clanes`'
  )


@bot.command(name='leves')
async def leves(ctx):
  embed = discord.Embed(
      title='Normas Leves',
      description=
      '1) Los bugs están permitidos pero antes debes consultar su uso con alguien del staff \n2) No esta permitido insultar a otros jugadores si es que no es de su agrado \n3) No hacer flood (ejemplo: holaaaaaa) ni Spam o texto innecesario que sature el chat. \n4) No está permitido el tener bajo su poder más de dos relojes de Redstone, tal como está prohibido los generadores de lag y cargadores de chunks. \n5) Las mascotas son propiedad privada aunque no este en una zona protegida esta prohibido matarles con la intención de esta. (caballos, cerdos, lobos, gatos) \n6) Los lobos están prohibidos como arma para el PVP  \n7) En casos de que haya problemas aislados, el staff se reserva el derecho de hacer una reunión para llegar a una solución o sentencia justa para el caso. \n8) No salirse de un juicio',
      color=discord.Color.purple())
  embed.set_footer(
      text=
      'Las normas se van acumulando y los castigos pueden cambiar dependiendo de la persona, para ver que mas comandos ocupo escribe +help'
  )
  await ctx.send(embed=embed)


@bot.command(name='graves')
async def graves(ctx):
  embed = discord.Embed(
      title='Normas graves',
      description=
      '1) Se prohíbe el uso de multicuentas, si deseas hacer hacer un cambio de cuenta debes avisar a un miembro del staff, el cual procederá a pasar tus ítems y propiedades a la nueva cuenta y posteriormente esa cuenta será baneada. Si tienes un familiar o amigo con la misma ip deberás avisar al staff para utilizar las cuentas. \n2) Los Hacks están completamente prohibidos y serán sancionados con ip-ban \n3) Queda prohibido el intento o la destrucción de construcciones protegidas, robo de ítems en zona de otro jugador, destrucción de cultivos o agarrar los cultivos mientras el otro jugador los quita (No nos hacemos responsables de zonas no protegidas) \n4) Cualquier clase de asesinato como el tpakill y el spawn kill está prohibido \n5) Prohibido sacar ventajas de bugs como lo son los glitchs de duplicación o movilidad \n6) Prohibido el uso de Hacks como lo es el xray, autoclick, etc. \n7) Se prohíbe la distribución de enlaces externos y de otros los servers, esto se debe consultar con alguien del staff. \n8) Hablarle con respeto al staff y queda totalmente prohibido faltarles el respeto o burlarse de u trabajo. \n9) Cualquier intento de evadir una sentencia se aumentará la sentencia y cualquier jugador que trate de ayudar a evadir la sentencia a otro jugador será sentenciado también. \n10) Esta estrictamente prohibido mentirle al staff. \n11) Prohibido el hacerse pasar por algún miembro del staff. \n12) No se debe hablar de otros casos para justificar una acción. \n13) No están permitidos los mensajes y construcciones que puedan ofender o faltar el respeto hacia los demás jugadores, ya sea por raza, genero, creencia, religión y/u orientación sexual. \n14) No escapar de la cárcel. \n15) No ayudar al preso a salir de la cárcel. \n16) No explorar, minar, talar en el mundo normal para eso esta /warp recursos',
      color=discord.Color.purple())
  embed.set_footer(
      text=
      'Las normas se van acumulando y los castigos pueden cambiar dependiendo de la persona, para ver que mas comandos ocupo escribe +help'
  )
  await ctx.send(embed=embed)


@bot.command(name='juicio')
async def juicio(ctx):
  embed = discord.Embed(
      title='Normas del juicio',
      description=
      '1) No interrumpir \n2) Tener pruebas \n3) No hacerle perder el tiempo al miembro del staff que le toque hacer de juez \n4) Leer las normas antes de solicitar un juicio \n5) Solo se permiten a los testigos y a los implicados del problema en el juicio \n6) Solo un Owner, Admin, Mod pueden ser juez \n7) Deben estar ambas partes tanto los acusados como los que acusan',
      color=discord.Color.purple())
  embed.set_footer(
      text=
      'Las normas se van acumulando y los castigos pueden cambiar dependiendo de la persona, para ver que mas comandos ocupo escribe +help'
  )
  await ctx.send(embed=embed)


@bot.command(name='clanes')
async def clanes(ctx):
  embed = discord.Embed(
      title='Normas del juicio',
      description=
      '1) Cualquier tipo de pvp es valido siempre y cuando los jugadores pertenezcan a un clan \n2) Se permite el grifeo pero solo a bases de los clanes',
      color=discord.Color.purple())
  embed.set_footer(
      text=
      'Las normas se van acumulando y los castigos pueden cambiar dependiendo de la persona, para ver que mas comandos ocupo escribe +help'
  )
  await ctx.send(embed=embed)


@bot.command(name='staff')
async def staff(ctx):
  embed = discord.Embed(
      title='Normas del staff',
      description=
      '1) Cualquier duda o queja respecto a los baneos se atenderá por discord \n2) Los objetos de los cuales el staff se reserva el derecho de tenerlos solo para ellos, no deben quedar en manos de un jugador, en caso  tal de que suceda, ambos involucrados serán sancionados. \n3) Responder todas las dudas de los jugadores \n4) Saludar a los nuevos jugadores \n5) No hacer Abuso de poder \n6) Solo las personas con rango Owner, Admin y Mod cuentan con los permisos para sancionar \n7) Tratar a todos los jugadores por igual \n8) No darles nada a los jugadores por medio del creativo o codigos, solo debe ser por medio del survival \n9) Ser neutral en los juicios \n10) Si no muestra actividad, ayuda o beneficio para el server se te será retirado del staff \n11) No decirle a los demas jugadores las nuevas cosas que se van a implementar',
      color=discord.Color.purple())
  embed.set_footer(
      text=
      'Las normas se van acumulando y los castigos pueden cambiar dependiendo de la persona, para ver que mas comandos ocupo escribe +help'
  )
  await ctx.send(embed=embed)


@bot.command(name='comandos')
async def comandos(ctx):
  embed = discord.Embed(
      title='Comandos que puedes usar en el server',
      description=
      '/tpa (ir a otro humano) \n/tpaccept (aceptar tpa) \n/tpahere (traer a otro humano) \n/back (volver a el sitio anterio) \n/sit (para sentarse) \n/afk (estar ausente) \n/sethome (marcar un home) \n/home "nombre" (lugar) \n/delhome "nombre" (borrar un home) \n/ps add "nombre" (agregar persona a tu piedra) \n/ps remove "nombre" (quitar a un jugador de tu piedra) \n/tienda (acceder a la tienda) \n/piedras (piedra de proteccion) \n/trabajos (conseguir dinero) \n/jobs join  "nombre"(ingresar a un trabajo) \n/jobs remove "nombre" (salir de un trabajo) \n/ec (ender chest) \n/pay "cantidad" "nickname" (pagar) \n/money (ver tu dinero) \n/baltop (ver las personas mas ricas de olimpus) \n/ah (subasta) \n/ah sell "precio" (poner el ítem en la mano para vender en el ah) \n/tienda (para comprar piedras, torretas, etc.) \n/warp recursos (este mundo es para conseguir materia prima y se resetea no se recomienda construir) \n/warp matadero (conseguir comida) \n/warp boda (Encontraras la iglesia) \n\nPuedes hacer ascensores solo pon un bloque de cuarzo y un bloque de redstone abajo de este',
      color=discord.Color.purple())
  embed.set_footer(text='Para ver que mas comandos ocupo escribe +help')
  await ctx.send(embed=embed)


keep_alive()
bot.run("YOUR_BOT_TOKEN"")
