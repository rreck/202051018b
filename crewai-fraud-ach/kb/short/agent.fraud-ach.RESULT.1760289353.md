```json
{
  "id": "1a9c1e9a0a7e8ef2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289353,
  "host_pid": "9e6742732c60:1",
  "hash": "de7ba815d2e2169b6be07c0f551201a02b42a6de20cde62a8c4f8a6f785cf898",
  "cid": "QmV1de7ba815d2e2169b6be07c0f551201a02b42a6de",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289353,
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
      "evaluated_at": 1760289353
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
  "sig": "fb67517b0335574923913a9f81437a1402f4a2facc1efc90223b28db237a8b52"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599280040
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 121, 'threshold': 50, 'total_amount': 58901106, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 120, 'first_seen': 1760285763, 'matching_hash': '3242f38050bfb93d'}}}