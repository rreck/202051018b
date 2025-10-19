```json
{
  "id": "b744aef6fb06e963",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292499,
  "host_pid": "9e6742732c60:1",
  "hash": "789e5fedfa68b788722d999da9f478c4e6e4f9228a9c7518f13d81343f5b3cb9",
  "cid": "QmV1789e5fedfa68b788722d999da9f478c4e6e4f922",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292499,
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
      "evaluated_at": 1760292499
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
  "sig": "09dd57ab8331cc37b6bfe22ae0ae8315f85148b0e917012cdcfaf1d0584e1dda"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241647784
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 199, 'threshold': 50, 'total_amount': 21876866, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 198, 'first_seen': 1760285763, 'matching_hash': '5747783cddc76b25'}}}