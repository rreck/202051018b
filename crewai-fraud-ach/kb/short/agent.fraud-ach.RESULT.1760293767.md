```json
{
  "id": "91fa15ce2ce27c02",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293767,
  "host_pid": "9e6742732c60:1",
  "hash": "36c27eb9a41f8d439687117be12711c3eb58b124bd9ebb97640ebbd03db0016b",
  "cid": "QmV136c27eb9a41f8d439687117be12711c3eb58b124",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293767,
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
      "evaluated_at": 1760293767
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
  "sig": "b377b10ffa5e70339fd3aeff99617869d7225570acff394876c25f74c925a662"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591886558
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 225, 'threshold': 50, 'total_amount': 70705575, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 224, 'first_seen': 1760285763, 'matching_hash': '37bcf4c9c4817870'}}}