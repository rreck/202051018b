```json
{
  "id": "98a9e07cd5812e2d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292922,
  "host_pid": "9e6742732c60:1",
  "hash": "a533e29d0a99d27741ff07e72fb5806261c1ac14f0148c4fac3daa5427f5e96e",
  "cid": "QmV1a533e29d0a99d27741ff07e72fb5806261c1ac14",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292922,
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
      "evaluated_at": 1760292922
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
  "sig": "f544026820a1b5ae51b7d84e9f3edc11db8ac226136b44c62e35754ae9b368d0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271295485
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 208, 'threshold': 50, 'total_amount': 79332448, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 207, 'first_seen': 1760285763, 'matching_hash': '1c5bb12c0a4cbea7'}}}