using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ChangeColor : MonoBehaviour
{
    private Renderer r;

    void Start()
    {
        r = GetComponent<Renderer>();
    }

    // Update is called once per frame
    void Update()
    {
        var changeColor = Input.GetKey("f");

        if (changeColor)
        {
            r.material.color = RandomColor();
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
