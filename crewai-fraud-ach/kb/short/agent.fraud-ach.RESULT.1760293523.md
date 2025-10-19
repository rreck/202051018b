```json
{
  "id": "da617105767f5b70",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293523,
  "host_pid": "9e6742732c60:1",
  "hash": "4221054add24baefda7cf01872fc3bc80ac2e6887378bb35cd59822d65ef39f5",
  "cid": "QmV14221054add24baefda7cf01872fc3bc80ac2e688",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293523,
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
      "evaluated_at": 1760293523
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
  "sig": "63225739a6e160c43bb098c9da6668933c162eee1268ac4b98a5e79baaa702c2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100275777124
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 220, 'threshold': 50, 'total_amount': 60677320, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 219, 'first_seen': 1760285763, 'matching_hash': 'd1e6afcf07f21c4a'}}}