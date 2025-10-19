```json
{
  "id": "d9fd1c6e94ef81ae",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293930,
  "host_pid": "9e6742732c60:1",
  "hash": "3b3e3e654c678d345a89e1c6302c03e75c205ba10acfffbcf4ca24566de58006",
  "cid": "QmV13b3e3e654c678d345a89e1c6302c03e75c205ba1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293930,
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
      "evaluated_at": 1760293930
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
  "sig": "f5dd2d19ff7041c94627de81d9c9967387c2945b525cf4437dc4228a8be7d232"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100276148173
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 228, 'threshold': 50, 'total_amount': 64454460, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 227, 'first_seen': 1760285765, 'matching_hash': 'f15677eba424e05f'}}}}