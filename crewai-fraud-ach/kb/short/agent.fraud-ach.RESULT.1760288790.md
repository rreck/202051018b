```json
{
  "id": "733d2880e5f50035",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288790,
  "host_pid": "9e6742732c60:1",
  "hash": "21e3e260b20a765ccac9f1e34455295ada517c3dee6e3adc54fe7a73a2edc5cb",
  "cid": "QmV121e3e260b20a765ccac9f1e34455295ada517c3d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288790,
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
      "evaluated_at": 1760288790
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
  "sig": "d2b9e1075c8f97c3fb32c009a7d28a7c07318441bb275e6c40cb84cf24d6bef3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593769639
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 104, 'threshold': 50, 'total_amount': 44641792, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 103, 'first_seen': 1760285763, 'matching_hash': 'cb8c3421a3879068'}}}