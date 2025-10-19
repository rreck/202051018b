```json
{
  "id": "229a6f400154df73",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294641,
  "host_pid": "9e6742732c60:1",
  "hash": "2dd4e54aebe6cc83f731ae0bb55c35a3ca00abf05a4b64deb217e41c1e953c00",
  "cid": "QmV12dd4e54aebe6cc83f731ae0bb55c35a3ca00abf0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294641,
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
      "evaluated_at": 1760294641
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
  "sig": "e98969f22aa3505c47bdb96a63324555c2597c065ab4f0aaf19eeb107334bb95"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105159149641
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 242, 'threshold': 50, 'total_amount': 46864752, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 241, 'first_seen': 1760285763, 'matching_hash': '1bdba49a970d4caa'}}}unt_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}