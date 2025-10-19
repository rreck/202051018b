```json
{
  "id": "36c9f48e1a0ab077",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292980,
  "host_pid": "9e6742732c60:1",
  "hash": "0fad64cbc76cbda12f2b0558611afa2d52c8d86274b62b8efeb3e746d898196d",
  "cid": "QmV10fad64cbc76cbda12f2b0558611afa2d52c8d862",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292980,
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
      "evaluated_at": 1760292980
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
  "sig": "c6081a35c781622601a928e1be03c6baa6c61e3f2ef6531095f6d1e9030e6ef0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000028559782
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 209, 'threshold': 50, 'total_amount': 46690182, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 208, 'first_seen': 1760285763, 'matching_hash': '551fe21bbee5d648'}}}