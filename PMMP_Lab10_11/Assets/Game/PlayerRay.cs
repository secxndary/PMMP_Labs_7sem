using UnityEngine;

public class PlayerRay : MonoBehaviour
{
    public float distance = 10;
    public GameObject player;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        var moveHL = Input.GetKey("a");
        var moveHR = Input.GetKey("d");
        var moveVU = Input.GetKey("w");
        var moveVD = Input.GetKey("s");

        var jump = Input.GetKey("space");

        // calculate force for all at the same time lokking to camera direction
        var playerDir = new Vector3(
            (moveHL ? -1 : 0) + (moveHR ? 1 : 0),
            0,
            (moveVU ? 1 : 0) + (moveVD ? -1 : 0)
        );

        var ray = new Ray(transform.position, playerDir * distance);
        Debug.DrawRay(transform.position, playerDir * distance, Color.green);

        if(Physics.Raycast(ray, out var hit, distance)) 
        {
            if(hit.collider.gameObject.tag == "purple") 
            {
                player.GetComponent<PlayerLogic>().currentScore++;
                Destroy(hit.collider.gameObject);
            }
        }
        
    }
}
