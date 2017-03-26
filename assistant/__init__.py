from .response import answer, eight_ball, last_tweet

fn_map = {}
fn_map['/answer'] = answer
fn_map['/ball'] = eight_ball
fn_map['/tweet'] = last_tweet


from .handler import process
