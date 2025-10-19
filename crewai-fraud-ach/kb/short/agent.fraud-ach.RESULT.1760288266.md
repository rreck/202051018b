```json
{
  "id": "e0117b2c3f796b29",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288266,
  "host_pid": "9e6742732c60:1",
  "hash": "1d6b0076893894c801b99aa416c58dae768184afa4c54117504b5630604dcb06",
  "cid": "QmV11d6b0076893894c801b99aa416c58dae768184af",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288266,
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
      "evaluated_at": 1760288266
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "47467b599d57dec8326f3bfc944e045e49d40c0fc2350a967d21f49bfe8ed6e8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000021252160
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 88, 'threshold': 50, 'total_amount': 41887824, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 87, 'first_seen': 1760285763, 'matching_hash': '942f41a705b17558'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '036223730', 'validation_error': 'Invalid routing number checksum'}}}