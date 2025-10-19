```json
{
  "id": "3acd3698dd899165",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293857,
  "host_pid": "9e6742732c60:1",
  "hash": "fc1ed9210dd5e1dd1054b02b9061c7a5202ea071b822aa4ef7716276c3f10801",
  "cid": "QmV1fc1ed9210dd5e1dd1054b02b9061c7a5202ea071",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293857,
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
      "evaluated_at": 1760293857
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
  "sig": "275d82c66c2f19d74f38364cda45ce2a331aecb140dde10436a20dd56e511280"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029536226
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 227, 'threshold': 50, 'total_amount': 16529232, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 226, 'first_seen': 1760285763, 'matching_hash': 'ee8686fc8d545b2d'}}}