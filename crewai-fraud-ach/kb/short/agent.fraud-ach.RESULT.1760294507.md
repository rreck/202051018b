```json
{
  "id": "5f2ec054b23cfb01",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294507,
  "host_pid": "9e6742732c60:1",
  "hash": "097ebe50993820d7fa73810cd6478599de4fc7d2a5ac7c6cb7a143b7c6ee8524",
  "cid": "QmV1097ebe50993820d7fa73810cd6478599de4fc7d2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294507,
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
      "evaluated_at": 1760294507
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
  "sig": "ad74e08ae6ab29fb61511d666ad97fd57fa70277f432ce1feaa266b3fc0c93be"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591273341
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 239, 'threshold': 50, 'total_amount': 13059916, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 238, 'first_seen': 1760285765, 'matching_hash': '7aa2b4ab7394d79b'}}}