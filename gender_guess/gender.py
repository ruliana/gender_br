import unidecode as ud

__gender_exceptions__ = {'a': ['bliw', 'br', 'civ', 'clim', 'diem', 'dnar', 'du', 'err', 'fa', 'h|', 'hc', 'ho', 'hpa', 'htan', 'ile|', 'iledr', 'imer', 'ja', 'jr', 'ka', 'kk', 'la|', 'lg', 'lit', 'liv', 'loc', 'lro', 'man', 'may', 'mini', 'mlaj', 'mn', 'mru', 'muz', 'ng', 'nnat', 'np', 'om', 'raj', 'rat', 'raug', 'rieb', 'riev', 'rik', 'riu', 'rp', 'ruj', 'rum', 'rut', 'sa', 'ssa', 'ssu', 'tai|', 'tano', 'tari', 'tel', 'terp', 'toj', 'tsi', 'ua', 'ud', 'uh', 'uq', 'va', 'vd', 'vi|', 'vlis', 'vo', 'vr', 'w', 'yan', 'zuo'],
              'b': ['adani'],
              'c': ['il', 'it'],
              'd': ['ade', 'ir'],
              'e': ['ad', 'aj', 'ak', 'bao', 'bu', 'cal', 'ced', 'cilef', 'ciru', 'cn', 'curb', 'dad', 'deb', 'di|', 'dia|', 'diat', 'dic', 'dila', 'div', 'dla', 'dlih', 'dlinesa', 'dn', 'do', 'el', 'g|', 'ge', 'go', 'gr', 'gu', 'hp', 'ib', 'ile', 'ill', 'in', 'j', 'ke', 'ki', 'klo', 'kn', 'ko', 'ks', 'ku', 'lat', 'lau', 'lav', 'lc', 'ledr', 'leg', 'leit', 'len', 'less', 'leu', 'lh', 'libat', 'lil', 'lir', 'lled', 'lo', 'ly', 'ma', 'mea', 'med', 'mi', 'ml', 'mr', 'ms', 'mu', 'my', 'nahp', 'nan', 'navi', 'navla', 'navle', 'navlig', 'navo', 'ned', 'neico', 'neit', 'nelig', 'nelsu', 'ner|', 'niav', 'niaw', 'nidla', 'nidu', 'nim', 'nin', 'nio', 'nitr', 'nnav', 'nner', 'nnh', 'nnoi', 'noc', 'nod', 'noe', 'nof', 'noice', 'noicla', 'noide', 'noih', 'noj', 'nor', 'not', 'nr', 'nu', 'oi', 'on', 'pe', 'pi', 'po', 'pp', 'py', 'ras', 'rb', 'rd', 'reb', 'red', 'rf', 'ria', 'rih', 'ro', 'rr', 'rt', 'sd', 'se', 'sieg', 'sliw', 'soj', 'sr', 'sse', 'ssu', 'su', 'tea', 'tedlaw', 'tedoi', 'teds', 'teia', 'tesin', 'teze', 'tezin', 'tided', 'tiu', 'tl', 'tna', 'tne', 'tra', 'treal', 'treh', 'trei', 'tser', 'ua', 'ug', 'uo', 'uqa', 'uqe', 'uqia', 'uqini', 'uqir', 'uql', 'uqo', 'uqr', 'use', 'uso', 'uzo', 'vat', 'vi', 'vo', 'w', 'y', 'z|', 'za', 'ze', 'zu'],
              'g': ['ie', 'neh', 'nipm', 'nob', 'nuj'],
              'h': ['ak', 'an', 'ar', 's', 'teb', 'ter', 'tes', 'tezil', 'tezir', 'tide|', 'tidu', 'tur'],
              'i': ['ale', 'ana', 'ano', 'ba', 'cajd', 'calg', 'caram', 'cari|', 'carid', 'carol', 'cedli', 'cen|', 'cia', 'cira', 'cle|', 'cn', 'co', 'cu', 'dak', 'diel', 'dir', 'duh', 'elrih', 'elris', 'em|', 'enir', 'ha', 'j|', 'ki', 'kusi', 'kuy|', 'lag', 'lar', 'legn', 'lei', 'lek', 'lel', 'len', 'les', 'leu', 'lev', 'lez', 'li', 'lleh', 'llek', 'lra', 'lrednaw', 'mah', 'mei', 'meo', 'mor', 'mt', 'muss', 'muy', 'muz', 'nab', 'nai', 'nari', 'nas', 'nat', 'naul', 'nav|', 'navi|', 'navli', 'nay', 'ne|', 'nec', 'neg', 'nel', 'neru', 'neso|', 'nev', 'nez', 'nic', 'nie', 'nil', 'nnej', 'nom', 'nu', 'ram', 'rev', 'rh', 'roa', 'ruya', 'sl', 'sr', 'sseg', 'tor', 'ts', 'tter', 'tteu', 'ua', 'vai', 'z|', 'zaz', 'zus'],
              'k': ['an', 'l'],
              'l': ['am', 'eb|', 'ebam', 'ebar', 'ebas', 'ebaz', 'ehca', 'eht', 'euq', 'iag', 'inel', 'lem', 'o'],
              'm': ['ailil', 'air', 'aiv', 'arim', 'ee', 'eleu', 'em', 'er'],
              'n': ['ailil', 'aillil', 'airam', 'airi', 'airy', 'aivi', 'ale', 'alir', 'asu', 'avin', 'avira', 'ayri', 'azu', 'eho', 'ekc', 'ele', 'ell', 'em', 'era', 'ets', 'ielr', 'ilek', 'ilev', 'ims', 'ir', 'itsi', 'itsr', 'na|', 'ny', 'orah', 'uk', 'us', 'y'],
              'o': ['acie', 'ce', 'cim', 'cit', 'd|', 'h|', 'ico', 'ka', 'ke', 'kiek', 'kies', 'kihc', 'kihs', 'kika', 'kiku', 'kim', 'kir', 'kit', 'ko', 'kur', 'kus', 'kuy', 'kuzi', 'leu', 'nats', 'niruam', 'rro', 'tej', 'tnem', 'ul'],
              'p': ['iy'],
              'r': ['al', 'amal', 'amaz', 'amicy', 'amidi', 'amidue', 'amilo', 'amisl', 'amizl', 'amsire', 'anide', 'effi', 'efi', 'ehta', 'ehts', 'epse', 'etse|', 'iadam', 'ialce', 'ialo', 'ian|', 'icalg', 'idan|', 'idel', 'inav|', 'inave|', 'inec|', 'inele', 'inez', 'inoi', 'oif', 'onoe', 'ycar'],
              's': ['adinu', 'aitak', 'ecr', 'edec', 'edio', 'edlia', 'edred', 'edru', 'eduel', 'edui', 'egri', 'ekl', 'eleg', 'enele', 'eng', 'eni|', 'enia', 'enid|', 'enir', 'ep', 'ered', 'erim|', 'erima', 'ero', 'even', 'iah', 'ial', 'iat', 'ida', 'ila', 'ile|', 'ili', 'ill', 'ily', 'inedl', 'inna', 'io', 'ira', 'irc|', 'iri|', 'irim', 'iris', 'irod', 'iry', 'isi', 'itr', 'iz', 'orieh', 'yd', 'yni', 'yr'],
              't': ['eb', 'er', 'ide|', 'ig', 'se', 'ten', 'ti'],
              'u': ['d|', 'la', 'rahim|', 's|'],
              'y': ['am', 'ana', 'anoi', 'cal', 'cara|', 'cari|', 'carod', 'cav', 'cira', 'clao', 'cn', 'cren', 'cu', 'dal', 'deh', 'elrih', 'enar', 'g', 'ha', 'htor', 'lat', 'lea', 'lecu', 'leg', 'lek', 'len', 'les', 'leu', 'lev', 'lez', 'lia', 'lir', 'lle', 'lram', 'mat', 'nai', 'nari', 'nas', 'nau', 'navl', 'naw', 'neg', 'nel', 'neu', 'nna', 'nom', 'ram', 'remi', 'rems', 'ri', 'ror', 'si', 'so', 'su', 't'],
              'z': ['eni|', 'enir', 'ered', 'il', 'ir', 'u']}

def male(name):
    reversed = name[::-1].lower()
    reversed = ud.unidecode(reversed + '|')
    end_letter = reversed[0]
    is_male = end_letter not in ['a', 'e']
    for e in __gender_exceptions__[end_letter]:
        if reversed[1:].startswith(e):
            return not is_male
    return is_male


def female(name):
    return not male(name)
