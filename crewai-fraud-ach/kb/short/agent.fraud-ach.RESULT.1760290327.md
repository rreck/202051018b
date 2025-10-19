```json
{
  "id": "d07c6228659bc2f1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290327,
  "host_pid": "9e6742732c60:1",
  "hash": "2f55154068dedcd136dbf16d0c8a93140175ccc8e6714db87b73034ecbe8e510",
  "cid": "QmV12f55154068dedcd136dbf16d0c8a93140175ccc8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290327,
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
      "evaluated_at": 1760290327
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
  "sig": "f318d844966350de2f48267d0d32c6b50058da159c4326d4cac843c20cb83f5e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274979410
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 147, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 146, 'first_seen': 1760285765, 'matching_hash': '00a04409f00be8e6'}}}