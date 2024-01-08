using UnityEngine;

public class PurpleBoyLogic : MonoBehaviour
{
    public GameObject player;
    public float distance = 5;

    private Rigidbody rb;
    
    void Start()
    {
        rb = GetComponent<Rigidbody>();   
        //rotate to player
        transform.rotation = Quaternion.LookRotation(player.transform.position - transform.position);
    }

    // Update is called once per frame
    void Update()
    {
        if(player == null)
            return;
        Vector3 directionToPlayer = (player.transform.position - transform.position).normalized;
        Ray ray = new Ray(transform.position, directionToPlayer);
        RaycastHit hit;

        if (Physics.Raycast(ray, out hit, distance))
        {
            if(hit.collider.gameObject.tag != "Player")
                return;
                
            //rotate to player
            transform.rotation = Quaternion.LookRotation(directionToPlayer);

            rb.velocity = Vector3.zero;
            rb.angularVelocity = Vector3.zero;
            rb.AddForce(directionToPlayer * 200);
        }
        else 
        {
            rb.velocity = Vector3.zero;
            rb.angularVelocity = Vector3.zero;
        }
    }

    void OnCollisionEnter(Collision col)
    {
        if(col.gameObject.tag == "Player")
        {
            var pl = col.gameObject.GetComponent<PlayerLogic>();
            if(pl != null)
                pl.GotoStart();
        }
    }
}
