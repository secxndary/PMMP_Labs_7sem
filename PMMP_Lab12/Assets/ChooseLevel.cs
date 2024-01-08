using UnityEngine;
using UnityEngine.SceneManagement;

public class ChooseLevel : MonoBehaviour
{
    public void LoadLevel(int id) 
    {
        SceneManager.LoadScene(id);
    }
}
