```json
{
  "id": "c9c604de3e8a863c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294453,
  "host_pid": "9e6742732c60:1",
  "hash": "f24da31c5f91ce4ae6139cf0b1321a2516ededcca7e5712f75198c784778c081",
  "cid": "QmV1f24da31c5f91ce4ae6139cf0b1321a2516ededcc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294453,
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
      "evaluated_at": 1760294453
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
  "sig": "c755daa0d8a175e109e47c826229e0331906e49266d6ca058b7635803fa368d2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465682795
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 314, 'threshold': 50, 'total_amount': 79101310, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 313, 'first_seen': 1760284979, 'matching_hash': 'c9bd5d9b74477b1c'}}}