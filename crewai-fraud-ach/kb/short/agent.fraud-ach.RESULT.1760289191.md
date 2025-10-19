```json
{
  "id": "bdfcea6c3b48801a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289191,
  "host_pid": "9e6742732c60:1",
  "hash": "ab7a1add99d228475f42db9fa7677e6524e812fbbdb770c4fef0ed5f97a93157",
  "cid": "QmV1ab7a1add99d228475f42db9fa7677e6524e812fb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289191,
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
      "evaluated_at": 1760289191
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
  "sig": "9414a733582ef94616e27e5e673a1f677516364ea4ea5e72934f298cf31958ca"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154730054
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 116, 'threshold': 50, 'total_amount': 31234160, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 115, 'first_seen': 1760285763, 'matching_hash': '3072a79f51416ab8'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '208726934', 'validation_error': 'Invalid routing number checksum'}}}