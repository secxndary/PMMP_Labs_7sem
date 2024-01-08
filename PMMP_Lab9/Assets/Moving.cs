using UnityEngine;

public class Moving : MonoBehaviour
{
    public Rigidbody rb;
    public GameObject surface;
    public float speed = 10;
    public bool useTransform = false;
    private float startY;
    
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

        if (useTransform)
        {
            // apply force to transform
            transform.Translate(force * speed * Time.deltaTime);
            return;
        }

        // apply force
        rb.AddForce(force * speed);
    }
}
