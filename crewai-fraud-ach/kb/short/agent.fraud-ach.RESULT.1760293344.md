```json
{
  "id": "73b1ab1ab18b1096",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293344,
  "host_pid": "9e6742732c60:1",
  "hash": "1f4b5a7ac79d8cbfd4fcb3ebf9caeb69c63dc5c8ab62e00399b9e92d9a176ce4",
  "cid": "QmV11f4b5a7ac79d8cbfd4fcb3ebf9caeb69c63dc5c8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293344,
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
      "evaluated_at": 1760293344
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
  "sig": "13f6787bfc1e5ded8af757acec95f93104afeb4c03ee140cfcbdf66e172608d5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 216, 'threshold': 50, 'total_amount': 68741568, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 215, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}