```json
{
  "id": "e22140cdafe10377",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294431,
  "host_pid": "9e6742732c60:1",
  "hash": "79d49099c533575ca0a7e79a1fd14b6d55a5926007e452d811c8db703b38dead",
  "cid": "QmV179d49099c533575ca0a7e79a1fd14b6d55a59260",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294431,
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
      "evaluated_at": 1760294431
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
  "sig": "dcf85a11adf9a1a8aaf251f401cbfc1095df5e8f74e11231622b722d0fefac92"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244516225
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 238, 'threshold': 50, 'total_amount': 34896750, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 237, 'first_seen': 1760285763, 'matching_hash': '305c81c4ba1c9c62'}}}