```json
{
  "id": "4d0424f5fb186bb6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293890,
  "host_pid": "9e6742732c60:1",
  "hash": "9339f211759514cfd4dedc4175deb3865aa11ce7edfe1e5647d08ec843bdb4cc",
  "cid": "QmV19339f211759514cfd4dedc4175deb3865aa11ce7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293890,
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
      "evaluated_at": 1760293890
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
  "sig": "536fd463355536ccd30acfb3ace0abf4b1f936eff5a25d035d90c88598b92db9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241265060
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 227, 'threshold': 50, 'total_amount': 103591677, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 226, 'first_seen': 1760285765, 'matching_hash': '7bee400a4c5e15b1'}}}