```json
{
  "id": "991f0499c2c8f04d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286762,
  "host_pid": "9e6742732c60:1",
  "hash": "2a03fc29aecc6e1691805afa01fc76fcaeca109927167f35742a2ca0adb655fc",
  "cid": "QmV12a03fc29aecc6e1691805afa01fc76fcaeca1099",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286762,
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
      "evaluated_at": 1760286762
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
  "sig": "52afbb6be55a98ecdb83afb2b61e4f5b881becb905f10a7afd84c6f44f662900"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 031201463787734
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 11566980, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 35, 'first_seen': 1760285764, 'matching_hash': 'c4d507dbbdae18b2'}}}