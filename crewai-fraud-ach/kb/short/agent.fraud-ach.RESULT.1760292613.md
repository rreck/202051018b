```json
{
  "id": "e6b2843c6803ffd1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292613,
  "host_pid": "9e6742732c60:1",
  "hash": "70cc5c68bbe85b9d802d34d53f26b2ee8c296b7d4f602c9a386f6737f0912fb7",
  "cid": "QmV170cc5c68bbe85b9d802d34d53f26b2ee8c296b7d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292613,
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
      "evaluated_at": 1760292613
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
  "sig": "b202a7b264c4c6db1ab2c8375ffff9d90bdcf96bf6f7a5712a9e79488a270ccd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026081546
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 201, 'threshold': 50, 'total_amount': 31383939, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 200, 'first_seen': 1760285763, 'matching_hash': 'ce75c9757255dcb1'}}}