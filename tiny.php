<?php
//@author carlos eduardo - ccedop@gmail.com
//@version php >= 5.4 
//requesito obrigatório: certificado SSL

class TinyERP extends Processador {

	const TINYERP = 'tiny';
	
	
	private $_apiKeyTinyERP="";//mudar para api de producao
    private $_endpointTiny="https://api.tiny.com.br/api2/";
    private $_parametros;
    public  $_apiType="content-type: application/x-www-form-urlencoded;charset=UTF-8";

public function consulta_geral_pedidos(){#Primeira função a ser chamada 
	
		
		//filtrar a consulta pela data informada entrada do pedido
		date_default_timezone_set('America/Sao_Paulo');
		$filtroDataDiaria=date('d/m/Y');
		$this->_parametros="token=".$this->_apiKeyTinyERP."&formato=JSON";
		$url=$this->_endpointTiny.'pedidos.pesquisa.php';
		//$dados=$this->_parametros."sort=ASC&dataInicialOcorrencia=".$filtroDataDiaria;
		$dados=$this->_parametros."&sort=ASC&dataInicial=27/07/2018&dataFinal=27/07/2018";
		//********************* NAO ESQUECER DE FORMATAR A PAGINACAO  ///////////
		$data=$this->headers_curl($url,$dados,self::METODO);
		
		$retorno=$this->setCurl($data,self::TINYERP);
		
		$pedidos=json_decode($retorno,true);
		print_r($pedidos);
		$status_cod=$pedidos['retorno']['status_processamento'];
		//$status_msg=$pedidos['retorno']['status'];
		
		if ($status_cod == '3') {
			$contagemPedidos=count($pedidos['retorno']['pedidos']);//æqui faz um loop
			
			for ($i=0;$i<$contagemPedidos;$i++) {
				
				$idCliente=$pedidos['retorno']['pedidos'][$i]['pedido']['id'];
				$nomeCliente=trim($pedidos['retorno']['pedidos'][$i]['pedido']['nome']);
				//$retornoConsultaPedido=$this->consulta_pedido_telefone($idCliente,$nomeCliente);
				//print_r($retornoConsultaPedido);
				//break;
			//fim for
			}
		// end if 
		}else{echo $status_msg=$pedidos['retorno']['status'];}
  

//fim consulta
}
public function formata_msg($origem,$nome_comprador){
	 
	 //os arquivos txt para modificacao textual estao na pasta Api
		$premsg='Olá '.$nome_comprador.', Como Vai ?'."\n";//primeira linha da mensagem
		$arquivo=fopen($origem,'r');
		$corpo = fread ($arquivo, filesize ($origem));
		$msg=nl2br($premsg . $corpo);
		fclose ($arquivo);
		
		return $msg;

	 }


public function msg_canais($filtro_canais,$nome_comprador){

	if ($filtro_canais == 'ML_EMPORIODOCELULAR' || $filtro_canais == 'ML_EMPORIODOSSMARTPHONE') {
		
		$origem='mercadolivre.txt';
		return $this->formata_msg($origem,$nome_comprador);
		
	}
	
	else {
		
		$origem='geral.txt';
		return $this->formata_msg($origem,$nome_comprador);
		
		
		}
	
	
	//fim function
	}
	
//possivelmente ocorrera uma chamda desta funcao dentro de um loop
//funcao sera usada pelo CLASS CHAT
public function consulta_pedido_telefone($idCliente,$nomeCliente){

		$url=$this->_endpointTiny."pedido.obter.php";
		$dados=$this->_parametros."&id=".(int)$idCliente;
		
		$data=$this->headers_curl($url,$dados,self::METODO);
		$retorno=$this->setCurl($data,self::TINYERP);
		
		$consulta=json_decode($retorno,true);
		print_r($consulta);
		$status_cod=$consulta['retorno']['status_processamento'];

		if ($status_cod == '3') 
		{
		//return $retorno;
		//********************TROCAR O FALSE POR TRUE *****************
		if(array_key_exists('ecommerce',$consulta['retorno']['pedido'])==false){
			
			
			$fone=trim($consulta['retorno']['pedido']['cliente']['fone']);
			if(preg_match("/^[(][0-9]{1,2}[)][ ][9][0-9]{1,4}[\-][0-9]{1,4}$/", $fone)==true)
			{
				$fone=preg_replace("/[(|)|\-| ]/", "", $fone);
					if(preg_match("/^[0-9]{1,11}$/", $fone)==true){
						//$canalVendaNome=trim($consulta['retorno']['pedido']['ecommerce']['canalVenda']);
						//return [$fone,$canalVendaNome];
						//return $fone;
					}
			
			}else{echo $status_msg=$pedidos['retorno']['status'];}
		}else{echo 'ERRO NAO EXISTE A CHAVE ECOMMERCE';}
	}

//fim pedido telefone
}

//fim class
}
