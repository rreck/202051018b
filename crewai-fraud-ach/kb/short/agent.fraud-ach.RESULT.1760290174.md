```json
{
  "id": "9ead1a27842f523d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290174,
  "host_pid": "9e6742732c60:1",
  "hash": "6ae5ed27e7f97c3f4040f4aaa10d0ec1d8ef60c5654e9fcc8d631e3a8dc1a111",
  "cid": "QmV16ae5ed27e7f97c3f4040f4aaa10d0ec1d8ef60c5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290174,
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
      "evaluated_at": 1760290174
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
  "sig": "618e898512a4edd10b277f1f0c4bb819d1c0a2e84ba43416eb3487353333d550"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029236644
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 143, 'threshold': 50, 'total_amount': 32574685, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 142, 'first_seen': 1760285765, 'matching_hash': 'c69cf0de1758a1d7'}}}