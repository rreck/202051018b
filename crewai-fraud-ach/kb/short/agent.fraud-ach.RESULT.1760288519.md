```json
{
  "id": "b90611a6a80de3b8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288519,
  "host_pid": "9e6742732c60:1",
  "hash": "2083c912308deabc41728f5f42c27f68b09a229dbffaad884a7b6e6476e40446",
  "cid": "QmV12083c912308deabc41728f5f42c27f68b09a229d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288519,
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
      "evaluated_at": 1760288519
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
  "sig": "11dddeeca40e1f4fbe53b4dcc3d80e2c471e31df3e2cbc314647d4e5d8706b98"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037990803
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 96, 'threshold': 50, 'total_amount': 22344000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 95, 'first_seen': 1760285763, 'matching_hash': 'be616144f18eac0b'}}}