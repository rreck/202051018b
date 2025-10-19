```json
{
  "id": "2b6f550270a8d9fb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294070,
  "host_pid": "9e6742732c60:1",
  "hash": "3b803e0841ff0728d72ad6159c0e9872ec6d730faa588a8fe538784a1c85350b",
  "cid": "QmV13b803e0841ff0728d72ad6159c0e9872ec6d730f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294070,
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
      "evaluated_at": 1760294070
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
  "sig": "b63ebd686d5e5b91d5bc135f1ea931fd8a6aacddd9fe510885d99b8af51a2e10"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201461534453
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 231, 'threshold': 50, 'total_amount': 81315003, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 230, 'first_seen': 1760285763, 'matching_hash': '17211f2899ea38ec'}}}