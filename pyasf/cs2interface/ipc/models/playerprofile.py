from pydantic import BaseModel


class Medals(BaseModel):
    display_items_defidx: list[int]
    featured_display_item_defidx: int


class Ranking(BaseModel):
    account_id: int
    rank_id: int
    wins: int
    rank_type_id: int
    per_map_rank: list | None


class Commendation(BaseModel):
    cmd_friendly: int
    cmd_teaching: int
    cmd_leader: int


class Profile(BaseModel):
    account_id: int
    ongoingmatch: None
    global_stats: None
    ranking: Ranking | None
    commendation: Commendation | None
    medals: Medals | None
    my_current_event: None
    my_current_event_teams: list
    my_current_team: None
    my_current_event_stages: list
    activity: None
    player_level: int
    player_cur_xp: int
    rankings: list[Ranking]


class PlayerProfile(BaseModel):
    account_profiles: list[Profile]
