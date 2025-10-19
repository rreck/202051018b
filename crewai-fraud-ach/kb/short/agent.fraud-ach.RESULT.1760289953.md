```json
{
  "id": "daae225929d44ca6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289953,
  "host_pid": "9e6742732c60:1",
  "hash": "e1cc6eec9d4ff24ad2afa4f98d2d522371118471f171c03f7aa2f4b21742547b",
  "cid": "QmV1e1cc6eec9d4ff24ad2afa4f98d2d522371118471",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289953,
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
      "evaluated_at": 1760289953
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
  "sig": "3c3e4e5e23320b6cf620f4b3861b3beeb4543d734910f8c68f80f2022e9107a9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 137, 'threshold': 50, 'total_amount': 43599976, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 136, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}