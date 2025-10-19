```json
{
  "id": "439458c75ebfcccb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291325,
  "host_pid": "9e6742732c60:1",
  "hash": "b2eeb6c321da1bf854e7d5504b9f82fcbfc15ea2e14cfafdd5af69a0109d56fa",
  "cid": "QmV1b2eeb6c321da1bf854e7d5504b9f82fcbfc15ea2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291325,
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
      "evaluated_at": 1760291325
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
  "sig": "9de679c6e1319a1bd675279cee445bfdf5978e2b254f491a70317bfb1c578969"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244797937
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 172, 'threshold': 50, 'total_amount': 68108904, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 171, 'first_seen': 1760285765, 'matching_hash': 'e00995c9aab9b89d'}}}