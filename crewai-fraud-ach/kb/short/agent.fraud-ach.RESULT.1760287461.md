```json
{
  "id": "8844e8ef8019b03b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287461,
  "host_pid": "9e6742732c60:1",
  "hash": "3d91e520eea294c35a27ee7acde32aaa955924342528534acc6a3212fab19964",
  "cid": "QmV13d91e520eea294c35a27ee7acde32aaa95592434",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287461,
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
      "evaluated_at": 1760287461
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
  "sig": "d0019bed5f89a4c6e31b67adf53e1ac37ca8670b300125d0db6c2f96853eb105"
}
```

Fraud detected: duplicate_transaction (score: 78)
Transaction: 121000245652457
Details: {'velocity': {'fraud_detected': True, 'risk_score': 72, 'details': {'transaction_count': 61, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 60, 'first_seen': 1760285763, 'matching_hash': '6ac12dd8f1799493'}}}een': 1760285763, 'matching_hash': 'bfc334a18daf8fbf'}}}g': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '646437635', 'validation_error': 'Invalid routing number checksum'}}}