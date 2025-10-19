```json
{
  "id": "53d141891b7bc5c2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290456,
  "host_pid": "9e6742732c60:1",
  "hash": "f48be89fd48c1eec151002d063bf78bd14051b97c51d76e43fa32a69ddc421ce",
  "cid": "QmV1f48be89fd48c1eec151002d063bf78bd14051b97",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290456,
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
      "evaluated_at": 1760290456
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
  "sig": "cb149443f4a00705ac72206cb5f0e495e83c46d318118ec1f4cf7ddf1cbee4d7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271052795
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 151, 'threshold': 50, 'total_amount': 33311808, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 150, 'first_seen': 1760285763, 'matching_hash': '457d955844db0007'}}}