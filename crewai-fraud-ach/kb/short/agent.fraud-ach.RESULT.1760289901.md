```json
{
  "id": "ecbbdd27327f0393",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289901,
  "host_pid": "9e6742732c60:1",
  "hash": "8833eed2c17ce650218bb3c09b50ee2e85bbc2da18534f5d75f2d1772f4fc2b7",
  "cid": "QmV18833eed2c17ce650218bb3c09b50ee2e85bbc2da",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289901,
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
      "evaluated_at": 1760289901
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
  "sig": "76f721003f0b0f19047e88e371f6172bf9e0be8c044647062e157343f4815317"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009597863146
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 136, 'threshold': 50, 'total_amount': 12217288, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 135, 'first_seen': 1760285763, 'matching_hash': '4ed1fbb19cfa36d6'}}}