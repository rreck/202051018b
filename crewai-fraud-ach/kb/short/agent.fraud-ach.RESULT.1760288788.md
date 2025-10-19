```json
{
  "id": "3faf591c3f6a821f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288788,
  "host_pid": "9e6742732c60:1",
  "hash": "01f94984e829c2bca1b05450b11eb0c5aed0ca7e56a8093a19c773ba051f41e2",
  "cid": "QmV101f94984e829c2bca1b05450b11eb0c5aed0ca7e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288788,
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
      "evaluated_at": 1760288788
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
  "sig": "65c76adc20b6e6657fb8135242e689de7313ecf4523ec80ceba52a6dd1bdc8a4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022233458
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 104, 'threshold': 50, 'total_amount': 29411616, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 103, 'first_seen': 1760285763, 'matching_hash': '02c54d650b9e4b50'}}}