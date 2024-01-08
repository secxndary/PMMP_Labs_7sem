using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class create_sphere_logic : MonoBehaviour
{
    public GameObject redSpherePrefab;
    public GameObject redContainer;
    public GameObject purplePrefab;
    public GameObject greenSpherePrefab;
    public GameObject greenContainer;
    public GameObject purpleContainer;
    public GameObject floor;
    public int maxRed = 5;
    public float redSpawnCooldown = 1f;  // Set the cooldown time for red spheres
    public float greenSpawnCooldown = 2f;  // Set the cooldown time for green spheres
    public float purpleSpawnCooldown = 5f;

    public GameObject player;

    private float lastRedSpawnTime = 0f;
    private float lastGreenSpawnTime = 0f;
    private float lastPurpleSpawnTime = 0f;

    // Start is called before the first frame update
    void Start()
    {
    }

    // Update is called once per frame
    void Update()
    {
        if (Time.time - lastRedSpawnTime > redSpawnCooldown && redContainer.transform.childCount < maxRed)
        {
            var x = Random.Range(floor.transform.position.x - floor.transform.localScale.x / 2, floor.transform.position.x + floor.transform.localScale.x / 2);
            var y = floor.transform.position.y + 0.7f;
            var z = Random.Range(floor.transform.position.z - floor.transform.localScale.z / 2, floor.transform.position.z + floor.transform.localScale.z / 2);

            var newSphere = Instantiate(redSpherePrefab, redContainer.transform);
            newSphere.transform.position = new Vector3(x, y, z);

            lastRedSpawnTime = Time.time;
        }

        if (Time.time - lastGreenSpawnTime > greenSpawnCooldown && greenContainer.transform.childCount < 5)
        {
            var x = Random.Range(floor.transform.position.x - floor.transform.localScale.x / 2, floor.transform.position.x + floor.transform.localScale.x / 2);
            var y = floor.transform.position.y + 0.7f;
            var z = Random.Range(floor.transform.position.z - floor.transform.localScale.z / 2, floor.transform.position.z + floor.transform.localScale.z / 2);

            var newSphere = Instantiate(greenSpherePrefab, greenContainer.transform);
            newSphere.transform.position = new Vector3(x, y, z);

            lastGreenSpawnTime = Time.time; 
        }

        if (Time.time - lastPurpleSpawnTime > purpleSpawnCooldown && purpleContainer.transform.childCount < 5)
        {
            var x = Random.Range(floor.transform.position.x - floor.transform.localScale.x / 2, floor.transform.position.x + floor.transform.localScale.x / 2);
            var y = floor.transform.position.y + 0.7f;
            var z = Random.Range(floor.transform.position.z - floor.transform.localScale.z / 2, floor.transform.position.z + floor.transform.localScale.z / 2);

            var duck = Instantiate(purplePrefab, purpleContainer.transform);
            duck.GetComponentInChildren<PurpleBoyLogic>().player = player;
            duck.transform.position = new Vector3(x, y, z);
            duck.transform.rotation = Quaternion.Euler(0, Random.Range(0, 360), 0);

            lastPurpleSpawnTime = Time.time;
        }
    }
}
