# generate SQLs by a given template with all possible values
import itertools

def generate(pattern, params):
    """Generate SQLs by enumerating all possible value combinations

    Parameters
    ----------
    pattern : str
        the SQL template
    params : dict
        a dict of key-value pairs, where key is the variable name we will replace in
        the pattern and value is a list of all possible values

    Returns
    -------
    type : list of str
        the generated SQLs

    Examples
    --------
    >>> pattern = 'SELECT * FROM cmu WHERE name = NAME'
    >>> params = dict(NAME=['andy', 'joy'])
    >>> print generate(pattern, params)
    ['SELECT * FROM cmu WHERE name = andy', 'SELECT * FROM cmu WHERE name = joy']

    >>> pattern = 'SELECT * FROM COMPANY WHERE VAR1 OP VAR2'
    >>> params = dict(COMPANY=['cmu'],
    ...               VAR1=['age', 'height'],
    ...               OP=['=', '>'],
    ...               VAR2=[random.randint(1, 10) for i in range(2)])
    >>> print generate(pattern, params)
    ['SELECT * FROM cmu WHERE age = 10', 'SELECT * FROM cmu WHERE age > 10', 'SELECT * FROM cmu WHERE height = 10', 'SELECT * FROM cmu WHERE height > 10', 'SELECT * FROM cmu WHERE age = 9', 'SELECT * FROM cmu WHERE age > 9', 'SELECT * FROM cmu WHERE height = 9', 'SELECT * FROM cmu WHERE height > 9']
    """
    # find the names in the pattern
    keys = [k for k in params.iterkeys()]
    words = pattern.split()
    pos = []
    for k in keys:
        p = [i for i, w in enumerate(words) if w == k]
        assert(len(p) == 1), 'name [%s] does not exist in the pattern' % 'yy'
        pos.append(p[0])

    # enumerate all combinations
    res = []
    for v in itertools.product(*params.itervalues()):
        assert(len(v) == len(pos))
        cur = words
        for p,w in zip(pos, v):
            cur[p] = w
        res.append(' '.join([str(w) for w in cur]))

    return res
