```json
{
  "id": "e3ffecbf02e784e2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287325,
  "host_pid": "9e6742732c60:1",
  "hash": "5980aea343886e930f3e461cb000a920b197b5a29be819ff35b450028dfa1e7c",
  "cid": "QmV15980aea343886e930f3e461cb000a920b197b5a2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287325,
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
      "evaluated_at": 1760287325
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
  "sig": "9b01f1d6755c0feba8ebdc6a49a6d306df5cf68bee2ffb3375b1a8c3ca08b908"
}
```

Fraud detected: duplicate_transaction (score: 73)
Transaction: 122105157447901
Details: {'velocity': {'fraud_detected': True, 'risk_score': 62, 'details': {'transaction_count': 56, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 55, 'first_seen': 1760285765, 'matching_hash': '08b33f5611b85fcf'}}}