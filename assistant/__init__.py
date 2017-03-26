from .response import answer, eight_ball, last_tweet, weather

fn_map = {}
fn_map['/answer'] = answer
fn_map['/ball'] = eight_ball
fn_map['/tweet'] = last_tweet
fn_map['/weather'] = weather


from .handler import process
