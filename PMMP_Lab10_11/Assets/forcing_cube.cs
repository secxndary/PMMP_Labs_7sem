using UnityEngine;

public class forcing_cube : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    void OnCollisionEnter(Collision col) 
    {
        if(col.gameObject.tag == "cubetag")
        {
            var randDir = new Vector3(Random.Range(-1f, 1f), 0, Random.Range(-1f, 1f));
            col.gameObject.GetComponent<Rigidbody>().AddForce(randDir * 1000);
        }
    }
}
