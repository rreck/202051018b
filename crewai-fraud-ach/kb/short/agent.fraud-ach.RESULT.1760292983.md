```json
{
  "id": "851d702b726d3019",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292983,
  "host_pid": "9e6742732c60:1",
  "hash": "fe989b34b54ee6364f3fffc8fbe3de198342e55a990290226cc39e73f09b4307",
  "cid": "QmV1fe989b34b54ee6364f3fffc8fbe3de198342e55a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292983,
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
      "evaluated_at": 1760292983
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
  "sig": "c0693806fb26c1eea81e9c6d14161c8b07a09292aef0d11ddaba5c68ddf60a4b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105158715464
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 209, 'threshold': 50, 'total_amount': 30969829, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 208, 'first_seen': 1760285763, 'matching_hash': '08e14bce24e2b1ea'}}}}