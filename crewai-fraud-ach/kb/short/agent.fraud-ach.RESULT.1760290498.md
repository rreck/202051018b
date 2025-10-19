```json
{
  "id": "108244164f859e0b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290498,
  "host_pid": "9e6742732c60:1",
  "hash": "419e227b9c9f35baea0023f8d1c6be5b5b341c64bcbf72b3949e3c35f18dc0e4",
  "cid": "QmV1419e227b9c9f35baea0023f8d1c6be5b5b341c64",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290498,
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
      "evaluated_at": 1760290498
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
  "sig": "22b7479fba7e4334f522c13932ca46e098433cb8a65d16ec746e915ae3011893"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031502254
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 152, 'threshold': 50, 'total_amount': 35783232, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 151, 'first_seen': 1760285763, 'matching_hash': 'cc2974580ec11a3c'}}}