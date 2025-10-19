```json
{
  "id": "c5aa4f7b17337634",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289296,
  "host_pid": "9e6742732c60:1",
  "hash": "f2d54f75425daa3ed754b2fe54a2d050d4edf2833383d0aefaab6ab882dc22a0",
  "cid": "QmV1f2d54f75425daa3ed754b2fe54a2d050d4edf283",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289296,
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
      "evaluated_at": 1760289296
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
  "sig": "8d4a3256f886bb5ee899371c4bf0fee96d871050eebd059a7f98c4ce4fbfadaa"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599876575
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 119, 'threshold': 50, 'total_amount': 37152752, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 118, 'first_seen': 1760285764, 'matching_hash': '0131e24faef32fc6'}}}