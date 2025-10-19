```json
{
  "id": "e239f5ea4cfc13d7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292183,
  "host_pid": "9e6742732c60:1",
  "hash": "873477cfebca73decc18b90b93e0c9e5d94fe4a0e3b1e28111ad34e364fdb594",
  "cid": "QmV1873477cfebca73decc18b90b93e0c9e5d94fe4a0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292183,
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
      "evaluated_at": 1760292183
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
  "sig": "e03fa5b37616e26366a34f7a1eeddc81105e0b5b1607e7cf794308466a6e9d25"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037758614
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 192, 'threshold': 50, 'total_amount': 15731712, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 191, 'first_seen': 1760285763, 'matching_hash': '8cf13377232eef82'}}}