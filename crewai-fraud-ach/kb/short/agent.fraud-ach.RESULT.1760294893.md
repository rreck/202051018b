```json
{
  "id": "af78f56dd07a10f3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294893,
  "host_pid": "9e6742732c60:1",
  "hash": "e372ba55286bf2d1a109227ab9f6fd07aa8f870eef3a0d791e4faac21bafce0e",
  "cid": "QmV1e372ba55286bf2d1a109227ab9f6fd07aa8f870e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294893,
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
      "evaluated_at": 1760294893
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
  "sig": "4ecaa0d97e07931e320e5705e14d57b75abb6194a4bd9c06142266a84d5d7c22"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274472610
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 246, 'threshold': 50, 'total_amount': 80914812, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 245, 'first_seen': 1760285764, 'matching_hash': '7db40904e20d1f88'}}}