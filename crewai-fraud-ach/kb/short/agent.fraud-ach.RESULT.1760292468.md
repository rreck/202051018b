```json
{
  "id": "f104a1cad8868720",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292468,
  "host_pid": "9e6742732c60:1",
  "hash": "d1397c59388afef3b7fcd0b6decaa57df1e9a287f3755c0efacf63ce2d545c3c",
  "cid": "QmV1d1397c59388afef3b7fcd0b6decaa57df1e9a287",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292468,
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
      "evaluated_at": 1760292468
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
  "sig": "d919a4375c61cf5ba2d4ca63284126fac35a84eaa3bd8498f1fbe73411c38454"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009594873577
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 274, 'threshold': 50, 'total_amount': 110381174, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 273, 'first_seen': 1760284979, 'matching_hash': '5add1f4a09a12b51'}}}