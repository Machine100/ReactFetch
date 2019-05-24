import React, {Component} from 'react';

class GoFetch extends Component {
	state = {
		monsterpic: 'https://s3.amazonaws.com/derffred/outputdestination.png'
	}
	
	addFood1() {console.log('food1');}
	addFood2() {console.log('food2');}
	addToy1()  {console.log('toy1');}
	addToy2()  {console.log('toy2');}
	addToy3()  {console.log('toy3');}


	render(){
		const {monsterpic} = this.state
		return(
			<React.Fragment>
				<img src={monsterpic} alt='' />
				<button onClick={this.addFood1}> addfood1 </button>
				<button onClick={this.addFood2}> addfood2 </button>
				<button onClick={this.addToy1}> addtoy1 </button>
				<button onClick={this.addToy2}> addtoy2 </button>
				<button onClick={this.addToy3}> addtoy3 </button>
			</React.Fragment>
		);
	}
}

export default GoFetch;


//inside the render is a return