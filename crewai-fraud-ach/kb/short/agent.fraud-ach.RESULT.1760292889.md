```json
{
  "id": "9cbc84d43a2bb525",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292889,
  "host_pid": "9e6742732c60:1",
  "hash": "ac23d54e5b54d4b9a74db381dc99e86850911425957e2f6273ba1ae2a7bc94f9",
  "cid": "QmV1ac23d54e5b54d4b9a74db381dc99e86850911425",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292889,
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
      "evaluated_at": 1760292890
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
  "sig": "04e9b476da57e62d482d5da99f664504bfc7f435045ce90890a06f9fb1baa3c7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460804941
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 207, 'threshold': 50, 'total_amount': 15256728, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 206, 'first_seen': 1760285763, 'matching_hash': 'e3b2eb0d41697d4a'}}}