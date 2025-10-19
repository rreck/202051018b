```json
{
  "id": "f9efe87e0d700d65",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287693,
  "host_pid": "9e6742732c60:1",
  "hash": "c72fdaeadd1e22dd9488f00b160501bbfc1f36059f6049c0d4abd1b7c353ea09",
  "cid": "QmV1c72fdaeadd1e22dd9488f00b160501bbfc1f3605",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287693,
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
      "evaluated_at": 1760287693
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
  "sig": "3b3f833b8ecd4dcaa34b5aa965e54d12ab9870d51731f55d33a9393a1afaae74"
}
```

Fraud detected: duplicate_transaction (score: 86)
Transaction: 122105152187504
Details: {'velocity': {'fraud_detected': True, 'risk_score': 88, 'details': {'transaction_count': 69, 'threshold': 50, 'total_amount': 32598636, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 68, 'first_seen': 1760285764, 'matching_hash': '4c6bc703d31ba532'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}