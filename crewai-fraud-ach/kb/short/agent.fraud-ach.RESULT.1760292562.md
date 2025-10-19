```json
{
  "id": "abb19fff20503340",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292562,
  "host_pid": "9e6742732c60:1",
  "hash": "a930aa4697e9790c80a4790f1599da29713dbd42222143adb0b4cacaa6629aeb",
  "cid": "QmV1a930aa4697e9790c80a4790f1599da29713dbd42",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292562,
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
      "evaluated_at": 1760292562
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
  "sig": "f7750f8e1a41d66b95b6015f794ae02286af7f6977205d85aafc38e30a607ab0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154102308
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 276, 'threshold': 50, 'total_amount': 101685852, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 275, 'first_seen': 1760284979, 'matching_hash': '687d8a253912c530'}}}