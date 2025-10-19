```json
{
  "id": "dce3844c81b110bf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289657,
  "host_pid": "9e6742732c60:1",
  "hash": "7157dafba556f215c0cff0dd3a3c21a56eff0ce36dbcd0152c7872836ccf9790",
  "cid": "QmV17157dafba556f215c0cff0dd3a3c21a56eff0ce3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289657,
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
      "evaluated_at": 1760289657
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
  "sig": "ade025d7054069442a6dc0ad850ef02619869f20a8c9b258c599e538210d5ed3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009590909791
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 129, 'threshold': 50, 'total_amount': 12229071, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 128, 'first_seen': 1760285765, 'matching_hash': 'dd7dbd0f0c1d6f0c'}}}