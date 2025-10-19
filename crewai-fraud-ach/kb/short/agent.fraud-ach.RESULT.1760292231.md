```json
{
  "id": "75668c31183bd8a3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292231,
  "host_pid": "9e6742732c60:1",
  "hash": "38812661ba77184b668b915dff2473464e189c56245ed3d809d8360d6ed8592b",
  "cid": "QmV138812661ba77184b668b915dff2473464e189c56",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292231,
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
      "evaluated_at": 1760292231
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
  "sig": "3e57d1aeea1b80bdb4b1f5c4ee49ab87c54e216257be45eb79077f56142ca230"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246406835
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 193, 'threshold': 50, 'total_amount': 45042533, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 192, 'first_seen': 1760285764, 'matching_hash': '1c7c2a17ea2f241c'}}}