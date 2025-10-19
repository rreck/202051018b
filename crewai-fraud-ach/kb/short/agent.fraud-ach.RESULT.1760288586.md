```json
{
  "id": "c208e55aeaa1c3a9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288586,
  "host_pid": "9e6742732c60:1",
  "hash": "2b166943aea44b57dcb73f5580cbce093007f452056587e0d86e06f225012ccd",
  "cid": "QmV12b166943aea44b57dcb73f5580cbce093007f452",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288586,
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
      "evaluated_at": 1760288586
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
  "sig": "cabf2273c5cc47e8a6cb3aff2c5d442daed22bf6d6a62b31b1da87b9d11faa33"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465006650
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 98, 'threshold': 50, 'total_amount': 17886862, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 97, 'first_seen': 1760285763, 'matching_hash': 'ac98f3afdd973e27'}}}