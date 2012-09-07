<?php

class Randomizer
{
	const METHOD_MAX = 3; // Number of defined custom methods
	const METHOD_RATE = 3; // 1/X % chance to not use the default
	const TRACKING_MAX = 10; //  Don't duplicate the last x results
	const TYPE_DEFAULT = 'default';
	const TYPE_FORCED = 'forced';
	const TYPE_1 = 'Country';
	const TYPE_2 = 'Terms';
	const TYPE_3 = 'Featured';

	public $beer;
	public $movie;
	public $type;
	public $meta;
	public $bIds;
	public $mIds;
	public $nfData;

	/**
	* Function to randomly determine which Randomizer method to use to create a pairing
	* @param array $bIds [optional] Array of beer ids
	* @param array $mIds [optional] Array of movie ids
	* @return Randomizer
	*/
	public static function pickOne(array $bIds = null, array $mIds = null)
	{
		$defaultTest = rand(1,self::METHOD_RATE);
		$method = ($defaultTest == self::METHOD_RATE) ? rand(1,self::METHOD_MAX) : 'Default';
		$return = new self($bIds, $mIds);
		call_user_func(array($return,'method'.$method));
		$return->nfData = Netflix::catalogDetail($return->movie->nfid);
		return $return;
	}

	/**
	* Constructor
	* @param array $bIds [optional] Array of beer ids
	* @param array $mIds [optional] Array of movie ids
	* @return void
	*/
	public function __construct(array $bIds = null, array $mIds = null)
	{
		$this->bIds = $bIds ? $bIds : array();
		$this->mIds = $mIds ? $mIds : array();
	}

	/**
	* Default Randomizer method -- Slot Machine Mode
	* @return Randomizer
	*/
	public function methodDefault()
	{
		$this->movie = self::getRandomModel('Movie', Doctrine::getTable('Movie')->getExclusionQuery($this->mIds));
		$this->beer = self::getRandomModel('Beer', Doctrine::getTable('Beer')->getExclusionQuery($this->bIds));
		$this->type = self::TYPE_DEFAULT;
		$this->meta = 'unknown mystical forces';
		return $this;
	}

	/**
	* Method 1 -- Match beer brewery country to a movie genre (foreign movie)
	* @return Randomizer
	*/
	public function method1()
	{
		$this->type = self::TYPE_1;
		$this->movie = null;
		$beerId = null;
		while(!$this->movie)
		{
			$query = Doctrine::getTable('Beer')->getByIdForeignQuery($this->bIds);
			$this->beer = self::getRandomModel('Beer', $query);
			if(!$this->beer || $this->beer->id == $beerId)
			{
				return $this->methodDefault();
			}

			$country = sfCultureInfo::getInstance()->getCountry($this->beer->Brewery->country);
			$query = Doctrine::getTable('Movie')->getIdByGenreQuery($country, $this->mIds);

			$this->meta = strpos($country, 'United') === 0 ? "The ".$country : $country;
			$this->movie = self::getRandomModel('Movie', $query);
			$beerId = $this->beer->id;
		}
		return $this;
	}

	/**
	* Method 2 -- Match beer to movie by keyword matches across text fields
	* @return Randomizer
	*/
	public function method2()
	{
		$this->type = self::TYPE_2;
		$this->movie = null;
		$beerId = null;
		while(!$this->movie)
		{
			$this->beer = self::getRandomModel('Beer', Doctrine::getTable('Beer')->getExclusionQuery($this->bIds));
			if(!$this->beer || $this->beer->id == $beerId)
			{
				return $this->methodDefault();
			}
			$country = sfCultureInfo::getInstance()->getCountry($this->beer->Brewery->country);
			$search = array(
				$this->beer->label,
				$this->beer->Style->style,
				$this->beer->Brewery->name,
				$country,
			);
			$query = Doctrine::getTable('Movie')->getIdByKeywordQuery(implode(' ', $search), $this->mIds);
			$this->meta = 'magical coincidence';
			$this->movie = self::getRandomModel('Movie', $query);
			$beerId = $this->beer->id;
		}
		return $this;
	}

	/**
	* Method 3 -- Fetch a FeaturedPair
	* @return Randomizer
	*/
	public function method3()
	{
		$featuredPair = self::getRandomModel('FeaturedPair', Doctrine::getTable('FeaturedPair')->getExclusionQuery($this->bIds, $this->mIds));
		if(!$featuredPair)
		{
			return $this->methodDefault();
		}
		$this->type = self::TYPE_3;
		$this->movie = $featuredPair->Movie;
		$this->beer = $featuredPair->Beer;
    if(!empty($featuredPair->meta))
    {
        $this->meta = $featuredPair->meta;
    }
    else
    {
    	$this->meta = 'insane elves who think these two things go together';
    }

		return $this;
	}

	/**
	* Method to get a random id from a supplied model class and retrieve that object
	* @param string $model Class name
	* @param Doctrine_Query $q Supply a custom query for id filtering
	* @return Object based on Class name
	*/
	public static function getRandomModel($model, $q = null)
	{
		$model = (string) ucfirst($model);
		if(class_exists($model))
		{
			if(is_null($q))
			{
				$q = Doctrine_Query::create()
					->select('id')
					->from($model);
			}

			$i = 1;
			foreach($q->fetchArray() as $row)
			{
				$ids[$i] = $row['id'];
				$i++;
			}
			if(isset($ids))
			{
				$key = rand(1, count($ids));
				return Doctrine::getTable($model)->find($ids[$key]);
			}
		}

		return null;
	}

}
