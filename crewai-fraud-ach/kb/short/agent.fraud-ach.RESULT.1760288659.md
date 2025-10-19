```json
{
  "id": "000180240e2d8f30",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288659,
  "host_pid": "9e6742732c60:1",
  "hash": "ee1f017d343f5743445ac874f0efdb2669d022804dd07efed494b9f671607def",
  "cid": "QmV1ee1f017d343f5743445ac874f0efdb2669d02280",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288659,
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
      "evaluated_at": 1760288659
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
  "sig": "674536d1cab1c872f39ed418e906468c83edfd76833919750dc38ec1365a239a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154971432
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 100, 'threshold': 50, 'total_amount': 33833100, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 99, 'first_seen': 1760285764, 'matching_hash': 'db584ac34c85fc07'}}}