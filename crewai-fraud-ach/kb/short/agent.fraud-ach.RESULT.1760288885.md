```json
{
  "id": "cd6c91860e4d7d13",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288885,
  "host_pid": "9e6742732c60:1",
  "hash": "9f7a7f6dc0a28c152f08106fb6b515b02c69daf8d13d2a45452b05a328f1dcca",
  "cid": "QmV19f7a7f6dc0a28c152f08106fb6b515b02c69daf8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288885,
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
      "evaluated_at": 1760288885
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
  "sig": "d92c05573238d5bd71a7f85a082cce8bacdc92c2390cc342a24a160a39d7f3cf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000023498410
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 107, 'threshold': 50, 'total_amount': 14154923, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 106, 'first_seen': 1760285763, 'matching_hash': 'a97f330737c5e5f9'}}}