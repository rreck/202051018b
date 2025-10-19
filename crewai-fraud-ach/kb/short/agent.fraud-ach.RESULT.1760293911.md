```json
{
  "id": "05e28c73bc566966",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293911,
  "host_pid": "9e6742732c60:1",
  "hash": "4526c3d476c3a28fdbf922bf1a4545d83444698224de535738b9e5f86c723ff1",
  "cid": "QmV14526c3d476c3a28fdbf922bf1a4545d834446982",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293911,
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
      "evaluated_at": 1760293911
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
  "sig": "a0ac67a6729498bdfdec4612f81f72d4c1f18c86fda41eb1d44a99c79ac1e77c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029122182
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 228, 'threshold': 50, 'total_amount': 22800000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 227, 'first_seen': 1760285763, 'matching_hash': '6eeeaf20a2fbd10d'}}}}