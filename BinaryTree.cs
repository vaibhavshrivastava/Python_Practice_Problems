using System;
namespace gitrepo
{
    public class TreeNode
    {
        public int data;
        public TreeNode left;
        public TreeNode right; 

        public TreeNode(int data)
        {
        this.data=data;
        this.left= this.right=null;
        }       
    }
    public class BinaryTree
    {
        // Find max element in a binary tree

        public int FindMaxInbinaryTree( TreeNode root)
        {
            int rightMax, leftMax, max = Int16.MinValue;
            if(root is null)
            {
                return -1;
            }
            else
            {
                leftMax=FindMaxInbinaryTree(root.left);
                rightMax=FindMaxInbinaryTree(root.right);
                if(leftMax>rightMax)
                {
                    max=leftMax;
                }
                else max=rightMax;
                if(root.data>max)
                return root.data;
                else return max;           
            }
            
        }

        public void Test_FindMaxInBinaryTree()
        {
        TreeNode root = new TreeNode(2); 
        root.left = new TreeNode(7); 
        root.right = new TreeNode(5); 
        root.left.right = new TreeNode(6); 
        root.left.right.left = new TreeNode(1); 
        root.left.right.right = new TreeNode(11); 
        root.right.right = new TreeNode(9); 
        root.right.right.left = new TreeNode(4); 

        System.Console.WriteLine("Max value in the binary tree is " + FindMaxInbinaryTree(root).ToString());
        }
    }
}