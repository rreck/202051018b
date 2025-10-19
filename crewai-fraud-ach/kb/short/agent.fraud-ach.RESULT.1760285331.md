```json
{
  "id": "54623881574e20b4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285331,
  "host_pid": "9e6742732c60:1",
  "hash": "7cbf6d667735becda70728625e753622a19a5a7760212884d161b95f86efd022",
  "cid": "QmV17cbf6d667735becda70728625e753622a19a5a77",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285331,
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
      "evaluated_at": 1760285331
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "1d4f296c93fb6cef43daaa6996f5f7b0e39448ed49bf78ff2f2fc80f97d56215"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 14748790, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 34, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}