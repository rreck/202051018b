```json
{
  "id": "e0cb8ad0569640ff",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291648,
  "host_pid": "9e6742732c60:1",
  "hash": "47dd622e2d5779c9afc404da2384abb7170ca6e4eadadaafa8b0348208d23cfe",
  "cid": "QmV147dd622e2d5779c9afc404da2384abb7170ca6e4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291648,
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
      "evaluated_at": 1760291648
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
  "sig": "2cfa660dea427ae0c158366c8d4bb8980867f4ab011cce7bf8b950cbbb1508d6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465206903
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 180, 'threshold': 50, 'total_amount': 83466000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 179, 'first_seen': 1760285763, 'matching_hash': 'cc8a6efa32cdbdd1'}}}