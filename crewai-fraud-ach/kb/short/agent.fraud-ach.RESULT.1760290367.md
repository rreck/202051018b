```json
{
  "id": "4984f080cc1d7546",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290367,
  "host_pid": "9e6742732c60:1",
  "hash": "ec116b46acb33cb27262a6bfb7e82c80f832b7f9346f77047aaa3f06855c3c2a",
  "cid": "QmV1ec116b46acb33cb27262a6bfb7e82c80f832b7f9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290367,
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
      "evaluated_at": 1760290367
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
  "sig": "3fd71187385ec01e38c430d3e86fa6cab71bb44b00dd4a94b9e9f2b9ecd66c0c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021517830
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 148, 'threshold': 50, 'total_amount': 44057084, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 147, 'first_seen': 1760285765, 'matching_hash': '323b6ce2946b0561'}}}