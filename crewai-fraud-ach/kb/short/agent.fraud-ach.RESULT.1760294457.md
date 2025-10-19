```json
{
  "id": "f0e6eac87d5224a6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294457,
  "host_pid": "9e6742732c60:1",
  "hash": "d484dfea60a3ee95282769a2e3021fb2b96f676cd8e9ee32f2f93ab0decb8a7a",
  "cid": "QmV1d484dfea60a3ee95282769a2e3021fb2b96f676c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294457,
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
      "evaluated_at": 1760294457
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
  "sig": "9175685b523f1837f4a878aef64cedb66ca2a3d05ef0d3476635fd6f9bd639be"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244797937
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 238, 'threshold': 50, 'total_amount': 94243716, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 237, 'first_seen': 1760285765, 'matching_hash': 'e00995c9aab9b89d'}}}