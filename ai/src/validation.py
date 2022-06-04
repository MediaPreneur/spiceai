from typing import Dict


def validate_rewards(action_rewards: Dict[str, str], external_reward_funcs: str) -> bool:
    return (
        True
        if external_reward_funcs
        else not any(
            "reward =" not in value
            and "reward=" not in action_rewards[action_name]
            for action_name, value in action_rewards.items()
        )
    )
