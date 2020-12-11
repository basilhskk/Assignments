using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace bookstore
{
    public partial class Printer : Form
    {
        public Printer()
        {
            InitializeComponent();
        }

        private void printbutton_Click(object sender, EventArgs e)
        {
            if ((colorbox.Text != "") && (sizebox.Text != ""))
            {
                if (copiesbox.Value != 0)
                {
                    System.Threading.Thread.Sleep(900);
                    MessageBox.Show("Print Successfully!", "Success!");
                    this.Close();
                }
                else
                {
                    MessageBox.Show("Select valid number of copies!", "Failed!");
                }
            }
            else
            {
                MessageBox.Show("Select color and size!", "Failed!");
            }
            
        }

        private void exitbutton_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
