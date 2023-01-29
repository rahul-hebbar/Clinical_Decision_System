<script>
	import { 
		Content,
		Tile,
		Grid,
		Row,
		Column,
		Icon
	} from "carbon-components-svelte";
	import { Link } from "svelte-routing";
	import LoginTemp from "./LoginTemp.svelte";
	import SignUpTemp from "./SignUpTemp.svelte";
	import Home32 from "carbon-icons-svelte/lib/Home32"

</script>

<div class="container">
	<div class="concen">
		<Tile>
			<div class="tile-con">
				<h3 class="heading"> "For Doctors only" => else => 
					<Link to="/"><Icon render={Home32} /></Link>
				</h3>
				<br />
				<Grid>
					<Row>
						<Column sm={8} md={8} lg={7}>
							<LoginTemp />
						</Column>
						<Column sm={0} md={0} lg={1}>
								<div class="line"></div>
						</Column>
						<Column sm={8} md={8} lg={7}>
							<SignUpTemp />
						</Column>
					</Row>
				</Grid>
			</div>
		</Tile>
	</div>
</div>

<style>
	.line {
		border-left: 3px solid #9CC3D5FF;
		height: 300px;
	}
	.tile-con {
		width: 70vw;
	}
</style>