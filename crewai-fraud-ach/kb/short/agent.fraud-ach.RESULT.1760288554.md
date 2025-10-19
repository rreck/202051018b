```json
{
  "id": "1640feca437fdee5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288554,
  "host_pid": "9e6742732c60:1",
  "hash": "086b6e6b194062e4b29f83dad88bccf9083943203756ca7daa0001a370c559ab",
  "cid": "QmV1086b6e6b194062e4b29f83dad88bccf908394320",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288554,
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
      "evaluated_at": 1760288554
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
  "sig": "ef2c0600a3cf5778d121e541ed434843c652c9383fceb2e33e26e3bcd466d15d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022866819
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 97, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 96, 'first_seen': 1760285763, 'matching_hash': '7f3c5046f4bcc1d0'}}}