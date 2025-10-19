```json
{
  "id": "42a5faddba9b4c07",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289658,
  "host_pid": "9e6742732c60:1",
  "hash": "57c150bcdb876dc3905597fc916c23ccfe46317390a8a38fdc371a95a6dd9c1f",
  "cid": "QmV157c150bcdb876dc3905597fc916c23ccfe463173",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289658,
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
      "evaluated_at": 1760289658
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
  "sig": "e1a135012a2bef1362b8f5e1f4a9e6f5594576dfc0b6f737e905565729aa8bb0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000020716291
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 129, 'threshold': 50, 'total_amount': 24391578, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 128, 'first_seen': 1760285765, 'matching_hash': 'a2f2d41c7f22f612'}}}