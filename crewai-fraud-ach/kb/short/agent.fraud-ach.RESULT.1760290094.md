```json
{
  "id": "f30895d07346f652",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290094,
  "host_pid": "9e6742732c60:1",
  "hash": "c417776b38c75154dcd1a9b109e571be9053cd5fa884159d1929f9e617408599",
  "cid": "QmV1c417776b38c75154dcd1a9b109e571be9053cd5f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290094,
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
      "evaluated_at": 1760290094
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
  "sig": "b94d91eeff373fc74fdf02e147674f6a50765e318a4699a03dcbf8a3409be3ca"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023546405
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 141, 'threshold': 50, 'total_amount': 60760707, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 140, 'first_seen': 1760285763, 'matching_hash': '22f38bfa79b47563'}}}