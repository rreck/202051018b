```json
{
  "id": "e2f4758dcce7e216",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288926,
  "host_pid": "9e6742732c60:1",
  "hash": "24da22357c46fd292c7c39e9ef664e71bba8e71093a671764b2bc5b4450918e4",
  "cid": "QmV124da22357c46fd292c7c39e9ef664e71bba8e710",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288926,
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
      "evaluated_at": 1760288926
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
  "sig": "aeaf4734fb9543fc8f0ae751e1f75b6712ca050f1d21d5df4f0fed984eda3a21"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105158912506
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 108, 'threshold': 50, 'total_amount': 16616988, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 107, 'first_seen': 1760285765, 'matching_hash': 'bcd6f6796bd6b696'}}}