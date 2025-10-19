```json
{
  "id": "3d00dd1d7886a128",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291375,
  "host_pid": "9e6742732c60:1",
  "hash": "917b15c8dcc0cc91628c372bd6ea32e19ef10ed707dd9fe4fcf6da4291e8fe59",
  "cid": "QmV1917b15c8dcc0cc91628c372bd6ea32e19ef10ed7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291375,
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
      "evaluated_at": 1760291375
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "7d458eb7e433959d50e74479b6fd5b27e910eff6dabe68d34085dd2c6e5a2a54"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 635242948975660
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 173, 'threshold': 50, 'total_amount': 74340176, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 172, 'first_seen': 1760285765, 'matching_hash': '596a6d950333709b'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '635242942', 'validation_error': 'Invalid routing number checksum'}}}