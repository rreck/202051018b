```json
{
  "id": "65e0583b649b5924",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287267,
  "host_pid": "9e6742732c60:1",
  "hash": "f01e8c215c19f44c3035fa18582ebf21d65e8a72b062912e81aeacbccf21bfd6",
  "cid": "QmV1f01e8c215c19f44c3035fa18582ebf21d65e8a72",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287267,
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
      "evaluated_at": 1760287267
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
  "sig": "5ee23657753207e008df4b236a0971027c3035f95015eae4a19283d523c03f68"
}
```

Fraud detected: duplicate_transaction (score: 71)
Transaction: 044000039536800
Details: {'velocity': {'fraud_detected': True, 'risk_score': 58, 'details': {'transaction_count': 54, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 53, 'first_seen': 1760285763, 'matching_hash': '37ca22243c3304cf'}}}een': 1760285763, 'matching_hash': '526960b6a0cd6e16'}}}routing_number': '650095545', 'validation_error': 'Invalid routing number checksum'}}}