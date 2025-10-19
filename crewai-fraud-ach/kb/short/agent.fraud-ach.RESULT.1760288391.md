```json
{
  "id": "5d2627e1f2d5bef1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288391,
  "host_pid": "9e6742732c60:1",
  "hash": "afb01c7fceafb19514b55eec614c87f8be0106e28b631624576454795cd4b54a",
  "cid": "QmV1afb01c7fceafb19514b55eec614c87f8be0106e2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288391,
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
      "evaluated_at": 1760288391
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
  "sig": "49dd1b8f49fc52389d37119afa8135176c1a40fba00c2bf7d95355747452fb1d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596329202
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 92, 'threshold': 50, 'total_amount': 16006160, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 91, 'first_seen': 1760285763, 'matching_hash': 'fa5bd443d3b1bd8d'}}}