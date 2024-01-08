using System.Collections;
using System.Collections.Generic;
using TMPro;
using Unity.VisualScripting;
using UnityEngine;

public class PlayerLogic : MonoBehaviour
{
    private Vector3 _startPos;
    private Rigidbody _rb;
    public TMP_Text currentScoreText; 
    public TMP_Text maxScoreText; 

    public int currentScore = 0;
    private int maxScore = 0;

    // Start is called before the first frame update
    void Start()
    {
        _startPos = transform.position;
        _rb = GetComponent<Rigidbody>();
    }

    // Update is called once per frame
    void Update()
    {
        currentScoreText.text = currentScore.ToString();
        maxScoreText.text = $"max: {maxScore}";

        bool rPressed = Input.GetKeyDown(KeyCode.R);
        if (rPressed) 
        {
            GotoStart();
        }
    }

    void OnCollisionEnter(Collision col) 
    {
        switch(col.gameObject.tag) 
        {
            case "red":
                col.gameObject.GetComponent<RedSphere>().isDestroyed = true;
                GotoStart();
                break;
            case "green":
                var isDestroyed = col.gameObject.GetComponent<GreenCapsule>().IsDestroyed;
                col.gameObject.GetComponent<GreenCapsule>().IsDestroyed = true;
                currentScore += 10;
                if(!isDestroyed)
                    Destroy(col.gameObject);
                break;
        }
    }

    public void GotoStart() {
        if(currentScore > maxScore)
            maxScore = currentScore;

        currentScore = 0;
        transform.position = _startPos;
        _rb.velocity = Vector3.zero;
    }
}
