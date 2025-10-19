```json
{
  "id": "ab64528973d4cec0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290229,
  "host_pid": "9e6742732c60:1",
  "hash": "853ffd7eef7795c065b25cec7d40081c7ea7434304c95965df873dfbef8230e4",
  "cid": "QmV1853ffd7eef7795c065b25cec7d40081c7ea74343",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290229,
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
      "evaluated_at": 1760290229
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
  "sig": "9801b1e1b49b667db5641a5bd10b7f91c5b3c781ce36a76bd51d09fce8ec312b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271177223
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 145, 'threshold': 50, 'total_amount': 70130410, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 144, 'first_seen': 1760285763, 'matching_hash': 'bfc9cdfd9eceb164'}}}