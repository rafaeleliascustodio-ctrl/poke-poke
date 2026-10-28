// Assets/_Projeto/Scripts/Editor/AnimationFoldersCreator.cs
#if UNITY_EDITOR
using UnityEditor;
using UnityEngine;

namespace Projeto.EditorTools
{
    /// <summary>
    /// Cria a estrutura de pastas de animações do projeto via menu do Editor.
    /// Menu: Projeto > Criar Pastas de Animação
    /// </summary>
    public static class AnimationFoldersCreator
    {
        // Pasta raiz onde tudo será criado
        private const string RaizAnimations = "Assets/_Projeto/Animations";

        // Subpastas relativas à raiz (suportam níveis aninhados, ex.: "Player/Clips")
        private static readonly string[] Subpastas =
        {
            "Player/Clips",
            "NPC/Clips",
            "Overworld",
            "Battle",
            "Transitions"
        };

        [MenuItem("Projeto/Criar Pastas de Animação")]
        public static void CriarPastas()
        {
            int criadas = 0;
            int jaExistiam = 0;

            // Garante que a raiz (Assets/_Projeto/Animations) exista
            if (!GarantirPasta(RaizAnimations, ref criadas, ref jaExistiam))
            {
                Debug.LogError($"[AnimationFoldersCreator] Não foi possível criar '{RaizAnimations}'.");
                return;
            }

            // Cria cada subpasta, nível por nível
            foreach (string subpasta in Subpastas)
            {
                string caminhoCompleto = $"{RaizAnimations}/{subpasta}";

                if (!GarantirPasta(caminhoCompleto, ref criadas, ref jaExistiam))
                {
                    Debug.LogError($"[AnimationFoldersCreator] Falha ao criar '{caminhoCompleto}'.");
                }
            }

            // Atualiza o Project Window
            AssetDatabase.Refresh();

            Debug.Log($"[AnimationFoldersCreator] Concluído. Criadas: {criadas} | Já existiam: {jaExistiam}");
        }

        /// <summary>
        /// Garante que um caminho (ex.: "Assets/A/B/C") exista, criando cada nível ausente.
        /// Retorna true se o caminho final é válido ao término.
        /// </summary>
        private static bool GarantirPasta(string caminho, ref int criadas, ref int jaExistiam)
        {
            // Se já existe, não faz nada
            if (AssetDatabase.IsValidFolder(caminho))
            {
                jaExistiam++;
                return true;
            }

            // Percorre os níveis, criando os que faltam
            string[] partes = caminho.Split('/');
            string atual = partes[0]; // "Assets"

            for (int i = 1; i < partes.Length; i++)
            {
                string proximo = $"{atual}/{partes[i]}";

                if (!AssetDatabase.IsValidFolder(proximo))
                {
                    // CreateFolder(pastaPai, nomeNovaPasta) retorna o GUID da nova pasta
                    string guid = AssetDatabase.CreateFolder(atual, partes[i]);

                    if (string.IsNullOrEmpty(guid))
                    {
                        return false;
                    }

                    criadas++;
                    Debug.Log($"[AnimationFoldersCreator] Criada: {proximo}");
                }

                atual = proximo;
            }

            return AssetDatabase.IsValidFolder(caminho);
        }
    }
}
#endif