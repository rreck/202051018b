```json
{
  "id": "1a6de5175ed602d8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289472,
  "host_pid": "9e6742732c60:1",
  "hash": "fcc208f9dedb2fac039e3a98b7da8fd66e933493f4c16f196c5ca11f70035e9e",
  "cid": "QmV1fcc208f9dedb2fac039e3a98b7da8fd66e933493",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289472,
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
      "evaluated_at": 1760289472
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
  "sig": "da34d4b737f0529dd13693dbd57fbae622c18d6157785a014aafb11ccd5427b4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100278613406
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 124, 'threshold': 50, 'total_amount': 51089736, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 123, 'first_seen': 1760285765, 'matching_hash': 'bc206509fe1a9621'}}}