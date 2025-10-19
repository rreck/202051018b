```json
{
  "id": "1447d25d680f4ece",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290102,
  "host_pid": "9e6742732c60:1",
  "hash": "97936db286d99c4526dc4c6f56907d21895b2520bf8c3c24c6dd12074f05ab43",
  "cid": "QmV197936db286d99c4526dc4c6f56907d21895b2520",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290102,
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
      "evaluated_at": 1760290102
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
  "sig": "40f4eee291e38aac5eb85596b2f6ce4b21fa79aa899bd3f53fecd2601f3d7196"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 141, 'threshold': 50, 'total_amount': 44872968, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 140, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}