```json
{
  "id": "61128f0cf8f5a13d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288335,
  "host_pid": "9e6742732c60:1",
  "hash": "5c6097af5dd6a44cc4bf000466b8a88e6bdea2b093ee9ea605c7014a4d5ff35b",
  "cid": "QmV15c6097af5dd6a44cc4bf000466b8a88e6bdea2b0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288335,
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
      "evaluated_at": 1760288335
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
  "sig": "81e8744a43ebc70e6e54aff27fb110e0e358d71969a4780c6ec5a562b59eac52"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242027891
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 90, 'threshold': 50, 'total_amount': 12559950, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 89, 'first_seen': 1760285764, 'matching_hash': '176f574fbb51fea2'}}}