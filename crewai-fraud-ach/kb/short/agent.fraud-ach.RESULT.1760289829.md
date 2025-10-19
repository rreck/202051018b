```json
{
  "id": "52f3bcdb3271eecc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289829,
  "host_pid": "9e6742732c60:1",
  "hash": "0b528c4439fb4f0d63c1e2eb8e38a42196cf2b5c34dd340f77a5c014c2ea5805",
  "cid": "QmV10b528c4439fb4f0d63c1e2eb8e38a42196cf2b5c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289829,
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
      "evaluated_at": 1760289829
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
  "sig": "db93c464ccffa7cd58a65664cfbc5d6ee0228b11c3e9ada6994329116c0b47f2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026494478
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 134, 'threshold': 50, 'total_amount': 25395278, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 133, 'first_seen': 1760285763, 'matching_hash': 'bca1271a1f86b87c'}}}}