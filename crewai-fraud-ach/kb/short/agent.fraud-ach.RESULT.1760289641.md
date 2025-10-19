```json
{
  "id": "74eab35f3ac25f3e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289641,
  "host_pid": "9e6742732c60:1",
  "hash": "512eb7366a6cbcde671a3ecaac14adf682928f18a7aeeaac397dec70ac2989ee",
  "cid": "QmV1512eb7366a6cbcde671a3ecaac14adf682928f18",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289641,
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
      "evaluated_at": 1760289641
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
  "sig": "2ca2371b6f854e9de0d50f05cfe44058ed7a71752b1e8afd0a3f407e54d7f5c1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241330040
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 129, 'threshold': 50, 'total_amount': 34387530, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 128, 'first_seen': 1760285763, 'matching_hash': '556aef048193b362'}}}