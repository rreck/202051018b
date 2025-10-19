```json
{
  "id": "031ea82e21232d63",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289908,
  "host_pid": "9e6742732c60:1",
  "hash": "6510f97155efc0bbddd728819ec72160ee118a6fcb7e7dfe8ae95c6020c27e41",
  "cid": "QmV16510f97155efc0bbddd728819ec72160ee118a6f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289908,
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
      "evaluated_at": 1760289908
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
  "sig": "dcaf5214ac41ed8928fa8e589cf8e43bb1b72a21961ba04720b95a8d2f087250"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000028366239
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 136, 'threshold': 50, 'total_amount': 18512592, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 135, 'first_seen': 1760285763, 'matching_hash': 'fc3cc28fddce4cc6'}}}