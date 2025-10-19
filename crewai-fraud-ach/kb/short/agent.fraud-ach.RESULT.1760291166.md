```json
{
  "id": "935f86ed3adec848",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291166,
  "host_pid": "9e6742732c60:1",
  "hash": "dfa8fa1c0a60e5c2690d54a4fa7ed44faeaeb9401f14d6b81205b6b311deca66",
  "cid": "QmV1dfa8fa1c0a60e5c2690d54a4fa7ed44faeaeb940",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291166,
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
      "evaluated_at": 1760291166
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
  "sig": "9129fecad889f1f364e351e1352e380ac887fe7d4727ddeed60618f439926ee9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 168, 'threshold': 50, 'total_amount': 53465664, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 167, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}