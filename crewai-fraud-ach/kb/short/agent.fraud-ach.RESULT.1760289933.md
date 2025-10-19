```json
{
  "id": "0c9fec98f3d45e7d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289933,
  "host_pid": "9e6742732c60:1",
  "hash": "9ef16d646f239ad3b405b454de0cb1e8a63a8dbdc3c7198f0768de8dc021f893",
  "cid": "QmV19ef16d646f239ad3b405b454de0cb1e8a63a8dbd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289933,
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
      "evaluated_at": 1760289933
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
  "sig": "964ff10e93065bed321030f8c609dc162bf523004ebe6b604175cfce7928b00e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000020947870
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 137, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 136, 'first_seen': 1760285763, 'matching_hash': '1f43c37f0aae1875'}}}een': 1760285764, 'matching_hash': '97f823784b1b19f6'}}}