```json
{
  "id": "14d0febf42939ddf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286458,
  "host_pid": "9e6742732c60:1",
  "hash": "b51c1f447414ddd9ca444a9f04a216bbbd57d1d4c51f3dd160fc0ffee8526f63",
  "cid": "QmV1b51c1f447414ddd9ca444a9f04a216bbbd57d1d4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286458,
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
      "evaluated_at": 1760286458
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
  "sig": "e666c7df0961c1069002b9a819c5b3197fc4f9634ba87856ebf8382fcf9543d0"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000032712325
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 25, 'first_seen': 1760285763, 'matching_hash': '06a9425dc3ac5c5b'}}}