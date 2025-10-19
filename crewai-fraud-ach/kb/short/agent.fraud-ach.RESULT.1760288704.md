```json
{
  "id": "f0929387363d16ab",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288704,
  "host_pid": "9e6742732c60:1",
  "hash": "a1ada5ecbad650b8550b7e1f7e10be1f982153248ac6eb4233cf8dcd68b525be",
  "cid": "QmV1a1ada5ecbad650b8550b7e1f7e10be1f98215324",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288704,
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
      "evaluated_at": 1760288704
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
  "sig": "0be292f89511d1b13d690d4adc9441dda85cf8dd0d09cba9b4a09a16d7d09706"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021517830
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 101, 'threshold': 50, 'total_amount': 30065983, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 100, 'first_seen': 1760285765, 'matching_hash': '323b6ce2946b0561'}}}