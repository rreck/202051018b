```json
{
  "id": "ac574d9943304ce4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289942,
  "host_pid": "9e6742732c60:1",
  "hash": "547c9ac5d495d10b47a3d2717c5a5b90ec9c0c6861861e24568298b2ee53b9fb",
  "cid": "QmV1547c9ac5d495d10b47a3d2717c5a5b90ec9c0c68",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289942,
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
      "evaluated_at": 1760289942
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
  "sig": "9e82693a827d4c6bd441b008a472c710e1b686983bffbdf1dfa816ae7c6640fa"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034624068
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 137, 'threshold': 50, 'total_amount': 19626072, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 136, 'first_seen': 1760285763, 'matching_hash': 'e9c21d379839efb6'}}}