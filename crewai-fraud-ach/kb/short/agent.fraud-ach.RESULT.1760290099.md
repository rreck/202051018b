```json
{
  "id": "5fca8d27e24bfa78",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290099,
  "host_pid": "9e6742732c60:1",
  "hash": "3ab7e704079272ae9e6f7e430ac6aebae6e12f5a90132d892e0bbe94b12d80a4",
  "cid": "QmV13ab7e704079272ae9e6f7e430ac6aebae6e12f5a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290099,
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
      "evaluated_at": 1760290099
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
  "sig": "498c6ce5d6ac286a5effb420177ba413458351534e5232729fdb847904d2e97c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155194168
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 141, 'threshold': 50, 'total_amount': 51555945, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 140, 'first_seen': 1760285765, 'matching_hash': '7ab74b64ae25594e'}}}