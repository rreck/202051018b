```json
{
  "id": "8f5ac77d8c3eaada",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290668,
  "host_pid": "9e6742732c60:1",
  "hash": "0e52d42c657d05a1cbcb3fc357edc94a1cf1fb70b52bc9a7f0276e02563e3333",
  "cid": "QmV10e52d42c657d05a1cbcb3fc357edc94a1cf1fb70",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290668,
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
      "evaluated_at": 1760290668
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
  "sig": "87be4f169682d7f09a9a7d41068f20fdc518487ae420b3822566f9c75f8b12a9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031291734
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 156, 'threshold': 50, 'total_amount': 53129544, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 155, 'first_seen': 1760285763, 'matching_hash': 'b88361d419e7152d'}}}