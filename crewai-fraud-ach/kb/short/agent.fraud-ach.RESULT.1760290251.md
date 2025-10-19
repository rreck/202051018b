```json
{
  "id": "10c7d23876c696e7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290251,
  "host_pid": "9e6742732c60:1",
  "hash": "caf9bf0346efa11af22a1e212fe767d3315758545b7a794c0d4b3ad714744011",
  "cid": "QmV1caf9bf0346efa11af22a1e212fe767d331575854",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290251,
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
      "evaluated_at": 1760290251
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
  "sig": "46bd96c43f08663759abf4d4172e3abbbe09165dfc9fd027e90d3b85924a16a4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201461662832
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 145, 'threshold': 50, 'total_amount': 60600140, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 144, 'first_seen': 1760285765, 'matching_hash': 'adb809538e6eb6af'}}}