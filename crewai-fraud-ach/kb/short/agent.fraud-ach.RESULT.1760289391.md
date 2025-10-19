```json
{
  "id": "b9ab218d5faac1d5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289391,
  "host_pid": "9e6742732c60:1",
  "hash": "9aecd258b94420470106e98efb5bdff25c2d127d1d29b6ae5ffdcf3271f9ed68",
  "cid": "QmV19aecd258b94420470106e98efb5bdff25c2d127d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289391,
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
      "evaluated_at": 1760289391
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
  "sig": "6360242cda3f7608c5fe2b236608032c4600af0be257982cd6367bca81c6d27f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243028505
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 122, 'threshold': 50, 'total_amount': 12579908, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 121, 'first_seen': 1760285763, 'matching_hash': '47e30fe250bb416c'}}}