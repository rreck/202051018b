```json
{
  "id": "bbc8751c0006f4e8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293968,
  "host_pid": "9e6742732c60:1",
  "hash": "fccb47d91d7e5cf7217276313d98e8c672f917b010eef2875a5e504b0e5b016a",
  "cid": "QmV1fccb47d91d7e5cf7217276313d98e8c672f917b0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293968,
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
      "evaluated_at": 1760293968
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
  "sig": "f6d91e63a897b6493b5741a25f3bf5536ab51fcada209d09180dcc413484d764"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000021906357
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 229, 'threshold': 50, 'total_amount': 100253223, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 228, 'first_seen': 1760285764, 'matching_hash': '507361b82f38c481'}}}