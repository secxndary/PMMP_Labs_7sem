using UnityEngine;

public class MoveTo : MonoBehaviour
{
    public GameObject target;
    public Rigidbody rb;

    // Start is called before the first frame update
    void Start()
    {
        rb = GetComponent<Rigidbody>();
    }

    // Update is called once per frame
    void Update()
    {
        rb.AddForce(0, 1000, 0);
        transform.position = Vector3.MoveTowards(transform.position, target.transform.position, Time.deltaTime);
    }
}
