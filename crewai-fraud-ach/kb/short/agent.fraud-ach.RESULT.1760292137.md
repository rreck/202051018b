```json
{
  "id": "4ec3ee267fc0cd74",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292137,
  "host_pid": "9e6742732c60:1",
  "hash": "3247a889632a44cca02d6f110efe4f9c2916cd12e9364321e2ea78be0b481f90",
  "cid": "QmV13247a889632a44cca02d6f110efe4f9c2916cd12",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292137,
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
      "evaluated_at": 1760292137
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
  "sig": "3d9c74c6cdc9df3a6f2abeec81e75b320f9370789c91df9ef58a4ed9f7efa047"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462755939
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 191, 'threshold': 50, 'total_amount': 16727207, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 190, 'first_seen': 1760285764, 'matching_hash': '0ef039381f9434ef'}}}