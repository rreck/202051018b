```json
{
  "id": "328f6082cc9acd0d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287632,
  "host_pid": "9e6742732c60:1",
  "hash": "26bc68eb3c9ad3554101b5f8501c0066a86ae0ce828258c99fbcf949c433c007",
  "cid": "QmV126bc68eb3c9ad3554101b5f8501c0066a86ae0ce",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287632,
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
      "evaluated_at": 1760287632
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
  "sig": "f0a6d68d90b71e875661c6616fec91b501ecfe7f1b012aed61856747c09a19e3"
}
```

Fraud detected: duplicate_transaction (score: 84)
Transaction: 021000027669266
Details: {'velocity': {'fraud_detected': True, 'risk_score': 84, 'details': {'transaction_count': 67, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 66, 'first_seen': 1760285764, 'matching_hash': 'fbd07eed8562f9d2'}}}een': 1760285764, 'matching_hash': '57e27cf175445fc0'}}}