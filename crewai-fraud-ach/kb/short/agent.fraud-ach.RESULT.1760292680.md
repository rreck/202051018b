```json
{
  "id": "54aaceb0de08eb66",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292680,
  "host_pid": "9e6742732c60:1",
  "hash": "17d673684199e8d41c6f9b64107377ff72d39979acab73455df9ea26632f6072",
  "cid": "QmV117d673684199e8d41c6f9b64107377ff72d39979",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292680,
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
      "evaluated_at": 1760292680
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
  "sig": "efc52885a7302a84c911222b314bbad93c08532bb761ac3f315f1223d9459a4c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593711895
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 203, 'threshold': 50, 'total_amount': 79226028, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 202, 'first_seen': 1760285763, 'matching_hash': '1e7ea83d54912238'}}}