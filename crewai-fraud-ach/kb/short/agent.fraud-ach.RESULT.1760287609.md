```json
{
  "id": "4e4f9565f114fe31",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287609,
  "host_pid": "9e6742732c60:1",
  "hash": "ad7d5d2eafc3784ffc8cb22887f3cd5f5aa30b5261edc36ba24ea9edc0bfdcc3",
  "cid": "QmV1ad7d5d2eafc3784ffc8cb22887f3cd5f5aa30b52",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287609,
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
      "evaluated_at": 1760287609
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
  "sig": "d9f863dc43e1ed5ca24bebc13ac422c33e2b997454c2ddb293ac2aade5353d55"
}
```

Fraud detected: duplicate_transaction (score: 83)
Transaction: 031201468256911
Details: {'velocity': {'fraud_detected': True, 'risk_score': 82, 'details': {'transaction_count': 66, 'threshold': 50, 'total_amount': 11980452, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 65, 'first_seen': 1760285765, 'matching_hash': 'b0ec3a54cf0504a9'}}}