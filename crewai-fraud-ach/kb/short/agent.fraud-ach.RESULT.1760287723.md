```json
{
  "id": "bcae6014b0d74f21",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287723,
  "host_pid": "9e6742732c60:1",
  "hash": "c33c4e1da5c9cfda684c921bb6df882f1f8c922e2c4b92f64a16a7cd7acd32b6",
  "cid": "QmV1c33c4e1da5c9cfda684c921bb6df882f1f8c922e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287723,
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
      "evaluated_at": 1760287723
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
  "sig": "8d0e4abad9c63b7163c0948dd601b2aa5213f8aa5a2f2315856b6b274a64ce60"
}
```

Fraud detected: duplicate_transaction (score: 87)
Transaction: 031201468454923
Details: {'velocity': {'fraud_detected': True, 'risk_score': 90, 'details': {'transaction_count': 70, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 69, 'first_seen': 1760285765, 'matching_hash': '07b42bdcb312ebee'}}}