```json
{
  "id": "0b65076d33eef1a8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287380,
  "host_pid": "9e6742732c60:1",
  "hash": "022fac34fef360e69db7b8308c2028a0a2b320d4b1c7b2c83a6fedd9bbff32dd",
  "cid": "QmV1022fac34fef360e69db7b8308c2028a0a2b320d4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287380,
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
      "evaluated_at": 1760287380
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
  "sig": "775a4be0f7c841992e98cdffe93d6f1705e3cf816d2fe71ebf870c6cdf6e867d"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 063100270359022
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 58, 'threshold': 50, 'total_amount': 12960274, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 57, 'first_seen': 1760285763, 'matching_hash': 'b3fe4d9c14539f22'}}}g': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '053611749', 'validation_error': 'Invalid routing number checksum'}}}