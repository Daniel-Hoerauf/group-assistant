from .response import answer

fn_map = {}
fn_map['/answer'] = answer


from .handler import process
