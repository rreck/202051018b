```json
{
  "id": "c41ae3a0414b9b46",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290585,
  "host_pid": "9e6742732c60:1",
  "hash": "dc85c6deedb409c49aeb572b60480c39972d2228d1109070c75fdf79548956ce",
  "cid": "QmV1dc85c6deedb409c49aeb572b60480c39972d2228",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290585,
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
      "evaluated_at": 1760290585
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
  "sig": "9500c6d0f135f5c11cc8afc416bbb27198405a8a794746c03e29b321fb5b6051"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593769639
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 154, 'threshold': 50, 'total_amount': 66104192, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 153, 'first_seen': 1760285763, 'matching_hash': 'cb8c3421a3879068'}}}