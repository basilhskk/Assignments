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
    public partial class Bookstore : Form
    {
        public Bookstore()
        {
            InitializeComponent();
        }

        private void coffeebutton_Click(object sender, EventArgs e)
        {
            Cafe cafe = new Cafe();
            cafe.ShowDialog();
        }

        private void eshopbutton_Click(object sender, EventArgs e)
        {
            Eshop eshop = new Eshop();
            eshop.ShowDialog();
        }

        private void labbutton_Click(object sender, EventArgs e)
        {
            LabRoom lab = new LabRoom();
            lab.ShowDialog();
        }

        private void exitbutton_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
