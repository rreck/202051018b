```json
{
  "id": "4aa734886fc0e449",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289757,
  "host_pid": "9e6742732c60:1",
  "hash": "eeb5b0dadcc6a4e135500aae92f6914060b0ef5e4bf385b24d0737021ac37244",
  "cid": "QmV1eeb5b0dadcc6a4e135500aae92f6914060b0ef5e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289757,
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
      "evaluated_at": 1760289757
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
  "sig": "d5d21e64e179958c6fd6c13b0143c359ca476d3cb85e779f4e758145359d1fcb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246878582
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 208, 'threshold': 50, 'total_amount': 56734080, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 207, 'first_seen': 1760284979, 'matching_hash': '3e968f91ba41b0b5'}}}