from sys import argv
from os import makedirs, system
from os.path import expanduser
from peyconfig import name


def main(args):
    company = args[0]
    position = args[1]
    team = args[2]

    preamble = r'''
    % INSERT PREAMBLE
    \documentclass[UTF8]{article}
    '''

    header = r'''
    %% INSERT UR MAKETITLE STUFF
    \title{lol id insert an emoji but no.}
    \author{
           %(name)s
    }
    \date{\today}
    ''' % {'name': name}

    content = r'''
    \begin{document}
    \maketitle
    INSERT UR LATEX HERE
    %(company)s %(position)s %(team)s
    \end{document} ''' % {'company': company, 'position': position, 'team':
                          team}

    dir = expanduser('~/jobs/{}'.format(company))
    tex = '{}/{}.tex'.format(dir, company)

    try:
        makedirs(expanduser('~/jobs/%s' % company))
    except Exception:
        pass
    new_cover = open(tex, "w")
    new_cover.write(preamble)
    new_cover.write(header)
    new_cover.write(content)
    new_cover.close()
    system('pdflatex -output-director {} {}'.format(dir, tex))
    return '{}/{}.pdf'.format(dir, company)


if __name__ == "__main__":
    main(argv[1:])
