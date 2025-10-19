```json
{
  "id": "72a9248185127369",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287726,
  "host_pid": "9e6742732c60:1",
  "hash": "359f42a24eaefe2b421a4309a3c9e78573abe3851afe09b55a58d470673d64ca",
  "cid": "QmV1359f42a24eaefe2b421a4309a3c9e78573abe385",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287726,
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
      "evaluated_at": 1760287726
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
  "sig": "607f69c0cb3f9351eea8a8579a2ebc9f19199e410fe143f6334e095fea27a50a"
}
```

Fraud detected: duplicate_transaction (score: 87)
Transaction: 122105153385568
Details: {'velocity': {'fraud_detected': True, 'risk_score': 90, 'details': {'transaction_count': 70, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 69, 'first_seen': 1760285763, 'matching_hash': '556aff2bced704f0'}}}