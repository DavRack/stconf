def xres2st():
    xres = open("xres", "r")
    lineas = xres.readlines()
    colores = []
    lista = []
    for i in lineas:
        lista = i.split(" ")
        for j in lista:
            if j.startswith("#"):
                colores.append(j[:-1])
    
    print('  /* 8 normal colors */')
    print('  [0] = "{}", /* black   */'.format(colores[1]))
    print('  [1] = "{}", /* red     */'.format(colores[5]))
    print('  [2] = "{}", /* green   */'.format(colores[7]))
    print('  [3] = "{}", /* yellow  */'.format(colores[9]))
    print('  [4] = "{}", /* blue    */'.format(colores[11]))
    print('  [5] = "{}", /* magenta */'.format(colores[13]))
    print('  [6] = "{}", /* cyan    */'.format(colores[15]))
    print('  [7] = "{}", /* white   */'.format(colores[17]))
    print('')
    print('  /* 8 bright colors */')
    print('  [8]  = "{}", /* black   */'.format(colores[4]))
    print('  [9]  = "{}", /* red     */'.format(colores[6]))
    print('  [10] = "{}", /* green   */'.format(colores[8]))
    print('  [11] = "{}", /* yellow  */'.format(colores[10]))
    print('  [12] = "{}", /* blue    */'.format(colores[12]))
    print('  [13] = "{}", /* magenta */'.format(colores[14]))
    print('  [14] = "{}", /* cyan    */'.format(colores[16]))
    print('  [15] = "{}", /* white   */'.format(colores[18]))
    print('')
    print('  /* special colors */')
    print('  [256] = "{}", /* background */'.format(colores[1]))
    print('  [257] = "{}", /* foreground */'.format(colores[0]))

def st2xres():
    xres = open("config.h", "r")
    lineas = xres.readlines()
    colores = []
    lista = []
    for i in lineas:
        lista = i.split(" ")
        for j in lista:
            if j.startswith('"#'):
                colores.append(j[1:-3])

    print('! special')
    print('*.foreground:   {}'.format(colores[17]))
    print('*.background:   {}'.format(colores[16]))
    print('*.cursorColor:  {}'.format(colores[17]))
    print('                ')
    print('! black         ')
    print('*.color0:       {}'.format(colores[0]))
    print('*.color8:       {}'.format(colores[8]))
    print('                ')
    print('! red           ')
    print('*.color1:       {}'.format(colores[1]))
    print('*.color9:       {}'.format(colores[9]))
    print('                ')
    print('! green         ')
    print('*.color2:       {}'.format(colores[2]))
    print('*.color10:      {}'.format(colores[10]))
    print('                ')
    print('! yellow        ')
    print('*.color3:       {}'.format(colores[3]))
    print('*.color11:      {}'.format(colores[11]))
    print('                ')
    print('! blue          ')
    print('*.color4:       {}'.format(colores[4]))
    print('*.color12:      {}'.format(colores[12]))
    print('                ')
    print('! magenta       ')
    print('*.color5:       {}'.format(colores[5]))
    print('*.color13:      {}'.format(colores[13]))
    print('                ')
    print('! cyan          ')
    print('*.color6:       {}'.format(colores[6]))
    print('*.color14:      {}'.format(colores[14]))
    print('                ')
    print('! white         ')
    print('*.color7:       {}'.format(colores[7]))
    print('*.color15:      {}'.format(colores[15]))


if input("xres2st[1] o st2xres[2]?: ") == "1":
    xres2st()
else:
    st2xres()
