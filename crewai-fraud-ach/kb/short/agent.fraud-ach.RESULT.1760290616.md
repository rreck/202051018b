```json
{
  "id": "2aab00968e211619",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290616,
  "host_pid": "9e6742732c60:1",
  "hash": "afd4b359c44b171d4babb23a92dfdece04d83cb1c46d322178074e4a77b85f82",
  "cid": "QmV1afd4b359c44b171d4babb23a92dfdece04d83cb1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290616,
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
      "evaluated_at": 1760290616
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
  "sig": "4bb5bc3031cbe0129ca2e077a34b537b2bdde273b2b8977d241355c6574b99f4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240863608
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 155, 'threshold': 50, 'total_amount': 28767225, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 154, 'first_seen': 1760285763, 'matching_hash': '74bcaa5b0fcf4d77'}}}