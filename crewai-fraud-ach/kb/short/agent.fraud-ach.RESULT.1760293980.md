```json
{
  "id": "b0a72edbb9cda350",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293980,
  "host_pid": "9e6742732c60:1",
  "hash": "1fd6aa5d3b1d3462388d70dca5affb8d68af4c7b05651b21e4a57a1a9e887416",
  "cid": "QmV11fd6aa5d3b1d3462388d70dca5affb8d68af4c7b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293980,
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
      "evaluated_at": 1760293980
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
  "sig": "bfd9030504ec030a040dfef04cb0f5aa98cfa5c3bdec80b0db861c0123b51751"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000021533630
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 229, 'threshold': 50, 'total_amount': 33757806, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 228, 'first_seen': 1760285765, 'matching_hash': 'e04be99e47eedc93'}}}