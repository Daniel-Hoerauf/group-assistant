from .response import answer, eight_ball, last_tweet, weather, math, news, image

fn_map = {}
fn_map['/answer'] = answer
fn_map['/ball'] = eight_ball
fn_map['/tweet'] = last_tweet
fn_map['/weather'] = weather
fn_map['/math'] = math
fn_map['/news'] = news

from .handler import process
