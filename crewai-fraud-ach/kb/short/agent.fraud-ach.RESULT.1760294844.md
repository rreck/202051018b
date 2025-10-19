```json
{
  "id": "4a5262ab2f8e3de8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294844,
  "host_pid": "9e6742732c60:1",
  "hash": "d1e9b86ec7e06ab14052c61a5741532d97a9a6a326bea5f9f808f568dd11977f",
  "cid": "QmV1d1e9b86ec7e06ab14052c61a5741532d97a9a6a3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294844,
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
      "evaluated_at": 1760294844
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
  "sig": "75144513a28360fdf5f0308239930ec52e1f64033c38b67be2e36a8074866c72"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009590866940
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 245, 'threshold': 50, 'total_amount': 104124020, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 244, 'first_seen': 1760285765, 'matching_hash': '66ff896a34603a53'}}}