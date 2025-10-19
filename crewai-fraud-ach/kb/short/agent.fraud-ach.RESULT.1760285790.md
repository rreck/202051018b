```json
{
  "id": "38dac576f2dce96f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285790,
  "host_pid": "9e6742732c60:488",
  "hash": "9479856604638798607d40d83ba4746d456b3995abedccc4e39939c4f44efc65",
  "cid": "QmV19479856604638798607d40d83ba4746d456b3995",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:488",
      "created_at": 1760285790,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760285790
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "8ddd733a638359b3404d6756bf388e93cfe09c8d795db5ee762b3e78045d2325"
}
```

Fraud detected: invalid_routing (score: 95)
Transaction: 649338001689495
Details: {'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '649338005', 'validation_error': 'Invalid routing number checksum'}}}