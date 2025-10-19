```json
{
  "id": "6b41fa70c2db4315",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288053,
  "host_pid": "9e6742732c60:1",
  "hash": "aefaa0e7c0552cc53c4fc4fc11a5ee1b989383ba82f3d3d127a6024adf56c1c3",
  "cid": "QmV1aefaa0e7c0552cc53c4fc4fc11a5ee1b989383ba",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288053,
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
      "evaluated_at": 1760288053
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
  "sig": "9eb1abca446c44f77223efcd8fc93eb34ae428c6c69351a31d8bc7f1c51ca479"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022625380
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 81, 'threshold': 50, 'total_amount': 29296971, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 80, 'first_seen': 1760285763, 'matching_hash': 'f6638b44b9180b42'}}}