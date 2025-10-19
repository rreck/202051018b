```json
{
  "id": "5a0a2557831454ff",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288566,
  "host_pid": "9e6742732c60:1",
  "hash": "c17b8be0d2913384724fbbc2979e1f2f78a5f6023fd7de554578213a957aab14",
  "cid": "QmV1c17b8be0d2913384724fbbc2979e1f2f78a5f602",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288566,
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
      "evaluated_at": 1760288566
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
  "sig": "b5a61ad9c0b852c14d07fc97be9c5897d6051e9306684782c660fadadb45415d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034778259
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 97, 'threshold': 50, 'total_amount': 17648568, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 96, 'first_seen': 1760285763, 'matching_hash': 'b6b775805828fc60'}}}