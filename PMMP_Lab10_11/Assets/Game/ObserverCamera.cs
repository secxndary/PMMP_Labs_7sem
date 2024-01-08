using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ObserverCamera : MonoBehaviour
{
    public GameObject target;
    public float xOffset = 0;
    public float yOffset = 10;
    public float zOffest = 0;
    private Vector3 lastPos;

    // Start is called before the first frame update
    void Start()
    {
        lastPos = target.transform.position;
    }

    // Update is called once per frame
    void Update()
    {
        if(lastPos.Equals(target.transform.position))
            return;

        var newPos = new Vector3(target.transform.position.x + xOffset, target.transform.position.y + yOffset, target.transform.position.z + zOffest);
        transform.position = newPos;
    }
}
