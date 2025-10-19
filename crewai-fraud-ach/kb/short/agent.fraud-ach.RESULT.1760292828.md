```json
{
  "id": "736fbc2297d4854a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292828,
  "host_pid": "9e6742732c60:1",
  "hash": "44fe5c26c66ab1bbb7ae89bf0c0643217d8bf973cda7ff3d896d58e661840903",
  "cid": "QmV144fe5c26c66ab1bbb7ae89bf0c0643217d8bf973",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292828,
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
      "evaluated_at": 1760292828
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
  "sig": "043910cea61190c85833f2a3414d7f4bd1e1b2389807a0d797d73b8d20e2649a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038495907
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 206, 'threshold': 50, 'total_amount': 56032412, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 205, 'first_seen': 1760285763, 'matching_hash': '3a0df0e30691ba23'}}}