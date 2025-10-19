```json
{
  "id": "64bd859a9f644260",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292287,
  "host_pid": "9e6742732c60:1",
  "hash": "a0f060235640f108170dac78125fee06108d1b6e7a9d2296072a653380bf9ed0",
  "cid": "QmV1a0f060235640f108170dac78125fee06108d1b6e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292287,
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
      "evaluated_at": 1760292287
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
  "sig": "05421f6edee6a9b4bebe03eaf8c64865453f5ef658322369262a65d1bd7823fa"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000020012424
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 194, 'threshold': 50, 'total_amount': 44628342, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 193, 'first_seen': 1760285763, 'matching_hash': '53913ea58eda97e4'}}}