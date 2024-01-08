using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class UpdateColor : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    void OnTriggerEnter(Collider col) 
    {
        col.gameObject.GetComponent<Renderer>().material.color = RandomColor();
    }

    private Color RandomColor()
    {
        float r = Random.value;
        float g = Random.value;
        float b = Random.value;

        return new Color(r, g, b);
    }
}
