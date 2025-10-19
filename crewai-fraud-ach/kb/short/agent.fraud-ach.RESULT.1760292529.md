```json
{
  "id": "4140858a897dc399",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292529,
  "host_pid": "9e6742732c60:1",
  "hash": "7212618044f04aa9920169a43befd17ae04b0425c7d4b1063df258399e261b83",
  "cid": "QmV17212618044f04aa9920169a43befd17ae04b0425",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292529,
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
      "evaluated_at": 1760292529
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
  "sig": "29c99fa205e9e75411b882d63b61ba9c35121811f6de16418c8911379ece3328"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 199, 'threshold': 50, 'total_amount': 63331352, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 198, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}