```json
{
  "id": "20a369f35f5cac1e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289151,
  "host_pid": "9e6742732c60:1",
  "hash": "ab1d4d9bd6ff61dcfd895ae80d94d6eb954791da7107528cda1e57f17d1f7814",
  "cid": "QmV1ab1d4d9bd6ff61dcfd895ae80d94d6eb954791da",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289151,
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
      "evaluated_at": 1760289151
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
  "sig": "bcb699a677bc0acf843ce755269a5511fcde3652056da634245edd28105bdfcc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460204606
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 115, 'threshold': 50, 'total_amount': 15355605, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 114, 'first_seen': 1760285763, 'matching_hash': 'ff63dbf095b2d177'}}}