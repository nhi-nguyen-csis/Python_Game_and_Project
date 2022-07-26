'''

Source: ASCII Art https://www.asciiart.eu/plants/roses
'''

sImage1 = '''
                        .mm
                      .mMMM       .mmmm.
                     /MMMMM    .mMMMMMM)
                    /MMMMMM.  .mMMMMM"'
                    MMMMMMM| ,MMMMMMM'
                    MMMMMMM| mMMMMM'
                    \MMMMMMMSsMMM/'
                    `MMM.sSSSSsMsSs
                   .. /SSSSSSSSsSSSs.
                  (SSss.SSSSSS/SSSSSSs,
                   `SSSSsSSS'SS/sSSS"S)
                    SSSSSSSNNNNn.SSSss,
                   (SSSSSSSsNNNNN)SSSSs,__
                   `"SSSsSSSSs~N~sSSSSS)MMMMmmm
                      SSSSSSSSSS\SSSS"mMMMMMMMMMMm..        .mM|
                  mmMMmSSSSSSS"mMMMMMMMMMMMMMMMMMMMMMMmm.mmmMMMM)
\Mm..        mmMMMMMMMMMmmmmmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmMM
 \MMMmm.mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM/"      "`MMMMMMMMmMM/
 |MMMMMMmMMMMMMMMMMMMMMMMMM"""""MMMMMMMMMMM|         \MMMMMMMMMM'
  M\MMMMMMMMMMMMMMMMMMM"'          `.MMMMM(           \MMMMMMMM/
  \MmMMMMMMMMMMMMMMMM"'               `.MM/            \MMMMMMM/
   \MMmMMMMMMMMMMMMM/                   `M|             )MMMMMM
    \MMMMMMMMMMMMMMM'                    "               MMMMM/
    |MMMMMMMMMMMMMM/                                     MMMM/
     \MMMMMMMMMMMMM(                                     MMMM'
      \MMMMMMMMMMMM|                         ...         MMM/
       \MMMMMMMMMMMM\                  .o.   OOOo       )MMM'
       `MMMMMMMMMMMMM.                oOOO   OOOOo      /MM/
        \MMMMMMMMMMMMM\              (OOOO   `OOOO     /MMM/
         \MMMMMMM""""MM\.             OOOO  ___`"'    ,mMMM(_
          \MMMM/       "-.             ".**"'  )***   /      '.
           \MM(                   .-'- (**(   .**** .----,.   )
            \M(                   `    (*********/    /   '  /
             \`.       ..-----\          """"""      /      /
              ``.     `    `\.                     ,'     /'
                \.           `\.                .-'    ,/'
                  `\.           `-._________--'      .'
                     ``-..                     /  _,'
                          ""`--____\.       ,/'"""
                                    `\____/'
'''
sImage2 = '''
_____8888888888____________________
____888888888888888_________________
__888888822222228888________________
_88888822222222288888_______________
888888222222222228888822228888______
888882222222222222288222222222888___
8888822222222222222222222222222288__
_8888822222222222222222222222222_88_
__88888222222222222222222222222__888
___888822222222222222222222222___888
____8888222222222222222222222____888
_____8888222222222222222222_____888_
______8882222222222222222_____8888__
_______888822222222222______888888__
________8888882222______88888888____
_________888888_____888888888_______
__________88888888888888____________
___________8888888888_______________
____________8888888_________________
_____________88888__________________
______________888___________________
_______________8____________________

'''
str = input('Enter the message to display with the bitmap: ')
i = 0
for line in sImage2.splitlines():
    for i, char in enumerate(line):
        if char == '_':
            print(char, end='')
        else:
            print(str[i % len(str)], end='')
    print()
print()
i = 0
for line in sImage1.splitlines():
    for i, char in enumerate(line):
        if char == ' ':
            print(char, end='')
        else:
            print(str[i % len(str)], end='')
    print()