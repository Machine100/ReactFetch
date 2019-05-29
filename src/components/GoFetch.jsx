import React, {Component} from 'react';

class GoFetch extends Component {
	state = {
		worldview: 'https://s3.amazonaws.com/derffred/worldview.png'
	}
	
	addFood1() {
		fetch('https://tfbenvwogg.execute-api.us-east-1.amazonaws.com/stage1/addfood1')
	}

	addFood2() {
		fetch('https://tfbenvwogg.execute-api.us-east-1.amazonaws.com/stage1/addfood2')
	}

	addToy1()     {fetch('https://tfbenvwogg.execute-api.us-east-1.amazonaws.com/stage1/addtoy1')}
	addToy2()     {fetch('https://tfbenvwogg.execute-api.us-east-1.amazonaws.com/stage1/addtoy2')}
	addToy3()     {fetch('https://tfbenvwogg.execute-api.us-east-1.amazonaws.com/stage1/addtoy3')}
	removeFood1() {fetch('https://tfbenvwogg.execute-api.us-east-1.amazonaws.com/stage1/removefood1')}
	removeFood2() {fetch('https://tfbenvwogg.execute-api.us-east-1.amazonaws.com/stage1/removefood2')}
	removeToy1()  {fetch('https://tfbenvwogg.execute-api.us-east-1.amazonaws.com/stage1/removetoy1')}
	removeToy2()  {fetch('https://tfbenvwogg.execute-api.us-east-1.amazonaws.com/stage1/removetoy2')}
	removeToy3()  {fetch('https://tfbenvwogg.execute-api.us-east-1.amazonaws.com/stage1/removetoy3')}
	generateWorld() {
		fetch('https://tfbenvwogg.execute-api.us-east-1.amazonaws.com/stage1/generateworld')}

	render(){
		const {worldview} = this.state
		return(
			<React.Fragment>
				<img src={worldview} alt='' />
				<button onClick={this.addFood1}> add food1 </button>
				<button onClick={this.addFood2}> add food2 </button>
				<button onClick={this.addToy1}> add toy1 </button>
				<button onClick={this.addToy2}> add toy2 </button>
				<button onClick={this.addToy3}> add toy3 </button>
				<button onClick={this.removeFood1}> remove food1 </button>
				<button onClick={this.removeFood2}> remove food2 </button>
				<button onClick={this.removeToy1}> remove toy1 </button>
				<button onClick={this.removeToy2}> remove toy2 </button>
				<button onClick={this.removeToy3}> remove toy3 </button>
				<button onClick={this.generateWorld}> generate world </button>
			</React.Fragment>
		);
	}
}

export default GoFetch;


//inside the render is a return