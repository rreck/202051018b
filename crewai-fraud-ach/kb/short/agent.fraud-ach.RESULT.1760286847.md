```json
{
  "id": "6dc7e2b0d827ed30",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286847,
  "host_pid": "9e6742732c60:1",
  "hash": "8f5925c1a12694fde865ed406f232cb900750b36edc8738969a592b9bc818db7",
  "cid": "QmV18f5925c1a12694fde865ed406f232cb900750b36",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286847,
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
      "evaluated_at": 1760286847
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
  "sig": "005f16e12c916e3434b59f214c8b532f84c8dccd7432fdfc900336e070229173"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000029964192
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 11832795, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 38, 'first_seen': 1760285764, 'matching_hash': '3fa9c762fe00e5a2'}}}