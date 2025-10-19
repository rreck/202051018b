```json
{
  "id": "29fec064a085916b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290743,
  "host_pid": "9e6742732c60:1",
  "hash": "327c1d4a955fbd72816843f95d5119700cbd4fc0f8d78a54fe2df84e4f152452",
  "cid": "QmV1327c1d4a955fbd72816843f95d5119700cbd4fc0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290743,
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
      "evaluated_at": 1760290743
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
  "sig": "99710716fd18dfff90289c50b0413da5de8b43ee12b2d8947f3f003d04f105f2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105157479316
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 158, 'threshold': 50, 'total_amount': 18500536, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 157, 'first_seen': 1760285764, 'matching_hash': 'd3845a7ded8f78ea'}}}