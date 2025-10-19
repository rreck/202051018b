```json
{
  "id": "ceabfdc7ee6d5b30",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288835,
  "host_pid": "9e6742732c60:1",
  "hash": "c96611a2ef2e95c93dcaa68216e28886cb2ba19a4f03ab530b48c040bd23961f",
  "cid": "QmV1c96611a2ef2e95c93dcaa68216e28886cb2ba19a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288835,
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
      "evaluated_at": 1760288835
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
  "sig": "4a72f77860a1a94fb0028d4c0d55fd8da2d4d8ed7742fc50a3b70814cc91257f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469832017
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 105, 'threshold': 50, 'total_amount': 32817855, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 104, 'first_seen': 1760285765, 'matching_hash': '99e095073411ccc4'}}}