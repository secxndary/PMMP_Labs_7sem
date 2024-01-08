using System.Threading.Tasks;
using UnityEngine;

public class CubeMoving : MonoBehaviour
{
    public float speed;

    // Start is called before the first frame update
    async void Start()
    {
        float posX = transform.position.x;
        float posY = transform.position.y;
        float posZ = transform.position.z;


        for(;;)
        {
            posX = transform.position.x;
            posY = transform.position.y;
            posZ = transform.position.z;

            transform.position = new Vector3(posX, posY + speed, posZ);
            await Task.Delay(3000);
            
            if (this == null)
                break;
        }
    }

    // Update is called once per frame
    void Update()
    {

    }
}
