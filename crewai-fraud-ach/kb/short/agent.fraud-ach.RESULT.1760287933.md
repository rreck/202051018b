```json
{
  "id": "42723c8e2cdf2a46",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287933,
  "host_pid": "9e6742732c60:1",
  "hash": "50252afa6f2b7d00343af8536f407aadd240b0c961ab83d199a1571d4e5a8855",
  "cid": "QmV150252afa6f2b7d00343af8536f407aadd240b0c9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287933,
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
      "evaluated_at": 1760287933
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
  "sig": "d1726368de703837bded3dcbc3403c851adf1896b50feb97cf7a5fff4bf55668"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000035025346
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 77, 'threshold': 50, 'total_amount': 12383833, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 76, 'first_seen': 1760285763, 'matching_hash': 'a8a877b5861d69af'}}}}}