```json
{
  "id": "efeedae79ecfb8e2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293403,
  "host_pid": "9e6742732c60:1",
  "hash": "bc914713735ecdf47db9aa0d62408772be6b008a9cbcb9e3c57b9efef2a18efd",
  "cid": "QmV1bc914713735ecdf47db9aa0d62408772be6b008a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293403,
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
      "evaluated_at": 1760293403
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
  "sig": "50540201cb8b8630c9bcb5775a4dd1dec2dd4454f5c57dc5bc3338c5480a5fab"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000030232602
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 218, 'threshold': 50, 'total_amount': 13151940, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 217, 'first_seen': 1760285763, 'matching_hash': '54bba9b5de699774'}}}