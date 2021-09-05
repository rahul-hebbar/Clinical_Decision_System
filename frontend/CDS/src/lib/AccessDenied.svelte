<script>
	import { Link } from "svelte-routing";
	import warning from "../assets/warning.svg"
</script>

<div class="container">
	<div class="concen">
		<div class="heading"><img src={warning} alt="warning" class="svg" /></div>
		<h6 class="heading"> Access Denied </h6>
		<Link to="/authuser" replace={true}><h4> Please login/signup first </h4></Link>
	</div>
</div>	

<style>
	.svg {
		width: 100px;
		height: 100px;
	}
</style>