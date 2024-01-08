using System.Collections;
using System.Collections.Generic;
using System.Threading.Tasks;
using Unity.VisualScripting;
using UnityEngine;

public class RedSphere : MonoBehaviour
{
    public int speed = 10000;
    public float speedMultiplier = 1.1f;
    public int maxBound = 10;
    private int _bound = 0;
    public bool isDestroyed = false;

    // Start is called before the first frame update
    async void Start()
    {
        await Task.Delay(300);
        var randDir = new Vector3(Random.Range(-1f, 1f), 0, Random.Range(-1f, 1f));
        var r = GetComponent<Rigidbody>();
        r.AddForce(randDir * speed);

        await Task.Delay(60000);
        if(!isDestroyed && gameObject != null)
            Destroy(gameObject);
    }

    // Update is called once per frame
    void Update()
    {
    }

    void OnCollisionEnter(Collision col)
    {
        if(isDestroyed || gameObject == null)
            return;

        speed = (int)(speed * speedMultiplier);

        var randDir = new Vector3(Random.Range(-1f, 1f), 0, Random.Range(-1f, 1f));
        var randRot = new Vector3(Random.Range(-1f, 1f), Random.Range(-1f, 1f), Random.Range(-1f, 1f));
        var r = GetComponent<Rigidbody>();
        r.AddForce(randDir * speed);
        r.AddTorque(randRot * speed * 1000);

        if(_bound > maxBound && !isDestroyed && gameObject != null)
        {
            isDestroyed = true;
            Destroy(gameObject);
        }
        _bound++;
    }
}
