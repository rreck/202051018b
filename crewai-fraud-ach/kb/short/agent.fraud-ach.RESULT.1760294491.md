```json
{
  "id": "ca1be8bec7a876a7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294491,
  "host_pid": "9e6742732c60:1",
  "hash": "b9000d281934e2c2d785be552c2b5529aff91d277654509a4744f99b82a4e818",
  "cid": "QmV1b9000d281934e2c2d785be552c2b5529aff91d27",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294491,
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
      "evaluated_at": 1760294491
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
  "sig": "689a0fe2df3cf10362aaa0b4689cc0dc820b153fff8fd2dfb839b55f66e73c18"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243661505
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 239, 'threshold': 50, 'total_amount': 99893874, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 238, 'first_seen': 1760285764, 'matching_hash': '37851bbce8ea73db'}}}