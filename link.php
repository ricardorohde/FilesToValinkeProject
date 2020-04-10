<?php

if (isset($_GET["link"]))
{
    validaLink($_GET["link"]);  
}
else
{
	$data = array(
	   "data" => array(
		    "preco" => "",
		    "link" => "",
		    "nome" => "",
		    "vendedor" => "",
		    "linkimagem" => "",
		    "loja" => "",
		    "vendidos" => "",
		    "estoqueAtual" => "",
		    "estoqueInicial" => "",
		    "status_link" => 1
	   ),
	   "erro" => true,
	   "erroMessage" => "Nenhum link recebido",
	   "status" => 200
	);
	$json_data = json_encode($data);
	print_r($json_data);
	return;
}


function validaLink($product_link_received)
{
	if(IsValidMarketPlace($product_link_received))
	{
		
		$product_link = str_replace("/", "{+}", $product_link_received);

		for($i = 0; $i < 3; $i++)
		{
			// Chamando Robô 
			$url_completa = "http://localhost:5060/" . $product_link;

			// Recebendo dados do Robô
			$data_received = file_get_contents($url_completa);

			// Json com dados do Robô
			$robotInfo = json_decode($data_received);

			if($robotInfo->erro == true)
			{
				$data = array(
							   "data" => array(
								    "preco" => "",
								    "link" => $robotInfo->link,
								    "nome" => "",
								    "vendedor" => "",
								    "linkimagem" => "",
								    "loja" => "",
								    "vendidos" => "",
								    "estoqueAtual" => "",
								    "estoqueInicial" => "",
								    "status_link" => 1
							   ),
							   "erro" => false,
							   "erroMessage" => "",
							   "status" => 200
							);
			}
			else
			{
				break;
			}	
		}
		if($robotInfo->erro == false && $robotInfo->nome == null)
		{
			$data = array(
							   "data" => array(
								    "preco" => "",
								    "link" => $robotInfo->link,
								    "nome" => "",
								    "vendedor" => "",
								    "linkimagem" => "",
								    "loja" => "",
								    "vendidos" => "",
								    "estoqueAtual" => "",
								    "estoqueInicial" => "",
								    "status_link" => 1
							   ),
							   "erro" => false,
							   "erroMessage" => "",
							   "status" => 200
							);
		}
		if($robotInfo->erro == false && $robotInfo->nome !== null)
		{
			
			//echo "DADOS ROBÔ: <br>";
			//echo "Nome: " . $robotInfo->nome . '<br>'; 
			//echo "Preço: " . $robotInfo->preco . '<br>';
			//echo "Link: " . $robotInfo->link . '<br>';
			//echo "Vendedor: " . $robotInfo->vendedor . '<br>';

			/*
			$conn = ConnectToDatabase();

			$sql = "ALTER TABLE item ADD FULLTEXT(nome)";
			
			$conn->query($sql);

			//$array_robot_nome_t = explode(' ', $robotInfo->nome);
			//for($i = 0; $i < strlen($array_robot_nome_t); $i++)
			//{
			//	if(endsWith($array_robot_nome_t[$i], "ml"))
			//	{
			//		;
			//	}
			//}

			$busca_nome_produto = str_replace('ml', ' ml', $robotInfo->nome);
			$busca_nome_produto = str_replace(' - ', '+', $busca_nome_produto);

			$sql = "SELECT nome, preco_venda 
					FROM item
					WHERE MATCH (nome) AGAINST ('" . $busca_nome_produto . "' IN BOOLEAN MODE) LIMIT 1";


			$result = $conn->query($sql);

			// TABELA "ITEM"
			if ($result->num_rows > 0) 
			{
			    $row = $result->fetch_assoc();

			    $databaseInfo = array(
		    						"nome" => $row["nome"],
		    						"preco" => $row["preco_venda"],
		    						"erro" => false
			    				);


			    //echo "<br><br>DADOS DO BANCO:<br>";
		        //echo "Nome: " . $databaseInfo['nome'] . "<br>" . 
		        //	"Preco: " . $databaseInfo['preco'] . "<br>" .
		        //	"Erro: " . $databaseInfo['erro'];


		        //Convertendo valores R$ em float para verificação --------------------------
		        $preco_robo_string = str_replace(',', '.', explode(' ', $robotInfo->preco)[1]);
		        $preco_robo = floatval($preco_robo_string);
		        //echo "<br>PRECO ROBO: ";
		        //echo $preco_robo;

		        $preco_banco_string = str_replace(',', '.', explode(' ', $databaseInfo['preco'])[1]);
		        $preco_banco = floatval($preco_banco_string);
		        //echo "<br>PRECO BANCO: ";
		        //echo $preco_banco;
	        	// --------------------------------------------------------------------------

		        $array_robot_nome = explode(' ', $robotInfo->nome);
		        $array_banco_nome = explode(' ', $databaseInfo['nome']);

		        $nomes_iguais = 0;
		        foreach($array_banco_nome as $item_nome_banco)
		        {
		        	if(strlen($item_nome_banco) > 3)
		        	{
		        		foreach($array_robot_nome AS $item_nome_robot)
		        		{
		        			if($item_nome_banco == $item_nome_robot)
		        			{
		        				$nomes_iguais = $nomes_iguais + 1;
		        			}
		        		}
		        	}
		        }
		        //echo "<br><br>Quantidade de nomes iguais:" . $nomes_iguais;
		        if($nomes_iguais > 2)
		        {
		        	$validacao_nome_produto = true;
		        }
		        else
		        {
		        	$validacao_nome_produto = false;
		        }


		        if ($preco_banco == 0 || $validacao_nome_produto == false)
		        {*/
					$data = array(
							   "data" => array(
									"preco" => $robotInfo->preco,
								    "link" => $robotInfo->link,
								    "nome" => $robotInfo->nome,
								    "vendedor" => $robotInfo->vendedor,
								    "linkimagem" => $robotInfo->linkimagem,
								    "loja" => $robotInfo->loja,
								    "vendidos" => "",
								    "estoqueAtual" => "",
								    "estoqueInicial" => "",
								    "status_link" => 1
							   ),
							   "erro" => false,
							   "erroMessage" => "",
							   "status" => 200
							);

		        /*}
		        else if($preco_robo < $preco_banco - 1)
		        {
		        	$data = array(
							   "data" => array(
								    "preco" => $robotInfo->preco,
								    "link" => $robotInfo->link,
								    "nome" => $robotInfo->nome,
								    "vendedor" => $robotInfo->vendedor,
								    "linkimagem" => $robotInfo->linkimagem,
								    "loja" => $robotInfo->loja,
								    "vendidos" => "",
								    "estoqueAtual" => "",
								    "estoqueInicial" => "",
								    "status_link" => 0
							   ),
							   "erro" => false,
							   "erroMessage" => "",
							   "status" => 200
							);
		        }
		        else
		        {
		        	$data = array(
							   "data" => array(
								    "preco" => $robotInfo->preco,
								    "link" => $robotInfo->link,
								    "nome" => $robotInfo->nome,
								    "vendedor" => $robotInfo->vendedor,
								    "linkimagem" => $robotInfo->linkimagem,
								    "loja" => $robotInfo->loja,
								    "vendidos" => "",
								    "estoqueAtual" => "",
								    "estoqueInicial" => "",
								    "status_link" => 2
							   ),
							   "erro" => false,
							   "erroMessage" => "",
							   "status" => 200
							);	
		        }

		    }
			else
			{

				$data = array(
							   "data" => array(
								    "preco" => "",
								    "link" => $robotInfo->link,
								    "nome" => "",
								    "vendedor" => "",
								    "linkimagem" => "",
								    "loja" => "",
								    "vendidos" => "",
								    "estoqueAtual" => "",
								    "estoqueInicial" => "",
								    "status_link" => 1
							   ),
							   "erro" => false,
							   "erroMessage" => "",
							   "status" => 200
							);
				
				$databaseInfo = array(
		    						"nome" => "",
		    						"preco" => "",
		    						"erro" => false
		    					);

				//echo "<br><br>DADOS DO BANCO:<br>";
		        //echo "Nome: " . $databaseInfo->nome . "<br>" . 
		        //	"Preco: " . $databaseInfo->preco . "<br>" .
		        //	"Erro: " . $databaseInfo->erro;
			}

			$conn->close();
		*/}	
	}

	else
	{

		$data = array(
				   "data" => array(
					    "preco" => "",
					    "link" => $product_link_received,
					    "nome" => "",
					    "vendedor" => "",
					    "linkimagem" => "",
					    "loja" => "",
					    "vendidos" => "",
					    "estoqueAtual" => "",
					    "estoqueInicial" => "",
					    "status_link" => 1
				   ),
				   "erro" => false,
				   "erroMessage" => "",
				   "status" => 200
		);    
	}

	$json_data = json_encode($data);
	print_r($json_data);

}




function ConnectToDatabase()
{
	$servername = "localhost";
	$username = "root";
	$password = "root";
	$dbname = "hunterz";
	

	// Create connection
	$conn = new mysqli($servername, $username, $password, $dbname);
	// Check connection
	if ($conn->connect_error) {
	    die("Connection failed: " . $conn->connect_error);
	}

	return $conn;
}

function IsValidMarketPlace($link)
{
	if(strpos($link, 'mercadolivre.com'))
	{
		return True;
	}
	else if(strpos($link, 'submarino.com'))
	{
		return True;
	}
	else if(strpos($link, 'shoptime.com'))
	{
		return True;
	}
	else if(strpos($link, 'americanas.com'))
	{
		return True;
	}
	else if(strpos($link, 'magazineluiza.com'))
	{
		return True;
	}
	else if(strpos($link, 'casasbahia.com'))
	{
		return True;
	}
	return False;
}

?>
