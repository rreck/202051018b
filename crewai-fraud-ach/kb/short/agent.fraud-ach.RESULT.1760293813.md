```json
{
  "id": "5b74d4ede04345c8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293813,
  "host_pid": "9e6742732c60:1",
  "hash": "c2e211d1e96035eecca8553599da51a714478f5282e2707bd163a641fb7b5adb",
  "cid": "QmV1c2e211d1e96035eecca8553599da51a714478f52",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293813,
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
      "evaluated_at": 1760293814
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
  "sig": "8713943826fe9ad954e7ac84b5d4d0bf792677987ab79b7ca6f6e70a08166202"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246406835
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 226, 'threshold': 50, 'total_amount': 52744106, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 225, 'first_seen': 1760285764, 'matching_hash': '1c7c2a17ea2f241c'}}}