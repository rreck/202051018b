```json
{
  "id": "d8b41b6b09902817",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292342,
  "host_pid": "9e6742732c60:1",
  "hash": "d667025a1ef446f4e97708d12c3eef5ddaafcf56d07ab73c7c27ad21f31c9b4c",
  "cid": "QmV1d667025a1ef446f4e97708d12c3eef5ddaafcf56",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292342,
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
      "evaluated_at": 1760292342
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
  "sig": "c55b6ded62f5cf13f0ea044beb106d40c0295c8a52eae79946c6e3a5c06b8969"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009590866940
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 195, 'threshold': 50, 'total_amount': 82874220, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 194, 'first_seen': 1760285765, 'matching_hash': '66ff896a34603a53'}}}