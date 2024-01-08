using UnityEngine;

public class Moving : MonoBehaviour
{
    public GameObject surface;
    public float speed = 10;
    public bool useTransform = false;
    private float startY;
    private Rigidbody rb;
    private Vector3 lastDir = new (0,0,0); 

    private int multiplier = 100;
    
    void Start()
    {
        rb = GetComponent<Rigidbody>();
        startY = transform.position.y;
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
        var force = new Vector3(
            (moveHL ? -1 : 0) + (moveHR ? 1 : 0),
            jump && startY > transform.position.y ? 10 : 0,
            (moveVU ? 1 : 0) + (moveVD ? -1 : 0)
        );

        var rotateDir = new Vector3(
            (moveVU ? -1 : 0) + (moveVD ? 1 : 0),
            0,
            (moveHL ? -1 : 0) + (moveHR ? 1 : 0)
        );

        // rotate player to direction
        if (rotateDir.x != 0 || rotateDir.z != 0)
        {
            transform.rotation = Quaternion.LookRotation(rotateDir);
        }

        // apply force to rigidbody
        if (useTransform)
        {
            // apply force to transform
            transform.Translate(force * speed * Time.deltaTime);
            return;
        }
        else {
            rb.velocity = new Vector3(0, rb.velocity.y, 0);
            //rb.angularVelocity = Vector3.zero;
            // new cool formula :D             
            rb.AddForce(new Vector3(force.x * speed * multiplier, force.y * speed, force.z * speed * multiplier));

            // if(force.x != lastDir.x || force.z != lastDir.z)
            // {
            //     rb.AddForce(force * speed * 20);
            // }
            // else
            //     rb.AddForce(force * speed);
        }

        lastDir = force;
    }
}
