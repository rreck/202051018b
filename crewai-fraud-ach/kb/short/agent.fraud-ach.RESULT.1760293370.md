```json
{
  "id": "81c6b330e15945af",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293370,
  "host_pid": "9e6742732c60:1",
  "hash": "dad51815bdd70397f918ec4776a12656efb3a5a22d1fb71ee9f6aab402861143",
  "cid": "QmV1dad51815bdd70397f918ec4776a12656efb3a5a2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293370,
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
      "evaluated_at": 1760293370
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
  "sig": "b736d2de289cb373557057b05ac213a09192109bcaf705718008e8a0a9554a7e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009590136300
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 217, 'threshold': 50, 'total_amount': 107507659, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 216, 'first_seen': 1760285764, 'matching_hash': '2d6fc2065b3c1287'}}}