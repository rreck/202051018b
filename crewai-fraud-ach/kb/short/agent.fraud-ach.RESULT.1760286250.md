```json
{
  "id": "8691247a17936b20",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286250,
  "host_pid": "9e6742732c60:1",
  "hash": "ef947f0d56bca1cf94ee64fbb785eee76c340b015a822abd6bf8475bbbb8146a",
  "cid": "QmV1ef947f0d56bca1cf94ee64fbb785eee76c340b01",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286250,
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
      "evaluated_at": 1760286250
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
  "sig": "d81956689f855b5700f33ce10da2b7d89a55a0008f04c206f9b620344dfc1960"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000029964192
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 18, 'first_seen': 1760285764, 'matching_hash': '3fa9c762fe00e5a2'}}}