using UnityEngine;

public class NPCAI : MonoBehaviour
{
    public enum State { IDLE, WALKING, CHASING, ATTACKING }
    public State currentState = State.IDLE;

    void Update()
    {
        switch (currentState)
        {
            case State.IDLE:
                Idle();
                break;
            case State.WALKING:
                Walk();
                break;
            case State.CHASING:
                Chase();
                break;
            case State.ATTACKING:
                Attack();
                break;
        }
    }

    void Idle()
    {
        // The NPC is idle. They might wait for a certain amount of time, or wait for the player to come close.
        // If the player comes close, transition to the CHASING state
        if (PlayerIsClose())
            currentState = State.CHASING;
    }

    void Walk()
    {
        // The NPC is walking. They might patrol a specific area, or move randomly.
        // If the player comes close, transition to the CHASING state
        if (PlayerIsClose())
            currentState = State.CHASING;
    }

    void Chase()
    {
        // The NPC is chasing the player. They might follow the player, or move towards them.
        // If the player is too far away, transition back to the IDLE state
        // If the player is close enough, transition to the ATTACKING state
        if (!PlayerIsClose())
            currentState = State.IDLE;
        else if (PlayerIsInAttackRange())
            currentState = State.ATTACKING;
    }

    
    void Attack()
{
    if (PlayerIsInAttackRange())
    {
        // Choose a random attack move
        int move = Random.Range(0, 3); // 0, 1, 2
        switch (move)
        {
            case 0:
                // Perform a basic attack
                BasicAttack();
                break;
            case 1:
                // Perform a heavy attack
                HeavyAttack();
                break;
            case 2:
                // Perform a special attack
                SpecialAttack();
                break;
        }
    }
    else
    {
        // Transition back to the CHASING state
        currentState = State.CHASING;
    }
}

void BasicAttack()
{
    // Perform a basic attack animation and deal damage to the player
}

void HeavyAttack()
{
    // Perform a heavy attack animation and deal more damage to the player
}

void SpecialAttack()
{
    // Perform a special attack animation and deal unique damage or effects to the player
}


    bool PlayerIsClose()
    {
        // Return true if the player is close, false otherwise
    }

    bool PlayerIsInAttackRange()
    {
        // Return true if the player is in attack range, false otherwise
    }
}
