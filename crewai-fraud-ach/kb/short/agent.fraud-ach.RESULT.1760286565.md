```json
{
  "id": "858f0c5f360e98df",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286565,
  "host_pid": "9e6742732c60:1",
  "hash": "3b1db739ef58cb226591e7a6389ee904c996f24ea1515d546e60c0141f23b1d8",
  "cid": "QmV13b1db739ef58cb226591e7a6389ee904c996f24e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286565,
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
      "evaluated_at": 1760286565
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
  "sig": "58d3d26fe5e37771eb2f2a9e501333794ab3218af2ccdde49d9f7a97a732f6d4"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000021480535
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 14304163, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 28, 'first_seen': 1760285765, 'matching_hash': '9682be52dcbb3d1d'}}}