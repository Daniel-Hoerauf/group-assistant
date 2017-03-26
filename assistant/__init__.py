from .response import answer, eight_ball

fn_map = {}
fn_map['/answer'] = answer
fn_map['/ball'] = eight_ball


from .handler import process
