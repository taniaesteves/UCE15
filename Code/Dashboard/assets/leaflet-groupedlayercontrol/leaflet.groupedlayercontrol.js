/* global L */

// A layer control which provides for layer groupings.
// Author: Ishmael Smyrnow
var group0;
var group1;

L.Control.GroupedLayers = L.Control.extend({
  
  options: {
    collapsed: true,
    position: 'topright',
    autoZIndex: true
  },

  initialize: function (baseLayers, groupedOverlays, options) {
    var i, j;
    L.Util.setOptions(this, options);

    this._layers = {};
    this._lastZIndex = 0;
    this._handlingClick = false;
    this._groupList = [];
    this._domGroups = [];

    for (i in baseLayers) {
      this._addLayer(baseLayers[i], i);
    }

    for (i in groupedOverlays) {
      for (var j in groupedOverlays[i]) {
        
        if (i == 'Points of Interest') {
          this._addLayer(groupedOverlays[i][j], j, i, true, "All");          
        }
        else if (i == 'Delta') {
          this._addLayer(groupedOverlays[i][j], j, i, true, "LastMonth");          
        }          
          
      }
    }
  },

  onAdd: function (map) {
    this._initLayout();
    this._update();

    map
        .on('layeradd', this._onLayerChange, this)
        .on('layerremove', this._onLayerChange, this);

    return this._container;
  },

  onRemove: function (map) {
    map
        .off('layeradd', this._onLayerChange)
        .off('layerremove', this._onLayerChange);
  },

  addBaseLayer: function (layer, name) {
    this._addLayer(layer, name);
    this._update();
    return this;
  },

  addOverlay: function (layer, name, group, type) {
    this._addLayer(layer, name, group, true, "overlay", type);
    this._update();
    return this;
  },

  removeLayer: function (layer) {
    var id = L.Util.stamp(layer);
    delete this._layers[id];
    this._update();
    return this;
  },

  _initLayout: function () {
    var className = 'leaflet-control-layers',
        container = this._container = L.DomUtil.create('div', className);

    //Makes this work on IE10 Touch devices by stopping it from firing a mouseout event when the touch is released
    container.setAttribute('aria-haspopup', true);

    if (!L.Browser.touch) {
      L.DomEvent.disableClickPropagation(container);
      L.DomEvent.on(container, 'wheel', L.DomEvent.stopPropagation);
    } else {
      L.DomEvent.on(container, 'click', L.DomEvent.stopPropagation);
    }

    var form = this._form = L.DomUtil.create('form', className + '-list');

    if (this.options.collapsed) {
      if (!L.Browser.android) {
        L.DomEvent
            .on(container, 'mouseover', this._expand, this)
            .on(container, 'mouseout', this._collapse, this);
      }
      var link = this._layersLink = L.DomUtil.create('a', className + '-toggle', container);
      link.href = '#';
      link.title = 'Layers';

      if (L.Browser.touch) {
        L.DomEvent
            .on(link, 'click', L.DomEvent.stop)
            .on(link, 'click', this._expand, this);
      }
      else {
        L.DomEvent.on(link, 'focus', this._expand, this);
      }

      this._map.on('click', this._collapse, this);
      // TODO keyboard accessibility
    } else {
      this._expand();
    }

    this._baseLayersList = L.DomUtil.create('div', className + '-base', form);
    this._separator = L.DomUtil.create('div', className + '-separator', form);    
    var deltaLayerList = L.DomUtil.create('div', "delta-list", form);
    // this._deltaLayer = L.DomUtil.create('input', "delta-cenas", form);
    var deltaLabelAll = L.DomUtil.create('label', "delta-All", deltaLayerList);
    var deltaSpanAll = L.DomUtil.create('input', "delta-All", deltaLabelAll);
    deltaSpanAll.setAttribute('type', 'radio');
    deltaSpanAll.setAttribute('className', 'leaflet-control-layers-selector');
    deltaSpanAll.setAttribute('name', 'deltaradio');
    deltaSpanAll.setAttribute('checked', 'checked');
    var deltalayerAll = L.DomUtil.create('span', "delta-All-layer", deltaLabelAll);
    deltalayerAll.innerHTML = ' All';

    var deltaLabelLastMonth = L.DomUtil.create('label', "delta-lastmonth", deltaLayerList);
    var deltaSpanLastMonth = L.DomUtil.create('input', "delta-lastmonth", deltaLabelLastMonth);
    deltaSpanLastMonth.setAttribute('type', 'radio');
    deltaSpanLastMonth.setAttribute('className', 'leaflet-control-layers-selector');
    deltaSpanLastMonth.setAttribute('name', 'deltaradio');
    deltaSpanLastMonth.setAttribute('defaultChecked', 'checked');
    var deltalayerLastMonth = L.DomUtil.create('span', "delta-lastmonth-layer", deltaLabelLastMonth);
    deltalayerLastMonth.innerHTML = ' Last Month';

    L.DomEvent.on(deltaSpanAll, 'click', this._onDeltaInputClick, this);
    L.DomEvent.on(deltaSpanLastMonth, 'click', this._onDeltaInputClick, this);

    this._separator = L.DomUtil.create('div', className + '-separator', form);  
    this._overlaysList = L.DomUtil.create('div', className + '-overlays', form);

    //this._deltaLayerList.appendChild(deltaLayer);
    

    container.appendChild(form);
  },

  _addLayer: function (layer, name, group, overlay, type) {
    var id = L.Util.stamp(layer);
    this._layers[id] = {
      layer: layer,
      name: name,
      overlay: overlay,
      type: type,
    };
    // 

    if (group) {
      var groupId = this._groupList.indexOf(group);

      if (groupId === -1) {
        groupId = this._groupList.push(group) - 1;        
      }
      this._layers[id].group = {
        name: group,
        id: groupId
      };
    }

    if (this.options.autoZIndex && layer.setZIndex) {
      this._lastZIndex++;
      layer.setZIndex(this._lastZIndex);
    }
    
  },

  _update: function () {
    if (!this._container) {
      return;
    }

    this._baseLayersList.innerHTML = '';
    this._domGroups.length = 0;

    var baseLayersPresent = false,
        overlaysPresent = false,
        i, obj;

    for (i in this._layers) {      
      obj = this._layers[i];      
      if (obj.overlay && obj.group.name === "Points of Interest") {
        
      }
      this._addItem(obj);
      overlaysPresent = overlaysPresent || obj.overlay ;
      baseLayersPresent = baseLayersPresent || !obj.overlay;      
    }

    this._separator.style.display = overlaysPresent && baseLayersPresent ? '' : 'none';         

  },

  _onLayerChange: function (e) {
    var obj = this._layers[L.Util.stamp(e.layer)];

    if (!obj) { return; }

    if (!this._handlingClick) {
      this._update();
    }

    var type = obj.overlay ?
      (e.type === 'layeradd' ? 'overlayadd' : 'overlayremove') :
      (e.type === 'layeradd' ? 'baselayerchange' : null);

    if (type) {
      this._map.fire(type, obj);
    }
  },

  // IE7 bugs out if you create a radio dynamically, so you have to do it this hacky way (see http://bit.ly/PqYLBe)
  _createRadioElement: function (name, checked) {

    var radioHtml = '<input type="radio" class="leaflet-control-layers-selector" name="' + name + '"';
    if (checked) {
      radioHtml += ' checked="checked"';
    }
    radioHtml += '/>';

    var radioFragment = document.createElement('div');
    radioFragment.innerHTML = radioHtml;

    return radioFragment.firstChild;
  },

  _addItem: function (obj) {
    var label = document.createElement('label'),
        input,
        checked = this._map.hasLayer(obj.layer),
        container;

    

    if (obj.overlay) {
      // 
      // if (obj.type === "All") 
      input = document.createElement('input');
      input.type = 'checkbox';
      input.className = 'leaflet-control-layers-selector';
      input.defaultChecked = checked;
    } else {
      input = this._createRadioElement('leaflet-base-layers', checked);
    }

    input.layerId = L.Util.stamp(obj.layer);

    L.DomEvent.on(input, 'click', this._onDeltaInputClick, this);

    var name = document.createElement('span');
    name.innerHTML = ' ' + obj.name;

    label.appendChild(input);
    label.appendChild(name);

    if (obj.type === "LastMonth")
      return label;
    // 

    if (obj.overlay) {
      container = this._overlaysList;

      var groupContainer = this._domGroups[obj.group.id];

      // Create the group container if it doesn't exist
      if (!groupContainer) {
        groupContainer = document.createElement('div');
        groupContainer.className = 'leaflet-control-layers-group';
        groupContainer.id = 'leaflet-control-layers-group-' + obj.group.id;

        var groupLabel = document.createElement('span');
        groupLabel.className = 'leaflet-control-layers-group-name';
        groupLabel.innerHTML = obj.group.name;

        groupContainer.appendChild(groupLabel);
        container.appendChild(groupContainer);

        this._domGroups[obj.group.id] = groupContainer;
      }      
      container = groupContainer;
    } else {         
        container = this._baseLayersList;
    }
        
    container.appendChild(label);

    return label;
  },

  _addItems2: function (obj, id) {

    var label = document.createElement('label'),
        input,
        checked = this._map.hasLayer(obj.layer),
        container;

    if (obj.overlay) {
      // 
      // if (obj.type === "All") 
      input = document.createElement('input');
      input.type = 'checkbox';
      input.className = 'leaflet-control-layers-selector';
      input.defaultChecked = checked;
    } else {
      input = this._createRadioElement('leaflet-base-layers', checked);
    }

    input.layerId = L.Util.stamp(obj.layer);

    L.DomEvent.on(input, 'click', this._onDeltaInputClick, this);

    var name = document.createElement('span');
    name.innerHTML = ' ' + obj.name;

    label.appendChild(input);
    label.appendChild(name);

    document.getElementById("leaflet-control-layers-group-" + id).appendChild(label);

  },

  _addGroupItems: function (id) {
    var groupContainer = document.createElement('div');
    groupContainer.className = 'leaflet-control-layers-group';
    groupContainer.id = 'leaflet-control-layers-group-' + id;

    var groupLabel = document.createElement('span');
    groupLabel.className = 'leaflet-control-layers-group-name';
    if (id == 0)
      groupLabel.innerHTML = "Points of Interest";
    else if (id == 1)
      groupLabel.innerHTML = "Points of Interest";

    groupContainer.appendChild(groupLabel);
    
    document.getElementsByClassName("leaflet-control-layers-overlays")[0].appendChild(groupContainer);          
  },

  _onInputClick: function () {
    var i, input, obj,
        inputs = this._form.getElementsByTagName('input'),
        inputsLen = inputs.length;

    this._handlingClick = true;

    for (i = 0; i < inputsLen; i++) {
      if (i != 2 && i != 3) {
        input = inputs[i];
        obj = this._layers[input.layerId];

        
        

        if (input.checked && !this._map.hasLayer(obj.layer)) {
          this._map.addLayer(obj.layer);

        } else if (!input.checked && this._map.hasLayer(obj.layer)) {
          this._map.removeLayer(obj.layer);
        }
      }
      
    }

    this._handlingClick = false;

    
  },

  _onDeltaInputClick: function () {
    var i, j, input, input2, obj,
        inputs = this._form.getElementsByTagName('input');        
        inputsLen = inputs.length;

    this._handlingClick = true;

    for (i = 0; i < 2; i++) {
      obj = this._layers[inputs[i].layerId]; 
      if (inputs[i].checked && !this._map.hasLayer(obj.layer)) {
        this._map.addLayer(obj.layer);

      } else if (!inputs[i].checked && this._map.hasLayer(obj.layer)) {
        this._map.removeLayer(obj.layer);
      }      
    }
     
    if (inputs[3].checked) {

      // if não existe 1 adicionar grupo 1
      if (document.getElementById("leaflet-control-layers-group-1") == null) {
        this._addGroupItems(1);

        // adicionar as labels ao grupo 1
        for(var key in this._layers) {
          var obj = this._layers[key];
          if (obj.overlay && obj.group.id == 1) {
            this._addItems2(obj, 1);
          }
        }
      }
      
      for (j = 4; j < inputsLen; j++) {
        input2 = inputs[j];
        obj = this._layers[input2.layerId]; 
        if (obj.type === "All") {
          if (this._map.hasLayer(obj.layer)) 
            this._map.removeLayer(obj.layer);
        } else if (obj.type === "LastMonth") {
          if (input2.checked && !this._map.hasLayer(obj.layer)) 
            this._map.addLayer(obj.layer);            
            
          if (!input2.checked && this._map.hasLayer(obj.layer))
            this._map.removeLayer(obj.layer);
        } 

      }
      // if exist 0
      if (document.getElementById("leaflet-control-layers-group-0") != null)
        document.getElementById("leaflet-control-layers-group-0").remove();
      
    } else if (inputs[2].checked) {
      // if não existe 0
      if (document.getElementById("leaflet-control-layers-group-0") == null) {
        this._addGroupItems(0);

        for(var key in this._layers) {
          var obj = this._layers[key];
          if (obj.overlay && obj.group.id == 0) {
            this._addItems2(obj, 0);
          }
        }
      }
      // document.getElementById("leaflet-control-layers-group-0").style.visibility = "visible";
      for (j = 4; j < inputsLen; j++) {
        input2 = inputs[j];
        obj = this._layers[input2.layerId];
        
        if (obj.type === "LastMonth") {
          if (this._map.hasLayer(obj.layer)) 
            this._map.removeLayer(obj.layer);
        } else if (obj.type === "All") {
          if (input2.checked && !this._map.hasLayer(obj.layer)) 
            this._map.addLayer(obj.layer);                   
          if (!input2.checked && this._map.hasLayer(obj.layer))
            this._map.removeLayer(obj.layer);
            
        }
      }
      // if exist 1
      if (document.getElementById("leaflet-control-layers-group-1") != null)
        document.getElementById("leaflet-control-layers-group-1").remove();
    } 

    this._handlingClick = false;

    
  },

  _expand: function () {
    L.DomUtil.addClass(this._container, 'leaflet-control-layers-expanded');
  },

  _collapse: function () {
    this._container.className = this._container.className.replace(' leaflet-control-layers-expanded', '');
  }
});

L.control.groupedLayers = function (baseLayers, groupedOverlays, options) {
  return new L.Control.GroupedLayers(baseLayers, groupedOverlays, options);
};
