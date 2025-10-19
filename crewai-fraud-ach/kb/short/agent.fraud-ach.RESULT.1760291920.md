```json
{
  "id": "77d424af1ad2efd0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291920,
  "host_pid": "9e6742732c60:1",
  "hash": "a15a1c9e8a5c92acfe4ed8604dfb6a150657c3fdf1ee530d942961b126d56995",
  "cid": "QmV1a15a1c9e8a5c92acfe4ed8604dfb6a150657c3fd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291920,
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
      "evaluated_at": 1760291921
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
  "sig": "c0f5f54f13eda310d5f548260bfa6368d9f33d916d9a17700ffec367e90ff311"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241124617
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 186, 'threshold': 50, 'total_amount': 51410772, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 185, 'first_seen': 1760285763, 'matching_hash': 'fcf7fec38d983fba'}}}