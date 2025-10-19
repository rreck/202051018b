```json
{
  "id": "be1c0312e12b6388",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287560,
  "host_pid": "9e6742732c60:1",
  "hash": "ffa4b99b1f8df696e3c9d45aaacc34b00f3b569dbdd07f47dfc068e2aca594ab",
  "cid": "QmV1ffa4b99b1f8df696e3c9d45aaacc34b00f3b569d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287560,
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
      "evaluated_at": 1760287560
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
  "sig": "4f2c55e58d8dadfc9023845e0ecac948039e45cce185e70463d2dcf204a0cd89"
}
```

Fraud detected: duplicate_transaction (score: 81)
Transaction: 122105158656793
Details: {'velocity': {'fraud_detected': True, 'risk_score': 78, 'details': {'transaction_count': 64, 'threshold': 50, 'total_amount': 19398016, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 63, 'first_seen': 1760285765, 'matching_hash': 'b1ac6f9d66d66d2b'}}}