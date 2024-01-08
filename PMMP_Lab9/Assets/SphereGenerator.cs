using System.Net.Mail;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SphereGenerator : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        var mouseClicked = Input.GetMouseButtonDown(0);

        if (mouseClicked)
        {
            var sphere = GameObject.CreatePrimitive(PrimitiveType.Sphere);
            sphere.transform.position = new Vector3(0, Random.Range(2, 15), 0);
            sphere.AddComponent<Rigidbody>();
            sphere.AddComponent<ChangeColor>();
            sphere.GetComponent<Renderer>().material.color = RandomColor();
        }
    }

    private Color RandomColor()
    {
        float r = Random.value; // Random red component between 0 and 1
        float g = Random.value; // Random green component between 0 and 1
        float b = Random.value; // Random blue component between 0 and 1

        return new Color(r, g, b);
    }
}
