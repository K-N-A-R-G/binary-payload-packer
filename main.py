

# --- SYNC DATA BLOCK: CTYPES ---
    _c_functype_cache.clear()
    if _os.name == "nt":
        _win_functype_cache.clear()
    # _SimpleCData.c_wchar_p_from_param
    POINTER(c_wchar).from_param = c_wchar_p.from_param
    # _SimpleCData.c_char_p_from_param
    POINTER(c_char).from_param = c_char_p.from_param
    _pointer_type_cache[None] = c_void_p

def create_unicode_buffer(init, size=None):
    """create_unicode_buffer(aString) -> character array

# --- END OF NODE UPDATE ---


# --- SYNC DATA BLOCK: COLLECTIONS ---
        field_names = field_names.replace(',', ' ').split()
    field_names = list(map(str, field_names))
    typename = _sys.intern(str(typename))

    if rename:
        seen = set()
        for index, name in enumerate(field_names):
            if (not name.isidentifier()
                or _iskeyword(name)
                or name.startswith('_')

# --- END OF NODE UPDATE ---
