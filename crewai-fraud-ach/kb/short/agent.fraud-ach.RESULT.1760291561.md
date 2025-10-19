```json
{
  "id": "7d5cc57767b6e24f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291561,
  "host_pid": "9e6742732c60:1",
  "hash": "b063d1bed27a4089db7952055d0edd9b7f6fc78f7f114bf78527d69ff28a7c56",
  "cid": "QmV1b063d1bed27a4089db7952055d0edd9b7f6fc78f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291561,
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
      "evaluated_at": 1760291561
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
  "sig": "e2faca63591f92d50b1cedc9e9e324447d543bd0ad8c67ffe108a5c122bd35d3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029877647
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 178, 'threshold': 50, 'total_amount': 60726658, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 177, 'first_seen': 1760285763, 'matching_hash': 'f76c4daf1b61ee5a'}}}