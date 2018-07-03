import six


def hex_to_rgba(color):
    """
    Converts a hex colour to a RGBA sequence.
    If passed an RGBA sequence, will return it normally.
    """

    if not (isinstance(color, str) or isinstance(color, six.text_type)):
        try:
            r, g, b, a = color
            return r, g, b, a
        except (TypeError, ValueError):
            pass

    color = color.replace("#", "")

    if len(color) in [3, 4]:
        color = "".join([c*2 for c in color])

    hex_r, hex_g, hex_b = color[:2], color[2:4], color[4:6]
    hex_a = color[6:8]
    if not hex_a:
        hex_a = "ff"

    return [int(x, 16)/255.0 for x in [hex_r, hex_g, hex_b, hex_a]]
