```json
{
  "id": "85dd17df4cdb0521",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294520,
  "host_pid": "9e6742732c60:1",
  "hash": "d63cc802803b991add53e19c0c178b544f20898fbea7a4f549d3347feddcbe00",
  "cid": "QmV1d63cc802803b991add53e19c0c178b544f20898f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294520,
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
      "evaluated_at": 1760294520
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
  "sig": "927d680d26a782a8713d7045aa656ccedcaf5e9590f0fe6cec315e5a04b5a16b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100276932154
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 239, 'threshold': 50, 'total_amount': 87978290, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 238, 'first_seen': 1760285765, 'matching_hash': '117d4b1b88487dad'}}}