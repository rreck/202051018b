```json
{
  "id": "8c30dd47bcd5cdb5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287364,
  "host_pid": "9e6742732c60:1",
  "hash": "f74bec84ed09c40f7dc0a4eb3c06f6be4479e39f31fbff211600872ee8e76e53",
  "cid": "QmV1f74bec84ed09c40f7dc0a4eb3c06f6be4479e39f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287364,
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
      "evaluated_at": 1760287364
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "9653b3f9d7b1a02481844515f8a37c281bf3c5ccd28b35be8d2edf2bd925e09a"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 021000026265735
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 57, 'threshold': 50, 'total_amount': 20069016, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 56, 'first_seen': 1760285765, 'matching_hash': 'e94388ee515b2db1'}}}