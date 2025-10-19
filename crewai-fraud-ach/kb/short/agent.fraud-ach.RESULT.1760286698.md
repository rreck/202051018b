```json
{
  "id": "1bb5d45cf2e8e7ed",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286698,
  "host_pid": "9e6742732c60:1",
  "hash": "dbfa224ab6d60d8a0d109d923f1430b577c848d7cca7c62e016db9fcd4080f66",
  "cid": "QmV1dbfa224ab6d60d8a0d109d923f1430b577c848d7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286698,
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
      "evaluated_at": 1760286698
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
  "sig": "422706f83a931258583b970a006e207afd47bd2eee1cc30842ed7e841aff9629"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000023924602
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 13683402, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 33, 'first_seen': 1760285764, 'matching_hash': '8a38ff5636f784bb'}}}760284979, 'matching_hash': '54d3add09935598e'}}}