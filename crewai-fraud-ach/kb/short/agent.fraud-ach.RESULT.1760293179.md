```json
{
  "id": "484c2a6f467f27a7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293179,
  "host_pid": "9e6742732c60:1",
  "hash": "f7d37b74b8980b0258b27e92f154b38322b5666c9fc6c35bba37d6aa41fa8be1",
  "cid": "QmV1f7d37b74b8980b0258b27e92f154b38322b5666c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293179,
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
      "evaluated_at": 1760293179
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
  "sig": "6bdbbe15c598d96bb0a0aef07370787422cd0638e6ea02524fb38432237d8164"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032958974
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 213, 'threshold': 50, 'total_amount': 89662350, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 212, 'first_seen': 1760285763, 'matching_hash': '718043100f50114f'}}}