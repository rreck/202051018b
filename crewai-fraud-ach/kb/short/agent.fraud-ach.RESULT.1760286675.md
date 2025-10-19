```json
{
  "id": "2eb86800aa567f69",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286675,
  "host_pid": "9e6742732c60:1",
  "hash": "61e7922ea0730f05a2ba8b59833e63d47b266482cc8676481cd303c142362c5a",
  "cid": "QmV161e7922ea0730f05a2ba8b59833e63d47b266482",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286675,
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
      "evaluated_at": 1760286675
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
  "sig": "a0c26b2a483b3d39782e4a77d579e2e4b0dadb87319a1ecf6f027334fc0da00b"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 026009597956116
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 12119910, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 32, 'first_seen': 1760285764, 'matching_hash': '37dac3adff3764b9'}}}